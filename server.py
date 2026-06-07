import http.server
import json
import os
import threading
import time
from urllib.parse import urlparse

# Clientes SSE conectados
clients = []
clients_lock = threading.Lock()

class Handler(http.server.SimpleHTTPRequestHandler):

    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format % args}")

    def do_GET(self):
        parsed = urlparse(self.path)

        # SSE — overlay conecta aqui para receber mensagens
        if parsed.path == '/events':
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Connection', 'keep-alive')
            self.end_headers()

            queue = []
            with clients_lock:
                clients.append(queue)

            print(f"[SSE] Overlay conectado. Total: {len(clients)}")

            try:
                # Envia ping inicial
                self.wfile.write(b'data: {"type":"connected"}\n\n')
                self.wfile.flush()

                while True:
                    if queue:
                        msg = queue.pop(0)
                        data = f'data: {json.dumps(msg)}\n\n'
                        self.wfile.write(data.encode('utf-8'))
                        self.wfile.flush()
                    else:
                        # Keepalive a cada 15s
                        self.wfile.write(b': ping\n\n')
                        self.wfile.flush()
                        time.sleep(15)

            except Exception:
                pass
            finally:
                with clients_lock:
                    if queue in clients:
                        clients.remove(queue)
                print(f"[SSE] Overlay desconectado. Total: {len(clients)}")
            return

        # Ficheiros estáticos
        super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)

        # Receber mensagem do controlador
        if parsed.path == '/send':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)

            try:
                data = json.loads(body)
                with clients_lock:
                    for q in clients:
                        q.append(data)
                print(f"[MSG] Enviado para {len(clients)} overlay(s): {data.get('type','?')}")
            except Exception as e:
                print(f"[ERRO] {e}")

            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
            return

        self.send_response(404)
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == '__main__':
    port = 8080
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = http.server.ThreadingHTTPServer(('', port), Handler)
    print('=' * 45)
    print('  StreamChat Simulator')
    print('=' * 45)
    print(f'  Controlador : http://localhost:{port}/controller.html')
    print(f'  Overlay OBS : http://localhost:{port}/overlay.html')
    print('=' * 45)
    print('  Nao feches esta janela!')
    print('  Para parar: CTRL+C')
    print('=' * 45)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServidor parado.')
