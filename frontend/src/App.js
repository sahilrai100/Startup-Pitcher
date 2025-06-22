import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import IdeaDetail from './pages/IdeaDetail';
import SubmitIdea from './pages/SubmitIdea';
import Login from './pages/Login';
import Register from './pages/Register';
import TopIdeas from './pages/TopIdeas';
import Footer from './components/Footer';
import { AuthProvider } from './context/AuthContext';
import './App.css';

function App() {
  const [theme, setTheme] = useState('light');

  useEffect(() => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    setTheme(savedTheme);
    document.documentElement.setAttribute('data-theme', savedTheme);
  }, []);

  const toggleTheme = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
    document.documentElement.setAttribute('data-theme', newTheme);
  };

  return (
    <AuthProvider>
      <Router>
        <div className="App">
          <Navbar theme={theme} toggleTheme={toggleTheme} />
          <main>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/idea/:id" element={<IdeaDetail />} />
              <Route path="/submit" element={<SubmitIdea />} />
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              <Route path="/top-ideas" element={<TopIdeas />} />
            </Routes>
          </main>
          <Footer />
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App; 