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
    git clone <repo-url>
    cd aspireit_backend
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

Shivam Kumar
Phone : +91 98523 21884
Email : btech10427.19@bitmesra.ac.in  
