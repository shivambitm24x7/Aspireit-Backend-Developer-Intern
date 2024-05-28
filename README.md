# Aspireit Backend System

## Overview

This project is a simplified version of Aspireit's platform backend, built with Flask. It includes user authentication, MongoDB integration, and a simple sentiment analysis feature.

## Features

- User registration and login
- Profile management
- Sentiment analysis on text data
- Frontend integration using HTML, CSS, and JavaScript

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/shivambitm24x7/Aspireit-Backend-Developer-Intern
    cd Aspireit-Backend-Developer-Intern/
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Start MongoDB:
    ```bash
    mongod
    ```

4. Run the Flask application:
    ```bash
    flask run
    ```

5. Open `localhost:5000` in your browser to access the frontend.

## API Endpoints

 **Access the application**:
    Open your web browser and navigate to `http://127.0.0.1:5000`.

1. **User Registration**

    - **Endpoint:** `/register`
    - **Method:** `POST`
    - **Description:** Registers a new user.
    - **Request Body:**
      ```json
      {
          "username": "string",
          "password": "string"
      }
      ```
    - **Response:**
      - **Success:**
        ```json
        {
            "message": "User registered successfully."
        }
        ```
      - **Failure:**
        ```json
        {
            "message": "User already exists."
        }
        ```

2. **User Login**

    - **Endpoint:** `/login`
    - **Method:** `POST`
    - **Description:** Logs in a user and returns a JWT token.
    - **Request Body:**
      ```json
      {
          "username": "string",
          "password": "string"
      }
      ```
    - **Response:**
      - **Success:**
        ```json
        {
            "access_token": "jwt_token"
        }
        ```
      - **Failure:**
        ```json
        {
            "message": "Invalid credentials."
        }
        ```

3. **Get User Profile**

    - **Endpoint:** `/profile`
    - **Method:** `GET`
    - **Description:** Retrieves the authenticated user's profile.
    - **Headers:**
      ```json
      {
          "Authorization": "Bearer jwt_token"
      }
      ```
    - **Response:**
      ```json
      {
          "username": "string",
          "profile_data": {
              // additional profile data of the user
          }
      }
      ```

4. **Update User Profile**

    - **Endpoint:** `/profile`
    - **Method:** `PUT`
    - **Description:** Updates the authenticated user's profile.
    - **Headers:**
      ```json
      {
          "Authorization": "Bearer jwt_token"
      }
      ```
    - **Request Body:**
      ```json
      {
          "profile_data": {
              // profile data to update
          }
      }
      ```
    - **Response:**
      ```json
      {
          "message": "Profile updated successfully."
      }
      ```

5. **Text Analysis**

    - **Endpoint:** `/analyze`
    - **Method:** `POST`
    - **Description:** Analyzes the sentiment of the provided text.
    - **Headers:**
      ```json
      {
          "Authorization": "Bearer jwt_token"
      }
      ```
    - **Request Body:**
      ```json
      {
          "text": "string"
      }
      ```
    - **Response:**
      ```json
      {
          "polarity": "float",
          "subjectivity": "float"
      }
      ```
      
### Authentication

- `POST /register`: Register a new user
- `POST /login`: User login
- `GET/PUT /profile`: Retrieve/update user profile

### Sentiment Analysis

- `POST /analyze`: Analyze text data for sentiment

## Security Measures

- HTTPS for secure data transmission
- Rate limiting to prevent brute force attacks
- Input sanitization to avoid injection attacks
- Environment variables for sensitive information

## Contact

Shivam Kumar <br>
Phone : +91 98523 21884 <br>
Email : btech10427.19@bitmesra.ac.in  
