# Azure Practice 3 — Service Bus Integration

## Overview
REST API with Azure Service Bus messaging.

## Components
- FastAPI backend
- Azure SQL Database
- Azure Service Bus Queue
- Background listener (consumer thread)

## Flow
1. Client sends POST /feedbacks
2. Backend saves data to SQL
3. Backend sends message to Service Bus queue
4. Listener receives and prints messages

## Technologies
- FastAPI
- Azure SQL
- Azure Service Bus
- pyodbc
- azure-servicebus

## Endpoint

POST /feedbacks

Example request:
{
  "feedbackId": 1,
  "classId": 1,
  "rating": 5,
  "comment": "Great"
}

## Run

pip install -r requirements.txt
uvicorn main:app --reload

## Notes
- Listener starts on app startup
- Queue polling runs in background thread
- Do not hardcode connection strings
