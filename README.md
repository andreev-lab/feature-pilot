# feature-pilot

feature-pilot is an open-source tool that allows non-technical users like product managers, designers, and salespeople to create working demos and prototypes directly on a real company UI project using a simple chat interface.

The goal is to bridge the gap between idea and implementation, enabling rapid, interactive prototyping on the actual codebase, not a mockup. By being open-source, organizations can self-host the tool, maintain full control over their code, and integrate their own preferred Large Language Models (LLMs).

## Core Idea & Purpose

*   **Empower Non-Developers**: Give non-technical team members the ability to see their ideas come to life by simply describing changes in a chat.
*   **Prototype on Real Code**: Eliminate the waste of building throwaway prototypes. Changes are made in a real git branch on the actual application codebase.
*   **Streamline Collaboration**: Drastically shorten the feedback loop between product, design, and engineering. A working demo is more powerful than a hundred mockups.
*   **Secure & Controllable**: As a self-hosted solution, companies can run it within their own infrastructure, ensuring their code never leaves their control.

## Phase 1: The Local Development Setup

This initial phase focuses on building the core functionality of the application in a local development environment. The architecture is designed to be simple and efficient for development, separating the frontend and backend concerns. The plan is to package this into a distributable desktop app in a later phase.

## High-Level Architecture

The system is composed of two primary, independently running components:

*   **Frontend**: A web-based UI that serves as the user's entire interface. It provides the chat window, a project selection screen, and an iframe to display the target application in real-time.
*   **Backend Server**: A lightweight server that acts as the "brain" of the operation. It receives commands from the frontend, interacts with the LLM, and executes local command-line tools like git and npm to manage the project's code and development server.

```
+---------------------------------+      +-----------------------------------------+
|      UI (Browser)               |      |         Backend Server                  |
|                                 |      |                                         |
|  [ Chat Interface ]             |      |  - FastAPI (for API endpoints)          |
|  [ Project Management ]         |      |  - WebSocket (for real-time logs)       |
|  [ iframe for Target App ]      |      |  - LLM Interaction Service              |
|                                 |      |  - Workspace & File Management          |
+---------------------------------+      |  - Subprocess Executor                  |
             ^                           +-----------------------------------------+
             |                                              |
     (REST API & WebSockets)                                | (Spawns and controls processes)
             |                                              v
             v                           +-----------------------------------------+
+---------------------------------+      |              Local CLI Tools            |
| http://localhost:5173 (UI)      |      |                                         |
| http://localhost:8000 (Server)  |      |  [ Git ]   [ Docker ]   [ npm / yarn ]  |
+---------------------------------+      +-----------------------------------------+
```

### How it Works: A Typical Workflow

1.  A user types a change request (e.g., "Change the primary button color to green") into the UI.
2.  The UI sends this prompt to the backend via a REST API call.
3.  The backend prepares a prompt for the LLM, including the user's request and relevant code context from the local files.
4.  The LLM processes the prompt and returns a code diff.
5.  The backend receives the diff and applies it to the corresponding file on the user's local file system.
6.  The target application's dev server (e.g., Vite), which is running as a long-lived subprocess managed by the backend, detects the file change and triggers a hot-reload.
7.  The iframe in the UI, which points to the target app's localhost URL, automatically updates to show the green button.
8.  Any logs from the dev server (console.log, errors, etc.) are captured by the backend and streamed in real-time to the UI over a WebSocket for debugging.

## Technology Stack

### Frontend

*   **Framework**: SvelteKit
*   **Styling**: Your choice (e.g., Tailwind CSS, plain CSS)
*   **Communication**: `fetch` for API calls, standard `WebSocket` client for real-time logs.

### Backend

*   **Language**: Python 3.10+
*   **Web Framework**: FastAPI (for creating the REST API and WebSocket endpoints)
*   **Process Management**: Python's built-in `subprocess` module to execute and manage CLI commands.

### Development

*   **Backend Environment**: `uv` for dependency isolation.
*   **Frontend Environment**: Node.js and npm/yarn/pnpm.

## Getting Started (Local Development)

This guide assumes you have Python 3.10+, Node.js, and Git installed on your machine.

### 1. Serve backend

```bash
npm run serve:api
```

### 2. Serve frontend 

```bash
npm run serve:ui
```

Once both are running, you can open your browser to `http://localhost:4200` to start using feature-pilot.
