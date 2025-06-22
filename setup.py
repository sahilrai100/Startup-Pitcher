#!/usr/bin/env python3
"""
Setup script for Startup Pitch Platform
This script will initialize the Django project and create a superuser.
"""

import os
import sys
import subprocess
import django
from django.contrib.auth.models import User

def run_command(command, cwd=None):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def setup_django():
    """Setup Django environment and create superuser."""
    print("🚀 Setting up Startup Pitch Platform...")
    
    # Change to backend directory
    backend_dir = os.path.join(os.getcwd(), 'backend')
    if not os.path.exists(backend_dir):
        print("❌ Backend directory not found!")
        return False
    
    os.chdir(backend_dir)
    
    # Install Python dependencies
    print("📦 Installing Python dependencies...")
    success, stdout, stderr = run_command("pip install -r requirements.txt")
    if not success:
        print(f"❌ Failed to install dependencies: {stderr}")
        return False
    print("✅ Dependencies installed successfully!")
    
    # Set Django settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'startup_platform.settings')
    django.setup()
    
    # Run migrations
    print("🗄️ Running database migrations...")
    success, stdout, stderr = run_command("python manage.py makemigrations")
    if not success:
        print(f"❌ Failed to make migrations: {stderr}")
        return False
    
    success, stdout, stderr = run_command("python manage.py migrate")
    if not success:
        print(f"❌ Failed to run migrations: {stderr}")
        return False
    print("✅ Database migrations completed!")
    
    # Create superuser
    print("👤 Creating superuser...")
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            print("✅ Superuser created successfully!")
            print("   Username: admin")
            print("   Password: admin123")
        else:
            print("ℹ️ Superuser already exists!")
    except Exception as e:
        print(f"❌ Failed to create superuser: {e}")
        return False
    
    # Create some sample data
    print("📝 Creating sample data...")
    try:
        from api.models import Idea, Comment, Like
        
        # Create sample users
        user1, created = User.objects.get_or_create(
            username='john_doe',
            defaults={
                'email': 'john@example.com',
                'first_name': 'John',
                'last_name': 'Doe'
            }
        )
        if created:
            user1.set_password('password123')
            user1.save()
        
        user2, created = User.objects.get_or_create(
            username='jane_smith',
            defaults={
                'email': 'jane@example.com',
                'first_name': 'Jane',
                'last_name': 'Smith'
            }
        )
        if created:
            user2.set_password('password123')
            user2.save()
        
        # Create sample ideas
        if not Idea.objects.exists():
            idea1 = Idea.objects.create(
                title="AI-Powered Personal Finance Assistant",
                description="A comprehensive AI-driven platform that helps users manage their finances, track spending, and make smart investment decisions. The app uses machine learning to analyze spending patterns and provide personalized financial advice.",
                pitcher=user1
            )
            
            idea2 = Idea.objects.create(
                title="Sustainable Food Delivery Network",
                description="A zero-waste food delivery service that connects local farmers with consumers, reducing food waste and supporting sustainable agriculture practices. The platform uses eco-friendly packaging and electric vehicles for delivery.",
                pitcher=user2
            )
            
            idea3 = Idea.objects.create(
                title="Virtual Reality Education Platform",
                description="An immersive VR platform for remote learning that creates interactive 3D environments for students. The platform supports multiple subjects and allows teachers to create custom virtual classrooms.",
                pitcher=user1
            )
            
            # Add some likes and comments
            Like.objects.create(user=user2, idea=idea1)
            Like.objects.create(user=user1, idea=idea2)
            Like.objects.create(user=user2, idea=idea3)
            
            Comment.objects.create(
                idea=idea1,
                commenter=user2,
                content="This is a fantastic idea! I would definitely use this app to manage my finances better."
            )
            
            Comment.objects.create(
                idea=idea2,
                commenter=user1,
                content="Great concept! Sustainability is the future of food delivery."
            )
            
            Comment.objects.create(
                idea=idea3,
                commenter=user2,
                content="VR in education has so much potential. This could revolutionize how we learn!"
            )
            
            print("✅ Sample data created successfully!")
        else:
            print("ℹ️ Sample data already exists!")
            
    except Exception as e:
        print(f"❌ Failed to create sample data: {e}")
        return False
    
    print("🎉 Django backend setup completed successfully!")
    return True

def setup_frontend():
    """Setup React frontend."""
    print("\n⚛️ Setting up React frontend...")
    
    frontend_dir = os.path.join(os.getcwd(), '..', 'frontend')
    if not os.path.exists(frontend_dir):
        print("❌ Frontend directory not found!")
        return False
    
    os.chdir(frontend_dir)
    
    # Install Node.js dependencies
    print("📦 Installing Node.js dependencies...")
    success, stdout, stderr = run_command("npm install")
    if not success:
        print(f"❌ Failed to install dependencies: {stderr}")
        return False
    print("✅ Frontend dependencies installed successfully!")
    
    print("🎉 React frontend setup completed successfully!")
    return True

def main():
    """Main setup function."""
    print("=" * 50)
    print("🚀 STARTUP PITCH PLATFORM SETUP")
    print("=" * 50)
    
    # Setup Django backend
    if not setup_django():
        print("❌ Backend setup failed!")
        sys.exit(1)
    
    # Setup React frontend
    if not setup_frontend():
        print("❌ Frontend setup failed!")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("🎉 SETUP COMPLETED SUCCESSFULLY!")
    print("=" * 50)
    print("\n📋 Next steps:")
    print("1. Start the Django backend:")
    print("   cd backend")
    print("   python manage.py runserver")
    print("\n2. Start the React frontend (in a new terminal):")
    print("   cd frontend")
    print("   npm start")
    print("\n3. Access the application:")
    print("   Frontend: http://localhost:3000")
    print("   Backend API: http://localhost:8000")
    print("   Admin Panel: http://localhost:8000/admin")
    print("\n4. Login credentials:")
    print("   Username: admin")
    print("   Password: admin123")
    print("\nHappy coding! 🚀")

if __name__ == "__main__":
    main() 