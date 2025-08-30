# Git Server

This library handles all git actions against the local git CLI.

## Features

*   Find all available repos with their description (README file).
*   Fork a repo.
*   Clone a repo.
*   Push to a repo.
*   Authenticate against git using a username and a Personal Access Token (PAT).

## Architecture

The functionality is wrapped in a FastAPI server. Development will start with simple unit tests to ensure that the required functionality works.