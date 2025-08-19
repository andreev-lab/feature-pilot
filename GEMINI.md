# Project Overview

This is an nx monorepo for the Feature Pilot project.

## UI App

The UI application is built with Svelte 5. The source code is located in `apps/feature-pilot`.

### Key technologies

- **Svelte 5:** A modern JavaScript framework for building user interfaces.
- **TypeScript:** A typed superset of JavaScript that compiles to plain JavaScript.
- **Vite:** A fast build tool and development server.
- **Vitest:** A fast unit test framework.
- **Playwright:** A framework for end-to-end testing.

### Getting Started

To start the development server, run the following command:

```bash
npm run serve
```

This will start the Vite development server and open the application in your browser.

## End-to-End Tests

The end-to-end tests are located in `apps/feature-pilot-e2e`. They are written with Playwright.

To run the tests, use the following command:

```bash
nx e2e feature-pilot-e2e
```

## Workspace

This workspace is managed by nx. You can use the nx CLI to generate code, run tasks, and more.

### Useful commands

- `nx graph`: Open the project graph.
- `nx run-many --target=build --all`: Build all projects.
- `nx run-many --target=test --all`: Test all projects.
