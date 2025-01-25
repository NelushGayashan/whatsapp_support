# WhatsApp Support

## Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [Send Message](#1-send-message)
  - [Webhook Handler](#2-webhook-handler)
- [Admin Interface](#admin-interface)
- [Future Improvements](#future-improvements)
- [Assumptions Made](#assumptions-made)
- [License](#license)

## Overview
This Django application demonstrates the integration of WhatsApp messaging into a customer support system. The project provides functionalities to:

- **Store WhatsApp messages** (sender, receiver, content, timestamp, and status).
- **Receive incoming messages** via a webhook.
- **Send WhatsApp messages** using a dedicated API.
- Implement **error handling** and **logging** for better traceability.
- **Admin interface** to view messages, send test messages, and monitor message statuses.

## Features

- **Message Model**: 
   - Store incoming and outgoing WhatsApp messages with essential fields such as sender, receiver, content, status, and timestamp.
   - Allows easy tracking of message history and status.
   
- **Webhook Endpoint**: 
   - Receive incoming WhatsApp messages and save them into the database.
   - Handles payloads securely and stores them in real time.
   
- **Send Message API**: 
   - Sends WhatsApp messages to specified recipients with the option to track message delivery status.
   - Handles asynchronous message sending to optimize performance.
   
- **Admin Interface**: 
   - Easily manage incoming/outgoing messages and monitor their statuses (e.g., sent, failed).
   - Option to send test messages directly through the admin interface for quick validation.
   
- **Async Message Processing**: 
   - Basic async processing for handling messages, improving the responsiveness and performance of the system.
   
- **Logging & Error Handling**: 
   - Simple logging for debugging and troubleshooting errors.
   - Handles common errors gracefully to prevent the system from crashing.

## Tech Stack

- **Python 3.12+**: Latest stable version of Python to ensure maximum compatibility.
- **Django 4.2+**: The latest stable release of Django, an efficient web framework for building scalable applications.
- **Django REST Framework**: A powerful toolkit for building Web APIs.
- **SQLite**: Default database for simplicity in this project (can be switched to more scalable databases in production).

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/NelushGayashan/whatsapp_support.git
    cd whatsapp_support
    ```

2. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the database**:

    Run migrations to set up the necessary database tables:

    ```bash
    python manage.py migrate
    ```

4. **Create a superuser**:

    To access the Django admin interface, create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

5. **Start the server**:

    Start the Django development server:

    ```bash
    python manage.py runserver
    ```

6. **Access the Admin Interface**:

    Open your browser and visit `http://127.0.0.1:8000/admin` to access the Django admin interface. Log in using the superuser credentials created earlier.

## API Endpoints

### 1. **Send Message**
   - **URL**: `/api/send-message/`
   - **Method**: `POST`
   - **Description**: Sends a WhatsApp message to a recipient asynchronously.
   - **Request Body** (JSON):
     ```json
     {
       "sender": "sender_phone_number",
       "receiver": "receiver_phone_number",
       "content": "Message content"
     }
     ```

   - **Response**:
     - **Success** (201):
       ```json
       {
         "message": "Message sent asynchronously",
         "data": {
           "sender": "sender_phone_number",
           "receiver": "receiver_phone_number",
           "content": "Message content",
           "timestamp": "2025-01-25T10:00:00Z"
         }
       }
       ```
     - **Error** (400):
       ```json
       {
         "error": "Invalid payload"
       }
       ```

### 2. **Webhook Handler**
   - **URL**: `/api/webhook/`
   - **Method**: `POST`
   - **Description**: Receives incoming WhatsApp messages and stores them in the database.
   - **Request Body** (JSON):
     ```json
     {
       "sender": "sender_phone_number",
       "receiver": "receiver_phone_number",
       "content": "Received message content"
     }
     ```

   - **Response**:
     - **Success** (200):
       ```json
       {
         "message": "Webhook received asynchronously",
         "data": {
           "sender": "sender_phone_number",
           "receiver": "receiver_phone_number",
           "content": "Received message content",
           "timestamp": "2025-01-25T10:05:00Z"
         }
       }
       ```
     - **Error** (400):
       ```json
       {
         "error": "Invalid payload"
       }
       ```

## Admin Interface

The Django admin interface provides an easy way to interact with the application's data:

- **View incoming and outgoing messages**: Browse the database to see message content, sender, receiver, status, and timestamps.
- **Send test messages**: Use the admin panel to send WhatsApp messages to test the integration.
- **Monitor message statuses**: View and update message statuses (sent, failed, etc.) directly from the admin interface.

## Future Improvements

- **Error handling**: Improve error handling in both the webhook and API endpoints for better fault tolerance.
- **Message retries**: Add logic to retry sending messages in case of failures or timeouts.
- **Message queueing**: Implement a message queue (e.g., Celery) for more scalable message processing.
- **Security**: Add authentication mechanisms (e.g., JWT) to secure the API endpoints.
- **Testing**: Include unit tests for key functionalities like sending/receiving messages and status updates.

## Assumptions Made

- The WhatsApp messages are **text-based** only.
- The incoming webhook payload will always contain the necessary fields (`sender`, `receiver`, `content`).
- API calls assume a valid phone number format for the sender and receiver.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify or extend this documentation as per your needs.
