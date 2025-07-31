import React, { useState } from 'react';
import ReactGA from 'react-ga4';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [chatHistory, setChatHistory] = useState([]);

  // =================================================================
  // THIS IS THE UPDATED SECTION
  // =================================================================
  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!prompt.trim()) return;

    const userMessage = { type: 'user', content: prompt, timestamp: new Date() };
    setChatHistory(prevHistory => [...prevHistory, userMessage]);

    setIsLoading(true);
    setPrompt('');

    try {
      const apiUrl = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';
      const response = await fetch(`${apiUrl}/api/solve`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: prompt }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log('Data received from backend:', data);

      const aiMessage = { 
        type: 'ai', 
        content: data, 
        timestamp: new Date() 
      };
      
      setChatHistory(prevHistory => [...prevHistory, aiMessage]);

      // --- THIS IS THE NEW LINE ---
      // It runs only after a successful response is received and added to history.
      ReactGA.event({
        category: 'AI Interaction',
        action: 'Successful_Solve',
      });
      // --------------------------

    } catch (error) {
      const errorMessage = { 
        type: 'error', 
        content: error.message, 
        timestamp: new Date() 
      };
      setChatHistory(prevHistory => [...prevHistory, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };
  // =================================================================
  // END OF UPDATED SECTION
  // =================================================================

  const clearHistory = () => {
    setChatHistory([]);
  };

  const formatTimestamp = (timestamp) => {
    return new Date(timestamp).toLocaleTimeString([], { 
      hour: '2-digit', 
      minute: '2-digit' 
    });
  };

  // Your entire JSX return statement below this line is perfect and remains unchanged.
  return (
    <div className="App">
      <div className="app-container">
        {/* Header */}
        <header className="app-header">
          <div className="header-content">
            <div className="logo">
              <h1 className="wave-text">
                {'AI Homework Solver'.split('').map((char, index) => (
                  <span 
                    key={index} 
                    className="wave-letter"
                    style={{ animationDelay: `${index * 0.08}s` }}
                  >
                    {char === ' ' ? '\u00A0' : char}
                  </span>
                ))}
              </h1>
            </div>
            <p className="subtitle">Premium Math Help ⭐️</p>
          </div>
        </header>

        {/* Main Content */}
        <main className="main-content">
          <div className="chat-container">
            {/* Chat History */}
            <div className="chat-history">
              {chatHistory.length === 0 && (
                <div className="welcome-message">
                  <h3>Welcome to AI Homework Solver!</h3>
                  <p>Ask me any math problem, and I'll help you solve it step by step.</p>
                  <div className="example-prompts">
                    <p>Try asking:</p>
                    <ul>
                      <li>"Solve for x: 2x + 5 = 13"</li>
                      <li>"Simplify: 3x² + 6x - 5"</li>
                      <li>"What is the derivative of x³?"</li>
                    </ul>
                  </div>
                </div>
              )}

              {chatHistory.map((message, index) => (
                <div key={index} className={`message ${message.type}`}>
                  <div className="message-content">
                    {message.type === 'user' && (
                      <div className="user-message">
                        <div className="message-avatar">👤</div>
                        <div className="message-text">{message.content}</div>
                      </div>
                    )}
                    
                    {message.type === 'ai' && (
                      <div className="ai-message">
                        <div className="message-avatar">🤖</div>
                        <div className="message-text">
                          {message.content.final_answer && (
                            <div className="answer-section">
                              <h4>Answer:</h4>
                              <div className="final-answer">{message.content.final_answer}</div>
                            </div>
                          )}
                          {message.content.explanation && (
                            <div className="explanation-section">
                              <h4>Explanation:</h4>
                              <div className="explanation">{message.content.explanation}</div>
                            </div>
                          )}
                        </div>
                      </div>
                    )}

                    {message.type === 'error' && (
                      <div className="error-message">
                        <div className="message-avatar">⚠️</div>
                        <div className="message-text">Error: {message.content}</div>
                      </div>
                    )}
                  </div>
                  <div className="message-timestamp">
                    {formatTimestamp(message.timestamp)}
                  </div>
                </div>
              ))}

              {isLoading && (
                <div className="message ai">
                  <div className="message-content">
                    <div className="ai-message">
                      <div className="message-avatar">🤖</div>
                      <div className="message-text">
                        <div className="loading-indicator">
                          <div className="typing-dots">
                            <span></span>
                            <span></span>
                            <span></span>
                          </div>
                          <p>Thinking...</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              )}
            </div>

            {/* Input Form */}
            <div className="input-container">
              <form onSubmit={handleSubmit} className="input-form">
                <div className="input-wrapper">
                            <textarea
                    value={prompt}
                    onChange={(e) => setPrompt(e.target.value)}
                    onKeyDown={(e) => {
                      if (e.key === 'Enter' && !e.shiftKey) {
                        e.preventDefault();
                        if (prompt.trim() && !isLoading) {
                          handleSubmit(e);
                        }
                      }
                    }}
                    placeholder="Ask me any math problem..."
                    disabled={isLoading}
                    className="chat-input"
                  />
                  <button 
                    type="submit" 
                    disabled={isLoading || !prompt.trim()}
                    className="send-button"
                  >
                    {isLoading ? (
                      <div className="button-loading">
                        <div className="spinner"></div>
                      </div>
                    ) : (
                      <span>Send</span>
                    )}
          </button>
                </div>
        </form>
            </div>
          </div>

          {/* Sidebar */}
          <div className="sidebar">
            <div className="sidebar-section">
              <h3>Quick Actions</h3>
              <button 
                onClick={clearHistory} 
                className="clear-button"
                disabled={chatHistory.length === 0}
              >
                Clear Chat
              </button>
            </div>

            <div className="sidebar-section">
              <h3>Features</h3>
              <ul className="features-list">
                <li>✅ Step-by-step explanations</li>
                <li>✅ Algebraic problem solving</li>
                <li>✅ Mathematical simplification</li>
                <li>✅ Real-time AI assistance</li>
              </ul>
            </div>

            <div className="sidebar-section">
              <h3>Tips</h3>
              <ul className="tips-list">
                <li>Be specific with your questions</li>
                <li>Include all relevant information</li>
                <li>Ask for step-by-step solutions</li>
                <li>Use clear mathematical notation</li>
              </ul>
            </div>
        </div>
        </main>
      </div>
    </div>
  );
}

export default App;