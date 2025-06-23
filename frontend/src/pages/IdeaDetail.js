import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import axios from 'axios';
import './IdeaDetail.css';

const IdeaDetail = () => {
  const { id } = useParams();
  const { isAuthenticated } = useAuth();
  const navigate = useNavigate();
  
  const [idea, setIdea] = useState(null);
  const [comments, setComments] = useState([]);
  const [newComment, setNewComment] = useState('');
  const [loading, setLoading] = useState(true);
  const [commentLoading, setCommentLoading] = useState(false);
  const [likes, setLikes] = useState(0);
  const [isLiked, setIsLiked] = useState(false);
  const [likeLoading, setLikeLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (id && id !== 'undefined') {
      fetchIdea();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [id]);

  // Guard for undefined id (after hooks)
  if (!id || id === 'undefined') {
    return (
      <div className="idea-detail-page">
        <div className="container">
          <div className="error">Invalid idea ID. Please return to the home page and select a valid idea.</div>
        </div>
      </div>
    );
  }

  const fetchIdea = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`/api/ideas/${id}/`);
      setIdea(response.data);
      setComments(response.data.comments || []);
      setLikes(response.data.likes_count);
      setIsLiked(response.data.is_liked);
    } catch (error) {
      setError('Failed to load idea');
      console.error('Error fetching idea:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleLike = async () => {
    if (!isAuthenticated) {
      alert('Please login to like ideas');
      return;
    }

    setLikeLoading(true);
    try {
      const response = await axios.post(`/api/ideas/${id}/like/`);
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
      setLikeLoading(false);
    }
  };

  const handleCommentSubmit = async (e) => {
    e.preventDefault();
    if (!newComment.trim()) return;

    setCommentLoading(true);
    try {
      const response = await axios.post(`/api/ideas/${id}/add_comment/`, {
        content: newComment
      });
      setComments([response.data, ...comments]);
      setNewComment('');
    } catch (error) {
      console.error('Error posting comment:', error);
    } finally {
      setCommentLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="loading">
        <div className="spinner"></div>
      </div>
    );
  }

  if (error || !idea) {
    return (
      <div className="idea-detail-page">
        <div className="container">
          <div className="error">{error || 'Idea not found'}</div>
        </div>
      </div>
    );
  }

  return (
    <div className="idea-detail-page">
      <div className="container">
        <div className="idea-detail-card card">
          <div className="idea-header">
            <h1 className="idea-title">{idea.title}</h1>
            <div className="idea-meta">
              <span className="pitcher">by {idea.pitcher.username}</span>
              <span className="date">
                {new Date(idea.created_at).toLocaleDateString()}
              </span>
            </div>
          </div>

          <div className="idea-content">
            <p className="idea-description">{idea.description}</p>
          </div>

          <div className="idea-actions">
            <div className="idea-stats">
              <span className="likes-count">
                ❤️ {likes} likes
              </span>
              <span className="comments-count">
                💬 {comments.length} comments
              </span>
            </div>

            <div className="action-buttons">
              <button
                className={`like-btn ${isLiked ? 'liked' : ''} ${likeLoading ? 'loading' : ''}`}
                onClick={handleLike}
                disabled={likeLoading}
              >
                {isLiked ? '❤️' : '🤍'} {likeLoading ? '...' : ''}
              </button>
            </div>
          </div>
        </div>

        <div className="comments-section">
          <h3 className="comments-title">Comments ({comments.length})</h3>
          
          {isAuthenticated ? (
            <form onSubmit={handleCommentSubmit} className="comment-form">
              <div className="form-group">
                <textarea
                  className="form-control"
                  value={newComment}
                  onChange={(e) => setNewComment(e.target.value)}
                  placeholder="Share your thoughts on this idea..."
                  rows="3"
                  required
                />
              </div>
              <button 
                type="submit" 
                className="btn btn-primary"
                disabled={commentLoading || !newComment.trim()}
              >
                {commentLoading ? 'Posting...' : 'Post Comment'}
              </button>
            </form>
          ) : (
            <div className="login-prompt">
              <p>Please <button onClick={() => navigate('/login')} className="link-btn">login</button> to comment on this idea.</p>
            </div>
          )}

          <div className="comments-list">
            {comments.length === 0 ? (
              <p className="no-comments">No comments yet. Be the first to share your thoughts!</p>
            ) : (
              comments.map((comment) => (
                <div key={comment.id} className="comment-card">
                  <div className="comment-header">
                    <span className="commenter">{comment.commenter.username}</span>
                    <span className="comment-date">
                      {new Date(comment.created_at).toLocaleDateString()}
                    </span>
                  </div>
                  <p className="comment-content">{comment.content}</p>
                </div>
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default IdeaDetail; 