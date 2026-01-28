# Copilot Instructions for Database with Python Course

## Project Overview
This is a learning project from a Udemy course on databases with Python. The project is structured to demonstrate practical database operations and authentication workflows.

## Project Structure

- **`DataBaser.py`** - Primary database operations module (planned)
- **`index.py`** - Entry point/main application file (planned)
- **`Login/`** - Authentication and user login management module (planned)

## Architecture Patterns

### Separation of Concerns
- **Database Logic**: Keep all database operations isolated in `DataBaser.py`
- **Authentication**: Use `Login/` directory for user authentication workflows
- **Entry Point**: `index.py` should orchestrate the application flow, not contain business logic

### Expected Module Structure
When implementing features:
1. Database operations → `DataBaser.py` or submodules in dedicated directory
2. Authentication/user management → `Login/` package with separate modules
3. Main application flow → `index.py` as application orchestrator

## Database Implementation Guidelines

When building the database module:
- Use a single source of truth for connection strings and configuration
- Implement a connection manager class (e.g., `DatabaseConnection`) to handle connection lifecycle
- Separate SQL queries into logical groups (CRUD operations, queries)
- Use parameterized queries to prevent SQL injection

Example pattern:
```python
# DataBaser.py
class DatabaseConnection:
    def __init__(self, config):
        self.connection = None
    
    def connect(self):
        # Establish connection
        pass
    
    def execute_query(self, query, params):
        # Execute with parameters
        pass
```

## Authentication Module Guidelines

The `Login/` directory should contain:
- User authentication logic (login validation)
- Session management
- User credential handling

Keep sensitive operations in this module and ensure credentials are not logged or exposed.

## Development Workflow

### Running the Application
- Execute `index.py` as the entry point: `python index.py`

### Adding Features
1. Define the feature scope (database, auth, or UI)
2. Implement in the appropriate module
3. Test the component independently before integration
4. Update `index.py` to integrate if it affects application flow

## Key Conventions

- **File Organization**: One class per file when files get large (>200 lines)
- **Naming**: Use PascalCase for classes, snake_case for functions/variables
- **Imports**: Organize imports with standard library first, then third-party, then local
- **Error Handling**: Use specific exception types; avoid bare `except` clauses
- **Configuration**: Store database credentials in environment variables or config files, never in source code

## External Dependencies

Document dependencies as they're added using `requirements.txt`:
```bash
pip freeze > requirements.txt
```

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Notes for AI Agents

- The codebase is in early stages; establish patterns as you implement features
- Follow the directory structure provided — it's a foundation for scalability
- Reference real database operations and authentication flows from the Udemy course
- When uncertain about structure, prioritize separation of concerns
