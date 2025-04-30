# InterviewSim Project Documentation

## Overview
InterviewSim is a web application designed to facilitate mock interviews. It provides a platform for users to practice their interview skills through simulated interviews with AI and peer participants.

## Project Structure
The project is divided into two main parts: the backend and the frontend.

### Backend
- **Framework**: Flask
- **Directory**: `backend/`
  - **app/**: Contains the main application code.
    - **api/**: Defines the API routes and endpoints.
    - **models/**: Contains data models representing the application's data structure.
    - **services/**: Implements business logic and interactions with models.
    - **utils/**: Includes utility functions for various tasks.
  - **.env**: Environment variables for configuration.
  - **app.py**: Main entry point for the backend application.
  - **requirements.txt**: Lists dependencies for the backend.

### Frontend
- **Framework**: React
- **Directory**: `frontend/`
  - **src/**: Contains the source code for the React application.
    - **components/**: Entry point for React components.
    - **services/**: Defines service functions for API interactions.
    - **context/**: Sets up React context for state management.
    - **hooks/**: Contains custom React hooks.
    - **utils/**: Utility functions specific to the frontend.
  - **package.json**: Configuration file for npm.

## Getting Started
To get started with the project, follow these steps:

### Backend Setup
1. Navigate to the `backend` directory.
2. Create a virtual environment and activate it.
3. Install the required packages using `pip install -r requirements.txt`.
4. Set up environment variables in the `.env` file.
5. Run the backend server using `python app.py`.

### Frontend Setup
1. Navigate to the `frontend` directory.
2. Install the required packages using `npm install`.
3. Start the React application using `npm start`.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.