import React from 'react';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-section">
            <h3>🚀 Startup Pitch Platform</h3>
            <p>Share your innovative startup ideas and discover amazing concepts from entrepreneurs worldwide.</p>
          </div>
          
          <div className="footer-section">
            <h4>Quick Links</h4>
            <ul>
              <li><a href="/">Home</a></li>
              <li><a href="/top-ideas">Top Ideas</a></li>
              <li><a href="/submit">Submit Idea</a></li>
            </ul>
          </div>
          
          <div className="footer-section">
            <h4>Connect</h4>
            <ul>
              <li><a href="/login">Login</a></li>
              <li><a href="/register">Register</a></li>
            </ul>
          </div>
          
          <div className="footer-section">
            <h4>About</h4>
            <p>Built with ❤️ by Sahil Rai</p>
            <p>Django + React + SQLite</p>
          </div>
        </div>
        
        <div className="footer-bottom">
          <p>&copy; 2024 Startup Pitch Platform. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer; 