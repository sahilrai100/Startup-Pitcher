import React, { useState, useEffect } from 'react';
import axios from 'axios';
import IdeaCard from '../components/IdeaCard';
import './TopIdeas.css';

const TopIdeas = () => {
  const [ideas, setIdeas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchTopIdeas();
  }, []);

  const fetchTopIdeas = async () => {
    try {
      const response = await axios.get('/api/ideas/');
      setIdeas(response.data.results || response.data);
    } catch (error) {
      setError('Failed to load top ideas');
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

  if (error) {
    return (
      <div className="top-ideas-page">
        <div className="container">
          <div className="error">{error}</div>
        </div>
      </div>
    );
  }

  return (
    <div className="top-ideas-page">
      <div className="container">
        <div className="page-header">
          <h1 className="page-title">🔥 Top Startup Ideas</h1>
          <p className="page-subtitle">
            Discover the most popular and innovative startup ideas from our community
          </p>
        </div>

        {ideas.length === 0 ? (
          <div className="no-ideas">
            <h3>No ideas yet!</h3>
            <p>Be the first to share your startup idea and inspire others.</p>
          </div>
        ) : (
          <div className="ideas-grid">
            {ideas.map((idea) => (
              <IdeaCard key={idea.id} idea={idea} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default TopIdeas; 