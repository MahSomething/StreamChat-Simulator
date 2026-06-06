<div align="center">

# 💬 StreamChat Simulator

**Simulador de live chat estilo Twitch para OBS — overlay transparente, mensagens e utilizadores personalizados.**

---

🌐 **Idioma / Language / Langue**

[![PT](https://img.shields.io/badge/🇧🇷-Português-009c3b?style=for-the-badge)](#-português) &nbsp;
[![EN](https://img.shields.io/badge/🇺🇸-English-3c3b6e?style=for-the-badge)](#-english) &nbsp;
[![FR](https://img.shields.io/badge/🇫🇷-Français-002395?style=for-the-badge)](#-français)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://python.org)
[![OBS](https://img.shields.io/badge/OBS-Studio-purple?style=for-the-badge&logo=obsstudio)](https://obsproject.com)

</div>

---

## 🇧🇷 Português

### O que é?

O **StreamChat Simulator** é uma ferramenta gratuita e de código aberto para criadores de conteúdo que querem simular um chat ao vivo estilo Twitch nos seus vídeos do YouTube, streams ou gravações no OBS.

Também conhecido como **fake chat overlay**, **live chat simulator**, **chat faker para OBS** ou **simulador de chat para YouTube** — resolve um problema real: as ferramentas existentes não permitem personalizar mensagens nem utilizadores.

**Ideal para:**
- 🎵 Canais de música e mix
- 🎮 Canais de gaming
- 🚗 Vídeos de driving/viagens
- 📱 Qualquer criador que queira simular audiência real

---

### ✨ Funcionalidades

- ✅ Overlay transparente no OBS via Browser Source
- ✅ Mensagens e utilizadores 100% personalizáveis
- ✅ Importar/exportar ficheiros `.txt`
- ✅ Modos sequencial, aleatório e loop
- ✅ Badges de sub, mod e vip
- ✅ Intervalo de tempo configurável
- ✅ Efeito de desvanecer nas mensagens antigas
- ✅ Funciona em qualquer computador com Python

---

### 📁 Ficheiros

| Ficheiro | Função |
|---|---|
| `server.py` | Servidor local que faz a comunicação entre o controlador e o OBS |
| `controller.html` | Painel de controlo — configurar e iniciar o chat |
| `overlay.html` | Overlay transparente que aparece no OBS |
| `iniciar-servidor.bat` | Atalho para iniciar o servidor (Windows) |

---

### ✅ Requisitos

- **Python 3.x** → [python.org/downloads](https://python.org/downloads)
  - Durante a instalação marcar ✅ **"Add Python to PATH"**
- **OBS Studio** → [obsproject.com](https://obsproject.com)
- Chrome ou Edge

---

### 🚀 Instalação

1. Descarrega todos os ficheiros para uma pasta
2. Clica duas vezes em `iniciar-servidor.bat`
3. O terminal abre e mostra:

```
MozVibes Chat Server
Controlador : http://localhost:8080/controller.html
Overlay OBS : http://localhost:8080/overlay.html
```

> ⚠️ Não feches o terminal enquanto estiveres a gravar.

---

### 🎮 Como usar

#### 1. Abrir o controlador
```
http://localhost:8080/controller.html
```

#### 2. Configurar o OBS
- **Sources → + → Browser**
- Desmarca ❌ **"Local file"**
- URL: `http://localhost:8080/overlay.html`
- Width: `400` / Height: `600`
- Marca ✅ **"Allow transparency"**
- Custom CSS:
```css
body { background-color: rgba(0,0,0,0) !important; margin: 0; overflow: hidden; }
```

#### 3. Carregar utilizadores e mensagens

**`utilizadores.txt`** — formato:
```
Nome,#cor
AfroVibes,#ff6b6b
MaputoBeats,#4d96ff
KidzVibes,#ffd93d
```

**`mensagens.txt`** — uma mensagem por linha:
```
que música incrível 🔥
banger total 🎶
tô em loop aqui 🔁
```

> 💡 **Gerar ficheiros com IA gratuitamente** — copia este prompt para o ChatGPT, Claude ou Gemini:

```
Gera dois ficheiros de texto para um simulador de chat ao vivo no estilo Twitch.

FICHEIRO 1 — utilizadores.txt
Gera [30] utilizadores com nomes relacionados com [tema do teu canal].
Formato obrigatório: uma linha por utilizador → Nome,#cor

FICHEIRO 2 — mensagens.txt
Gera [300] mensagens de chat relacionadas com [tema do teu canal].
- Uma mensagem por linha
- Em [português/inglês/francês]
- Temas: apreciação do conteúdo, elogios, reacções, emojis, perguntas
- Sem mencionar nomes de pessoas reais ou locais específicos

Responde com os dois ficheiros separados, identificados como:
--- utilizadores.txt ---
(conteúdo)
--- mensagens.txt ---
(conteúdo)
```
> Substitui os valores entre `[ ]` com os teus dados.

#### 4. Iniciar
- Clica **▶ Iniciar** no controlador
- As mensagens aparecem no OBS em tempo real

---

### ⚙️ Opções

| Opção | Descrição |
|---|---|
| Intervalo mín/máx | Tempo entre mensagens (segundos) |
| Modo | Sequencial, Aleatório ou Loop |
| Badges | Sub ⭐ / Mod 🗡️ / Vip 💎 |
| Tamanho da fonte | Tamanho do texto no overlay |

---

### 🔧 Fluxo técnico

```
controller.html → POST → server.py → SSE → overlay.html (OBS)
```

O `server.py` actua como intermediário entre o browser do controlador e o browser interno do OBS (CEF), que são processos separados.

---

---

## 🇺🇸 English

### What is it?

**StreamChat Simulator** is a free, open-source tool for content creators who want to simulate a Twitch-style live chat in their YouTube videos, streams or OBS recordings.

Also known as **fake chat overlay**, **OBS chat simulator**, **live chat faker**, **chatflow overlay** or **stream chat generator** — it solves a real problem: existing tools don't allow custom messages or users.

**Perfect for:**
- 🎵 Music and mix channels
- 🎮 Gaming channels
- 🚗 Driving/travel videos
- 📱 Any creator who wants to simulate real audience engagement

---

### ✨ Features

- ✅ Transparent overlay in OBS via Browser Source
- ✅ 100% customisable messages and users
- ✅ Import/export `.txt` files
- ✅ Sequential, random and loop modes
- ✅ Sub, mod and vip badges
- ✅ Configurable message interval
- ✅ Fade-out effect on older messages
- ✅ Works on any computer with Python

---

### 📁 Files

| File | Purpose |
|---|---|
| `server.py` | Local server handling communication between controller and OBS |
| `controller.html` | Control panel — configure and start the chat |
| `overlay.html` | Transparent overlay displayed in OBS |
| `iniciar-servidor.bat` | Shortcut to start the server (Windows) |

---

### ✅ Requirements

- **Python 3.x** → [python.org/downloads](https://python.org/downloads)
  - During installation check ✅ **"Add Python to PATH"**
- **OBS Studio** → [obsproject.com](https://obsproject.com)
- Chrome or Edge

---

### 🚀 Installation

1. Download all files to a folder
2. Double-click `iniciar-servidor.bat`
3. Terminal opens and shows:

```
StreamChat Simulator Server
Controller : http://localhost:8080/controller.html
OBS Overlay: http://localhost:8080/overlay.html
```

> ⚠️ Do not close the terminal while recording.

---

### 🎮 How to use

#### 1. Open the controller
```
http://localhost:8080/controller.html
```

#### 2. Configure OBS
- **Sources → + → Browser**
- Uncheck ❌ **"Local file"**
- URL: `http://localhost:8080/overlay.html`
- Width: `400` / Height: `600`
- Check ✅ **"Allow transparency"**
- Custom CSS:
```css
body { background-color: rgba(0,0,0,0) !important; margin: 0; overflow: hidden; }
```

#### 3. Load users and messages

**`users.txt`** — format:
```
Name,#color
AfroVibes,#ff6b6b
MaputoBeats,#4d96ff
KidzVibes,#ffd93d
```

**`messages.txt`** — one message per line:
```
this music is incredible 🔥
total banger 🎶
on repeat here 🔁
```

> 💡 **Generate files for free with AI** — copy this prompt to ChatGPT, Claude or Gemini:

```
Generate two text files for a Twitch-style live chat simulator.

FILE 1 — users.txt
Generate [30] users with names related to [your channel theme].
Required format: one per line → Name,#color

FILE 2 — messages.txt
Generate [300] chat messages related to [your channel theme].
- One message per line
- In [English/Portuguese/French]
- Topics: content appreciation, compliments, reactions, emojis, questions
- Do not mention real people's names or specific locations

Reply with both files separated as:
--- users.txt ---
(content)
--- messages.txt ---
(content)
```
> Replace values in `[ ]` with your own.

#### 4. Start
- Click **▶ Start** in the controller
- Messages appear on OBS overlay in real time

---

### ⚙️ Options

| Option | Description |
|---|---|
| Min/Max interval | Time between messages (seconds) |
| Mode | Sequential, Random or Loop |
| Badges | Sub ⭐ / Mod 🗡️ / Vip 💎 |
| Font size | Text size in the overlay |

---

### 🔧 Technical flow

```
controller.html → POST → server.py → SSE → overlay.html (OBS)
```

`server.py` acts as intermediary between the controller browser and OBS's internal browser (CEF), which are completely separate processes.

---

---

## 🇫🇷 Français

### Qu'est-ce que c'est ?

**StreamChat Simulator** est un outil gratuit et open-source pour les créateurs de contenu qui souhaitent simuler un chat en direct style Twitch dans leurs vidéos YouTube, streams ou enregistrements OBS.

Aussi connu sous le nom de **fake chat overlay**, **simulateur de chat OBS**, **chat faker en direct**, **chatflow overlay** ou **générateur de chat stream** — il résout un problème réel : les outils existants ne permettent pas de personnaliser les messages ni les utilisateurs.

**Idéal pour :**
- 🎵 Chaînes de musique et mix
- 🎮 Chaînes gaming
- 🚗 Vidéos de conduite/voyages
- 📱 Tout créateur voulant simuler une vraie audience

---

### ✨ Fonctionnalités

- ✅ Overlay transparent dans OBS via Browser Source
- ✅ Messages et utilisateurs 100% personnalisables
- ✅ Import/export de fichiers `.txt`
- ✅ Modes séquentiel, aléatoire et boucle
- ✅ Badges sub, mod et vip
- ✅ Intervalle de temps configurable
- ✅ Effet de fondu sur les anciens messages
- ✅ Fonctionne sur tout ordinateur avec Python

---

### 📁 Fichiers

| Fichier | Fonction |
|---|---|
| `server.py` | Serveur local gérant la communication entre contrôleur et OBS |
| `controller.html` | Panneau de contrôle — configurer et démarrer le chat |
| `overlay.html` | Overlay transparent affiché dans OBS |
| `iniciar-servidor.bat` | Raccourci pour démarrer le serveur (Windows) |

---

### ✅ Prérequis

- **Python 3.x** → [python.org/downloads](https://python.org/downloads)
  - Pendant l'installation cocher ✅ **"Add Python to PATH"**
- **OBS Studio** → [obsproject.com](https://obsproject.com)
- Chrome ou Edge

---

### 🚀 Installation

1. Téléchargez tous les fichiers dans un dossier
2. Double-cliquez sur `iniciar-servidor.bat`
3. Le terminal s'ouvre et affiche :

```
StreamChat Simulator Server
Contrôleur : http://localhost:8080/controller.html
Overlay OBS: http://localhost:8080/overlay.html
```

> ⚠️ Ne fermez pas le terminal pendant l'enregistrement.

---

### 🎮 Comment utiliser

#### 1. Ouvrir le contrôleur
```
http://localhost:8080/controller.html
```

#### 2. Configurer OBS
- **Sources → + → Browser**
- Décochez ❌ **"Local file"**
- URL : `http://localhost:8080/overlay.html`
- Width : `400` / Height : `600`
- Cochez ✅ **"Allow transparency"**
- Custom CSS :
```css
body { background-color: rgba(0,0,0,0) !important; margin: 0; overflow: hidden; }
```

#### 3. Charger utilisateurs et messages

**`utilisateurs.txt`** — format :
```
Nom,#couleur
AfroVibes,#ff6b6b
MaputoBeats,#4d96ff
KidzVibes,#ffd93d
```

**`messages.txt`** — un message par ligne :
```
quelle musique incroyable 🔥
total banger 🎶
en boucle ici 🔁
```

> 💡 **Générer les fichiers gratuitement avec l'IA** — copiez ce prompt dans ChatGPT, Claude ou Gemini :

```
Génère deux fichiers texte pour un simulateur de chat en direct style Twitch.

FICHIER 1 — utilisateurs.txt
Génère [30] utilisateurs avec des noms liés à [thème de ta chaîne].
Format obligatoire : un par ligne → Nom,#couleur

FICHIER 2 — messages.txt
Génère [300] messages de chat liés à [thème de ta chaîne].
- Un message par ligne
- En [français/anglais/portugais]
- Thèmes : appréciation, compliments, réactions, emojis, questions
- Sans mentionner de vrais noms de personnes ou de lieux spécifiques

Réponds avec les deux fichiers séparés comme suit :
--- utilisateurs.txt ---
(contenu)
--- messages.txt ---
(contenu)
```
> Remplace les valeurs entre `[ ]` par les tiennes.

#### 4. Démarrer
- Cliquez sur **▶ Démarrer** dans le contrôleur
- Les messages apparaissent sur l'overlay OBS en temps réel

---

### ⚙️ Options

| Option | Description |
|---|---|
| Intervalle min/max | Temps entre les messages (secondes) |
| Mode | Séquentiel, Aléatoire ou Boucle |
| Badges | Sub ⭐ / Mod 🗡️ / Vip 💎 |
| Taille de police | Taille du texte dans l'overlay |

---

### 🔧 Flux technique

```
controller.html → POST → server.py → SSE → overlay.html (OBS)
```

`server.py` agit comme intermédiaire entre le navigateur du contrôleur et le navigateur interne d'OBS (CEF), qui sont des processus complètement séparés.

---

<div align="center">

**StreamChat Simulator** — *fake chat overlay · live chat simulator · OBS chat faker · chatflow overlay · stream chat generator · chat sim · overlay chat · chatcast · chatloop · chatreplay*

Made with ❤️ for content creators worldwide

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>
