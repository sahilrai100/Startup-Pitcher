#!/usr/bin/env python3
"""
Script to create sample data for the Startup Pitch Platform
"""

import os
import sys
import django
import random
from datetime import datetime, timedelta

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'startup_platform.settings')
django.setup()

from django.contrib.auth.models import User
from api.models import Idea, Comment, Like

def create_sample_data():
    print("🚀 Creating sample data for Startup Pitch Platform...")
    
    # Create sample users if they don't exist
    users = []
    user_data = [
        {'username': 'john_doe', 'email': 'john@example.com', 'first_name': 'John', 'last_name': 'Doe'},
        {'username': 'jane_smith', 'email': 'jane@example.com', 'first_name': 'Jane', 'last_name': 'Smith'},
        {'username': 'mike_wilson', 'email': 'mike@example.com', 'first_name': 'Mike', 'last_name': 'Wilson'},
        {'username': 'sarah_jones', 'email': 'sarah@example.com', 'first_name': 'Sarah', 'last_name': 'Jones'},
        {'username': 'alex_chen', 'email': 'alex@example.com', 'first_name': 'Alex', 'last_name': 'Chen'},
        {'username': 'emma_davis', 'email': 'emma@example.com', 'first_name': 'Emma', 'last_name': 'Davis'},
        {'username': 'david_brown', 'email': 'david@example.com', 'first_name': 'David', 'last_name': 'Brown'},
        {'username': 'lisa_garcia', 'email': 'lisa@example.com', 'first_name': 'Lisa', 'last_name': 'Garcia'},
    ]
    
    for user_info in user_data:
        user, created = User.objects.get_or_create(
            username=user_info['username'],
            defaults=user_info
        )
        if created:
            user.set_password('password123')
            user.save()
            print(f"✅ Created user: {user.username}")
        users.append(user)
    
    # Sample startup ideas
    ideas_data = [
        {
            'title': 'AI-Powered Personal Finance Assistant',
            'description': 'A comprehensive AI-driven platform that helps users manage their finances, track spending, and make smart investment decisions. The app uses machine learning to analyze spending patterns and provide personalized financial advice, helping users save money and achieve their financial goals.',
            'pitcher': users[0]
        },
        {
            'title': 'Sustainable Food Delivery Network',
            'description': 'A zero-waste food delivery service that connects local farmers with consumers, reducing food waste and supporting sustainable agriculture practices. The platform uses eco-friendly packaging and electric vehicles for delivery, making it the greenest food delivery option available.',
            'pitcher': users[1]
        },
        {
            'title': 'Virtual Reality Education Platform',
            'description': 'An immersive VR platform for remote learning that creates interactive 3D environments for students. The platform supports multiple subjects and allows teachers to create custom virtual classrooms, making education more engaging and accessible.',
            'pitcher': users[2]
        },
        {
            'title': 'Smart Home Energy Management System',
            'description': 'An intelligent system that optimizes home energy consumption using IoT sensors and machine learning algorithms. It automatically adjusts heating, cooling, and lighting based on usage patterns, helping homeowners reduce energy bills by up to 30%.',
            'pitcher': users[3]
        },
        {
            'title': 'Mental Health AI Companion',
            'description': 'A 24/7 AI-powered mental health companion that provides emotional support, mood tracking, and guided meditation sessions. The app uses natural language processing to understand user emotions and offers personalized coping strategies.',
            'pitcher': users[4]
        },
        {
            'title': 'Blockchain-Based Supply Chain Tracker',
            'description': 'A transparent supply chain tracking system using blockchain technology to ensure product authenticity and ethical sourcing. Companies can track their products from raw materials to final delivery, building trust with consumers.',
            'pitcher': users[5]
        },
        {
            'title': 'Drone-Based Urban Delivery Service',
            'description': 'An autonomous drone delivery service for urban areas that can deliver packages within 30 minutes. The service uses advanced navigation systems and weather monitoring to ensure safe and efficient deliveries.',
            'pitcher': users[6]
        },
        {
            'title': 'Personalized Fitness AI Trainer',
            'description': 'An AI-powered fitness trainer that creates personalized workout plans based on user goals, fitness level, and available equipment. The app provides real-time form correction and motivation to help users achieve their fitness goals.',
            'pitcher': users[7]
        },
        {
            'title': 'Smart Parking Solution',
            'description': 'A mobile app that helps drivers find available parking spots in real-time using IoT sensors and crowd-sourced data. The app reduces traffic congestion and saves drivers time by directing them to the nearest available parking space.',
            'pitcher': users[0]
        },
        {
            'title': 'Eco-Friendly Personal Care Products',
            'description': 'A subscription service for sustainable personal care products made from natural, biodegradable ingredients. The company uses refillable containers and carbon-neutral shipping to minimize environmental impact.',
            'pitcher': users[1]
        }
    ]
    
    # Sample comments
    sample_comments = [
        "This is absolutely brilliant! I would definitely use this.",
        "Great concept! The market potential is huge.",
        "I love the sustainability aspect of this idea.",
        "This could really solve a major problem in the industry.",
        "The technology behind this is fascinating.",
        "I can see this becoming very popular quickly.",
        "This addresses a real need in the market.",
        "The user experience design sounds amazing.",
        "This has the potential to disrupt the entire industry.",
        "I'm impressed by the innovation here.",
        "This could make a real difference in people's lives.",
        "The scalability of this idea is impressive.",
        "I love how user-friendly this concept is.",
        "This could be a game-changer for the sector.",
        "The business model looks very promising.",
        "I can see this becoming a household name.",
        "This idea has excellent market timing.",
        "The technology stack choice is perfect.",
        "This could create a whole new market category.",
        "I'm excited to see this come to life!",
        "This addresses a pain point I've experienced personally.",
        "The potential for growth is enormous.",
        "This could revolutionize how we think about this problem.",
        "I love the attention to detail in this concept.",
        "This has all the ingredients for success."
    ]
    
    # Create ideas and add random likes/comments
    for i, idea_data in enumerate(ideas_data):
        # Create the idea
        idea = Idea.objects.create(
            title=idea_data['title'],
            description=idea_data['description'],
            pitcher=idea_data['pitcher']
        )
        
        # Add random likes (between 5 and 25)
        num_likes = random.randint(5, 25)
        users_to_like = random.sample(users, min(num_likes, len(users)))
        
        for user in users_to_like:
            Like.objects.create(user=user, idea=idea)
        
        # Add random comments (between 2 and 8)
        num_comments = random.randint(2, 8)
        commenters = random.sample(users, min(num_comments, len(users)))
        
        for j, commenter in enumerate(commenters):
            comment_text = random.choice(sample_comments)
            Comment.objects.create(
                idea=idea,
                commenter=commenter,
                content=comment_text
            )
        
        print(f"✅ Created idea: {idea.title} ({num_likes} likes, {num_comments} comments)")
    
    print(f"\n🎉 Successfully created {len(ideas_data)} startup ideas with random likes and comments!")
    print(f"📊 Total users: {len(users)}")
    print(f"💡 Total ideas: {Idea.objects.count()}")
    print(f"❤️ Total likes: {Like.objects.count()}")
    print(f"💬 Total comments: {Comment.objects.count()}")

if __name__ == "__main__":
    create_sample_data() 