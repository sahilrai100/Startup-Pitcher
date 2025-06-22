import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import axios from 'axios';
import './IdeaCard.css';

const IdeaCard = ({ idea }) => {
  const { isAuthenticated } = useAuth();
  const [likes, setLikes] = useState(idea.likes_count);
  const [isLiked, setIsLiked] = useState(idea.is_liked);
  const [loading, setLoading] = useState(false);

  const handleLike = async () => {
    if (!isAuthenticated) {
      alert('Please login to like ideas');
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post(`/api/ideas/${idea.id}/like/`);
      if (response.data.status === 'liked') {
        setLikes(likes + 1);
        setIsLiked(true);
      } else {
        setLikes(likes - 1);
        setIsLiked(false);
      }
    } catch (error) {
      console.error('Error liking idea:', error);
    } finally {
      setLoading(false);
    }
  };

  const truncateText = (text, maxLength) => {
    if (text.length <= maxLength) return text;
    return text.substring(0, maxLength) + '...';
  };

  return (
    <div className="idea-card card">
      <div className="idea-header">
        <h3 className="idea-title">
          <Link to={`/idea/${idea.id}`}>{idea.title}</Link>
        </h3>
        <div className="idea-meta">
          <span className="pitcher">by {idea.pitcher.username}</span>
          <span className="date">
            {new Date(idea.created_at).toLocaleDateString()}
          </span>
        </div>
      </div>
      
      <p className="idea-description">
        {truncateText(idea.description, 150)}
      </p>
      
      <div className="idea-footer">
        <div className="idea-stats">
          <span className="comments-count">
            💬 {idea.comments?.length || 0} comments
          </span>
          <span className="likes-count">
            ❤️ {likes} likes
          </span>
        </div>
        
        <div className="idea-actions">
          <button
            className={`like-btn ${isLiked ? 'liked' : ''} ${loading ? 'loading' : ''}`}
            onClick={handleLike}
            disabled={loading}
          >
            {isLiked ? '❤️' : '🤍'} {loading ? '...' : ''}
          </button>
          <Link to={`/idea/${idea.id}`} className="btn btn-secondary">
            View Details
          </Link>
        </div>
      </div>
    </div>
  );
};

export default IdeaCard; 