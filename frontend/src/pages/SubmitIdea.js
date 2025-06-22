import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import axios from 'axios';
import './SubmitIdea.css';

const SubmitIdea = () => {
  const [formData, setFormData] = useState({
    title: '',
    description: ''
  });
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [loading, setLoading] = useState(false);
  const { isAuthenticated } = useAuth();
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    setLoading(true);

    if (!formData.title.trim() || !formData.description.trim()) {
      setError('Please fill in all fields');
      setLoading(false);
      return;
    }

    if (formData.title.length < 10) {
      setError('Title must be at least 10 characters long');
      setLoading(false);
      return;
    }

    if (formData.description.length < 50) {
      setError('Description must be at least 50 characters long');
      setLoading(false);
      return;
    }

    try {
      const response = await axios.post('/api/ideas/', formData);
      setSuccess('Your idea has been submitted successfully!');
      setFormData({ title: '', description: '' });
      
      setTimeout(() => {
        navigate(`/idea/${response.data.id}`);
      }, 2000);
    } catch (error) {
      setError(error.response?.data?.title?.[0] || 
               error.response?.data?.description?.[0] || 
               'Failed to submit idea. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  if (!isAuthenticated) {
    return (
      <div className="submit-idea-page">
        <div className="container">
          <div className="auth-required card">
            <h2>Authentication Required</h2>
            <p>You need to be logged in to submit startup ideas.</p>
            <button 
              className="btn btn-primary"
              onClick={() => navigate('/login')}
            >
              Go to Login
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="submit-idea-page">
      <div className="container">
        <div className="submit-idea-card card">
          <h2 className="page-title">Share Your Startup Idea</h2>
          <p className="page-subtitle">
            Inspire others with your innovative concept. Be detailed and clear about your vision.
          </p>
          
          {error && <div className="error">{error}</div>}
          {success && <div className="success">{success}</div>}
          
          <form onSubmit={handleSubmit} className="submit-form">
            <div className="form-group">
              <label htmlFor="title">Idea Title *</label>
              <input
                type="text"
                id="title"
                name="title"
                className="form-control"
                value={formData.title}
                onChange={handleChange}
                placeholder="Enter a compelling title for your startup idea (min 10 characters)"
                maxLength="200"
                required
              />
              <small className="char-count">
                {formData.title.length}/200 characters
              </small>
            </div>
            
            <div className="form-group">
              <label htmlFor="description">Description *</label>
              <textarea
                id="description"
                name="description"
                className="form-control"
                value={formData.description}
                onChange={handleChange}
                placeholder="Describe your startup idea in detail. Include the problem it solves, target market, and potential impact. (min 50 characters)"
                rows="8"
                required
              />
              <small className="char-count">
                {formData.description.length} characters (min 50)
              </small>
            </div>
            
            <div className="form-actions">
              <button 
                type="button" 
                className="btn btn-secondary"
                onClick={() => navigate('/')}
              >
                Cancel
              </button>
              <button 
                type="submit" 
                className="btn btn-primary"
                disabled={loading}
              >
                {loading ? 'Submitting...' : 'Submit Idea'}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default SubmitIdea; 