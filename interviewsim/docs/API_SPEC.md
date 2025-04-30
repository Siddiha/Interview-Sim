# API Specification for InterviewSim

## Overview
This document outlines the API specifications for the InterviewSim application. It includes details about the available endpoints, request and response formats, and authentication methods.

## Base URL
The base URL for the API is:
```
http://localhost:5000/api
```

## Endpoints

### 1. User Authentication

#### POST /auth/login
- **Description**: Authenticates a user and returns a token.
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "token": "string"
    }
    ```
  - **401 Unauthorized**:
    ```json
    {
      "error": "Invalid credentials"
    }
    ```

### 2. Interviews

#### GET /interviews
- **Description**: Retrieves a list of interviews.
- **Response**:
  - **200 OK**:
    ```json
    [
      {
        "id": "integer",
        "title": "string",
        "date": "string",
        "participants": ["string"]
      }
    ]
    ```

#### POST /interviews
- **Description**: Creates a new interview.
- **Request Body**:
  ```json
  {
    "title": "string",
    "date": "string",
    "participants": ["string"]
  }
  ```
- **Response**:
  - **201 Created**:
    ```json
    {
      "id": "integer",
      "title": "string",
      "date": "string",
      "participants": ["string"]
    }
    ```

### 3. Feedback

#### POST /feedback
- **Description**: Submits feedback for an interview.
- **Request Body**:
  ```json
  {
    "interviewId": "integer",
    "comments": "string",
    "rating": "integer"
  }
  ```
- **Response**:
  - **201 Created**:
    ```json
    {
      "message": "Feedback submitted successfully"
    }
    ```

## Authentication
All endpoints except for `/auth/login` require a valid token in the `Authorization` header:
```
Authorization: Bearer <token>
```

## Error Handling
All responses will include an appropriate HTTP status code and a JSON object with an error message when applicable. 

## Conclusion
This API specification serves as a guide for developers to understand the available endpoints and their usage within the InterviewSim application.