# Startup Idea Pitching Platform

A platform where users can pitch their startup ideas and others can view, like, and comment on them.

## Features

### 🎯 Core Features
- **Hero Section**: Background image with heading and call-to-action buttons
- **Top 5 Ideas**: Sorted by likes, displayed on homepage
- **Netflix-style Slider**: For remaining ideas
- **Idea Detail Pages**: Complete view with title, description, pitcher, likes, and comments
- **Commenting System**: Only logged-in users can comment
- **Like Feature**: One like per user per idea
- **Motivational Quotes**: Auto-changing quote section
- **Dark/Light Mode**: Toggle with localStorage persistence
- **Responsive Design**: Mobile, tablet, and desktop optimized

### 🔐 Authentication & User Types
- **Visitor**: Can view ideas and comments
- **Registered User**: Can like ideas and post comments
- **Pitcher (Idea Creator)**: Can submit ideas, edit their own ideas only

### 🧱 Backend Features (Django)
- User Registration & Login via Django auth
- Idea Model with title, description, pitcher, likes
- Comment Model linked to ideas and commenters
- Like logic (one like per user per idea)
- Authorization (users can only edit their own ideas)
- REST API endpoints for all functionality

## Tech Stack

- **Frontend**: React (CSS + JS only, NO Tailwind)
- **Backend**: Django + Django REST Framework
- **Database**: SQLite
- **Authentication**: Django Authentication

## Project Structure

```
startup-pitch-platform/
├── backend/                 # Django backend
│   ├── manage.py
│   ├── requirements.txt
│   ├── startup_platform/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── api/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       └── urls.py
├── frontend/               # React frontend
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── styles/
│   │   └── App.js
│   ├── package.json
│   └── README.md
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd startup-pitch-platform
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm start
   ```

4. **Access the application**
   - Backend API: http://localhost:8000
   - Frontend: http://localhost:3000

## API Endpoints

- `GET /api/ideas/` - Get all ideas
- `POST /api/ideas/` - Create new idea (authenticated)
- `GET /api/ideas/{id}/` - Get specific idea
- `PUT /api/ideas/{id}/` - Update idea (owner only)
- `DELETE /api/ideas/{id}/` - Delete idea (owner only)
- `POST /api/ideas/{id}/like/` - Like/unlike idea
- `GET /api/ideas/{id}/comments/` - Get comments for idea
- `POST /api/ideas/{id}/comments/` - Add comment (authenticated)
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout

## Author

**Sahil Rai**
 
