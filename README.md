# FastAPI Testing Framework

### Python | Pytest | Requests | REST API Testing | JWT Authentication

## Overview

This project is a Python-based API automation testing framework developed using Pytest and the Requests library to automate testing of a FastAPI-based application.

The framework focuses on testing authentication and student management functionalities through REST API requests.

It follows a modular architecture by separating API client methods, test cases, test data, and reusable utility functions.

The framework supports authenticated API requests using JWT Bearer tokens and provides reusable methods for performing different HTTP operations.

## Key Features

- **API Automation:** Automates REST API testing using Python Requests.
- **Pytest Framework:** Organizes and executes API test cases.
- **Reusable API Clients:** Maintains separate client methods for authentication and student management operations.
- **JWT Authentication:** Generates access tokens through login requests.
- **Bearer Token Authorization:** Uses JWT tokens in request headers to access protected endpoints.
- **Reusable Fixtures:** Uses Pytest fixtures to manage authentication tokens and test prerequisites.
- **CRUD Operations:** Supports GET, PUT, PATCH, and DELETE operations for student accounts.
- **Centralized Routes:** Maintains API endpoint URLs in a dedicated routes module.
- **Modular Architecture:** Separates API clients, test cases, and utility functions.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pytest | Test execution framework |
| Requests | HTTP API communication |
| JWT | Token-based authentication |
| REST API | API communication architecture |
| FastAPI | Backend application framework |

## Project Structure

```text
FastApi_testing_framework/
│
├── Fast_Api/
│
├── api_client/
│   ├── auth_client.py
│   └── student_client.py
│
├── test_cases/
│
├── tests/
│
├── utils/
│   ├── helper_fun.py
│   └── routes.py
│
└── conftest.py
```

## Folder Description

| Folder/File | Description |
|---|---|
| `Fast_Api/` | Contains the FastAPI application-related components. |
| `api_client/` | Contains reusable API request methods. |
| `auth_client.py` | Handles login and registration API requests. |
| `student_client.py` | Handles student account GET, PUT, PATCH, and DELETE operations. |
| `test_cases/` | Contains API test scenarios. |
| `tests/` | Contains test-related modules. |
| `utils/` | Contains reusable helper functions and API configurations. |
| `helper_fun.py` | Handles JWT access token generation and token decoding. |
| `routes.py` | Centralizes API endpoint URLs. |
| `conftest.py` | Contains reusable Pytest fixtures for authentication and test setup. |

## API Functionalities

### 1. Authentication

The framework provides reusable API clients for:

- User Login
- User Registration

The login API returns an access token, which is used for authenticated requests.

### 2. Student Management

The framework implements the following student account operations:

| HTTP Method | Operation | Description |
|---|---|---|
| GET | Retrieve Student | Retrieves the authenticated student's account or an account using an ID. |
| PUT | Update Student | Updates student account information. |
| PATCH | Partial Update | Updates selected student account fields. |
| DELETE | Delete Student | Deletes the authenticated student's account or an account using an ID. |

### 3. JWT Authentication

The framework generates access tokens using login credentials.

The token is then passed through the Authorization header.

Example:

```python
def headers(token):
    return {
        "Authorization": f"Bearer {token}"
    } if token else {}
```

This allows the framework to execute authenticated API requests.

## Framework Execution Flow

1. Pytest discovers the test cases.
2. Fixtures defined in `conftest.py` are initialized.
3. Authentication credentials are passed to the login API.
4. The login response provides a JWT access token.
5. The token is reused for authenticated API requests.
6. API client methods execute the required HTTP operations.
7. Test cases validate the API responses.
8. Pytest reports the execution results.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Eswar508/FastApi_testing_framework.git
```

### 2. Navigate to the Project Directory

```bash
cd FastApi_testing_framework
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install fastapi uvicorn pytest requests PyJWT
```

The configured API base URL is:

```text
http://127.0.0.1:8000
```

## Running Test Cases

Start the API in a first terminal from the `Fast_Api` folder:

```powershell
cd Fast_Api
python -m uvicorn FastApi.routes.main:app --reload
```

Keep the API running. In a second terminal, from the repository root, run:

Execute all test cases:

```bash
python -m pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run tests with detailed console output:

```bash
pytest -v -s
```

Execute a specific test file:

```bash
pytest test_cases/test_filename.py -v
```

Replace `test_filename.py` with the actual test file name.

## Authentication and Test Fixtures

The framework uses Pytest fixtures defined in `conftest.py`.

The fixtures provide reusable authentication tokens for different user roles:

- Admin authentication token.
- Student authentication token.
- Admin update token.
- Student update token.

Additional fixtures handle deleted student accounts and deleted user tokens.

This approach reduces repeated login operations and simplifies test setup.

## Design Approach

The framework follows a modular API automation architecture.

**API Client Layer**

Contains reusable methods responsible for sending HTTP requests to API endpoints.

**Utility Layer**

Contains common helper functions for JWT token generation, token decoding, and API route configuration.

**Test Layer**

Contains test scenarios that validate API functionality and response behavior.

**Fixture Layer**

Uses Pytest fixtures to manage authentication and test prerequisites.

This separation improves code reusability, maintainability, and test organization.

## Future Enhancements

- Implement data-driven API testing.
- Add response schema validation.
- Introduce negative and boundary test scenarios.
- Implement centralized logging.
- Add HTML or Allure reporting.
- Implement environment-based API configuration.
- Integrate automated testing with GitHub Actions.
- Improve test data management and cleanup.

## Author

**Eswar**

GitHub: Eswar508

---

*This project demonstrates Python-based REST API automation using Pytest, Requests, and JWT authentication.*
