# Project Overview

This is an nx monorepo for the Feature Pilot project.

## UI App

The UI application is built with Svelte 5. The source code is located in `apps/feature-pilot`.

## When finishing a task
Don't serve the apps it will give you nothing, you'll get stuck waiting for the process to finish and it never will.

## Code Style
1. **Important** Don't touch the project.toml / project.json / package.json when working on code features, it is acceptable only when there is a configuration issue!
2. **Important** Never run `npm i` inside of a lib, all dependencies are global and are shared with all libs and apps.
3. Use 2 space indents.
4. In each file / class, properties / methods / vars / classes that aren't exported should be private. In TS use # for classes, in python use __ as a prefix.
5. Don't add comments.
6. For ui always use typescript for script lang and scss for style lang.

### Key technologies

- **Svelte 5:** A modern JavaScript framework for building user interfaces.
- **TypeScript:** A typed superset of JavaScript that compiles to plain JavaScript.
- **Vite:** A fast build tool and development server.
- **Vitest:** A fast unit test framework.
- **Playwright:** A framework for end-to-end testing.

## Workspace

This workspace is managed by nx. Use nx MCP server to update / create / delete apps and libs.
