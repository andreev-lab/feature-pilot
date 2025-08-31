# Strategic Plan: Integrate TinyDB into the Python Server

## 1. Understanding the Goal
The primary objective is to integrate TinyDB, a lightweight, file-based database, into the existing Python server stack. This involves installing the dependency, initializing the database, and using it to store and retrieve user authentication tokens for GitHub API interactions. A health check endpoint will also be created to monitor the database's status.

## 2. Investigation & Analysis
To ensure a smooth and non-disruptive integration, the following investigative steps will be performed:

*   **Dependency Management:**
    *   Examine the `pyproject.toml` file within the `libs/infra/server/core` library to understand its current dependency structure.
    *   Identify the project name for `libs/infra/server/core` by inspecting its `project.json` file. This is crucial for using the correct `nx` commands.
    *   Research the appropriate `nx` command for adding a Python dependency to a specific project within the monorepo.

*   **Code Structure & Initialization:**
    *   Analyze `apps/api/src/main.py` to determine the application's entry point and the best place to hook in the database initialization, adhering to the principle that logic should reside in libraries.
    *   Review the contents of `libs/infra/server/core/src` to find a suitable location for the new database module, or to determine if a new file is needed.

*   **Token Handling:**
    *   Read `libs/git/server/src/git_server/git_service.py` to trace how the GitHub authentication token is currently managed and identify the exact location to insert the database write operation.
    *   Read `libs/git/server/src/git_server/github_sdk.py` to understand how the token is accessed for API calls and where to replace this with a database read operation.

*   **Project Dependencies:**
    *   Utilize `nx workspace` to visualize the project graph and confirm the dependency flow to avoid introducing circular dependencies. The intended flow is `api` -> `git-server` -> `infra-server-core`.

## 3. Proposed Strategic Approach
The integration will be executed in a phased manner to ensure modularity and testability.

1.  **Install Dependency:**
    *   Add `tinydb` as a dependency to the `infra-server-core` project using the appropriate `nx` command (e.g., `nx add-dependency infra-server-core tinydb`).

2.  **Create Database Module:**
    *   Create a new file: `libs/infra/server/core/src/database.py`.
    *   Inside this file, define a singleton pattern or a memoized function (e.g., using `functools.lru_cache`) to manage a single instance of the `TinyDB` database. This function, say `get_db()`, will prevent multiple file handles and ensure consistent access. The database file itself (`db.json`) should be stored in a non-version-controlled location.

3.  **Integrate DB into Services:**
    *   In `libs/git/server/src/git_server/git_service.py`, import `get_db` from the `infra` library. In the function responsible for handling the user token, use the database instance to `upsert` the token. A specific table for credentials will be used.
    *   In `libs/git/server/src/git_server/github_sdk.py`, also import `get_db`. Modify the code that prepares API requests to fetch the token from the database instead of its current source.

4.  **Expose Health Check:**
    *   In the main application file, `apps/api/src/main.py`, create a new FastAPI endpoint `/health`.
    *   This endpoint will call `get_db()` and perform a simple, non-intrusive read operation (like counting documents) to verify that the database is accessible and responsive. It will return a `200 OK` status on success or a `503 Service Unavailable` on failure.

## 4. Verification Strategy
Success will be measured through a combination of automated testing and manual verification.

*   **Automated Tests:**
    *   A new unit test will be created for the `database.py` module to verify the singleton/memoization behavior.
    *   Existing tests for `git_service.py` and `github_sdk.py` will be updated to mock the `get_db` function, allowing for isolated testing of the token storage and retrieval logic without a real database file.
    *   A new integration test for the `/health` endpoint will be added to the `api` application's test suite.

*   **Manual End-to-End Testing:**
    *   Run the application stack.
    *   Perform the action that triggers GitHub authentication to confirm the token is saved to the `db.json` file.
    *   Access the `/health` endpoint via a browser or `curl` to confirm it returns a success status.
    *   Execute a feature that relies on the GitHub SDK to ensure it correctly retrieves and uses the token from the database.

## 5. Anticipated Challenges & Considerations
*   **Database File Location:** A clear decision must be made on where to store the `db.json` file. A user-specific directory outside the project structure is preferable for a local application to avoid conflicts and ensure it is not committed to version control. This path needs to be managed gracefully.
*   **Concurrency:** TinyDB is not inherently thread-safe. Since FastAPI uses a thread pool, there is a risk of concurrent writes causing data corruption. The implementation must include a thread lock (`threading.Lock`) around all database write operations to ensure safety.
*   **Configuration Management:** The path to the database file should be configurable, perhaps via an environment variable, rather than being hardcoded. This provides flexibility for different environments and users.
*   **Error Handling:** Robust error handling must be added around all database interactions to gracefully manage scenarios like file permissions errors, disk full errors, or corrupted database files.
