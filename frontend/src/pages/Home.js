import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import IdeaCard from '../components/IdeaCard';
import './Home.css';

const Home = () => {
  const [topIdeas, setTopIdeas] = useState([]);
  const [allIdeas, setAllIdeas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [currentQuoteIndex, setCurrentQuoteIndex] = useState(0);

  const motivationalQuotes = [
   "I don’t believe in taking right decisions. I take decisions and then make them right. - Ratan Tata",
  "If you are born poor it's not your mistake, but if you die poor it's your mistake. - Narayana Murthy",
  "An entrepreneur is someone who dares to dream and is determined to make it happen. - Kiran Mazumdar-Shaw",
  "Ideas are easy. Implementation is hard. - Nandan Nilekani",
  "It’s not about ideas. It’s about making ideas happen. - Ritesh Agarwal",
  "Risk-taking is the essence of entrepreneurship. - Bhavish Aggarwal",
  "Build something you're passionate about; the rest will follow. - Vijay Shekhar Sharma",
  "Startups are about finding a scalable and repeatable business model. - Alok Kejriwal",
  "You don’t need a big company to start with. You need a big vision. - Byju Raveendran",
  "If you fully accept the worst that can ever happen in your journey, fear won’t ever be an obstacle. - Naval Ravikant"
  ];

  useEffect(() => {
    fetchIdeas();
    const quoteInterval = setInterval(() => {
      setCurrentQuoteIndex((prev) => (prev + 1) % motivationalQuotes.length);
    }, 5000);
    return () => clearInterval(quoteInterval);
  }, []);

  const fetchIdeas = async () => {
    try {
      const [topResponse, allResponse] = await Promise.all([
        axios.get('/api/top-ideas/'),
        axios.get('/api/ideas/')
      ]);
      
      setTopIdeas(topResponse.data);
      setAllIdeas(allResponse.data.results || allResponse.data);
    } catch (error) {
      console.error('Error fetching ideas:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="loading">
        <div className="spinner"></div>
      </div>
    );
  }

  return (
    <div className="home">
      {/* Hero Section */}
      <section className="hero">
        <div className="container">
          <div className="hero-content">
            <h1 className="hero-title">
              Share Your <span className="highlight">Startup Ideas</span>
            </h1>
            <p className="hero-subtitle">
              Connect with fellow entrepreneurs, get feedback, and discover the next big thing in the startup world.
            </p>
            <div className="hero-buttons">
              <Link to="/submit" className="btn btn-primary">Get Started</Link>
              <Link to="/top-ideas" className="btn btn-secondary">Blogs</Link>
            </div>
          </div>
        </div>
      </section>

      {/* Top 5 Ideas Section */}
      <section className="top-ideas-section">
        <div className="container">
          <h2 className="section-title">🔥 Top Ideas</h2>
          <div className="ideas-grid">
            {topIdeas.map((idea) => (
              <IdeaCard key={idea.id} idea={idea} />
            ))}
          </div>
        </div>
      </section>

      {/* Netflix-style Slider for Other Ideas */}
      <section className="other-ideas-section">
        <div className="container">
          <h2 className="section-title">💡 More Ideas</h2>
          <div className="ideas-slider">
            {allIdeas.slice(5).map((idea) => (
              <div key={idea.id} className="slider-item">
                <IdeaCard idea={idea} />
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Motivational Quotes Section */}
      <section className="quotes-section">
        <div className="container">
          <div className="quote-card">
            <p className="quote-text">"{motivationalQuotes[currentQuoteIndex]}"</p>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home; 