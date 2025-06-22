@echo off
echo Starting Startup Pitch Platform...
echo.

echo Starting Django Backend...
cd backend
start "Django Backend" cmd /k "python manage.py runserver"

echo Starting React Frontend...
cd ../frontend
start "React Frontend" cmd /k "npm start"

echo.
echo Both servers are starting...
echo Backend will be available at: http://localhost:8000
echo Frontend will be available at: http://localhost:3000
echo.
pause 