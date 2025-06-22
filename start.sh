#!/bin/bash

echo "Starting Startup Pitch Platform..."
echo

echo "Starting Django Backend..."
cd backend
python manage.py runserver &
BACKEND_PID=$!

echo "Starting React Frontend..."
cd ../frontend
npm start &
FRONTEND_PID=$!

echo
echo "Both servers are starting..."
echo "Backend will be available at: http://localhost:8000"
echo "Frontend will be available at: http://localhost:3000"
echo
echo "Press Ctrl+C to stop both servers"

# Wait for user to stop the servers
trap "echo 'Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait 