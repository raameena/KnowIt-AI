import React, { useEffect, useRef, useState } from 'react';
import ReactGA from 'react-ga4';
import './App.css';

// Helper function to generate a unique ID for each chat session
const generateSessionId = () => crypto.randomUUID();

function App() {
  const [sessionId, setSessionId] = useState('');
  const [uploadedFile, setUploadedFile] = useState(null);
  const fileInputRef = useRef(null);
  
  const [prompt, setPrompt] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [chatHistory, setChatHistory] = useState([]);
  const [showMoreOptions, setShowMoreOptions] = useState(false);
  const [showClearConfirm, setShowClearConfirm] = useState(false);

  useEffect(() => {
    setSessionId(generateSessionId());
  }, []);

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (showMoreOptions && !event.target.closest('.more-options-dropdown')) {
        setShowMoreOptions(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [showMoreOptions]);

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (showClearConfirm && !event.target.closest('.popup-content')) {
        setShowClearConfirm(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [showClearConfirm]);

  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    const MAX_FILE_SIZE = 10 * 1024 * 1024; // 10 MB

    if (file.size > MAX_FILE_SIZE) {
      // Create an error message and add it to the chat
      const errorMessage = { 
        type: 'error', 
        content: `File is too large. Please upload a PDF smaller than ${MAX_FILE_SIZE / 1024 / 1024} MB.`, 
        timestamp: new Date() 
      };
      setChatHistory(prev => [...prev, errorMessage]);

      // Stop the function here
      return; 
    }

    setIsLoading(true);
    setUploadedFile(file);

    const formData = new FormData();
    formData.append('file', file);
    formData.append('sessionId', sessionId);

    try {
      const apiUrl = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5001';
      const response = await fetch(`${apiUrl}/api/upload`, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`File upload failed! status: ${response.status}`);
      }

      const data = await response.json();
      console.log('Response from /api/upload:', data);

    } catch (error) {
      const errorMessage = { type: 'error', content: error.message, timestamp: new Date() };
      setChatHistory(prev => [...prev, errorMessage]);
      setUploadedFile(null);
    } finally {
      setIsLoading(false);
      if(fileInputRef.current) {
        fileInputRef.current.value = "";
      }
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!prompt.trim()) return;

    const userMessage = { type: 'user', content: prompt, timestamp: new Date() };
    setChatHistory(prevHistory => [...prevHistory, userMessage]);

    setIsLoading(true);
    setPrompt('');

    try {
      const apiUrl = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5001';
      const response = await fetch(`${apiUrl}/api/solve`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: prompt, sessionId: sessionId }),
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

      ReactGA.event({
        category: 'AI Interaction',
        action: 'Successful_Solve',
      });

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

  // --- THIS IS THE UPDATED FUNCTION ---
  const clearHistory = async () => {
    // Check if there is anything to clear OR if a file was uploaded,
    // as we still need to clear the backend session.
    if (chatHistory.length === 0 && !uploadedFile) return;

    try {
      const apiUrl = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5001';
      // Call the backend endpoint to delete the session data from the database
      const response = await fetch(`${apiUrl}/api/clear_session`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ sessionId: sessionId }),
      });

      if (!response.ok) {
        throw new Error('Failed to clear session on the server.');
      }

      console.log('Session cleared on server.');

    } catch (error) {
      console.error("Error clearing session:", error);
      // Optionally show an error in the chat
      const errorMessage = { 
        type: 'error', 
        content: 'Could not clear the server session. Please try again.', 
        timestamp: new Date() 
      };
      setChatHistory(prev => [...prev, errorMessage]);
    } finally {
      // This part runs regardless of the API call's success
      // to ensure the frontend UI is always cleared.
      setChatHistory([]);
      setUploadedFile(null);
      setSessionId(generateSessionId());
    }
  };

  const formatTimestamp = (timestamp) => {
    return new Date(timestamp).toLocaleTimeString([], { 
      hour: '2-digit', 
      minute: '2-digit' 
    });
  };

  return (
    <div className="App">
      <div className="app-container">
        <header className="app-header">
          <div className="header-content">
            <div className="logo">
              <h1 className="wave-text">
                {'KnowIt AI'.split('').map((char, index) => (
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
            <p className="subtitle">Powered by Wolfram Alpha API and Gemini API</p>
          </div>
        </header>

        <main className="main-content">
          <div className={`chat-container ${uploadedFile ? 'has-document' : ''}`}>
            <div className="chat-history">
              {chatHistory.length === 0 && (
                <div className="welcome-message">
                  {uploadedFile ? (
                    <>
                      <h3>📄 Document Analysis Ready!</h3>
                      <p>Your document has been uploaded successfully. Ask me anything about it!</p>
                      <div className="example-prompts">
                        <p>Try asking about your document:</p>
                        <ul>
                          <li>"Summarize the main points"</li>
                          <li>"What are the key qualifications mentioned?"</li>
                          <li>"Extract all contact information"</li>
                          <li>"What experience is highlighted?"</li>
                        </ul>
                      </div>
                    </>
                  ) : (
                    <>
                      <h3>Welcome to KnowIt AI!</h3>
                      <p> All your questions will be answered here :)</p>
                      <div className="example-prompts">
                        <p>Try asking:</p>
                        <ul>
                          <li>Math: "Solve for x: 2x + 5 = 13"</li>
                          <li>Math: "Simplify: 3x² + 6x - 5"</li>
                          <li>Other: "What is the capital of France"</li>
                        </ul>
                      </div>
                    </>
                  )}
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

                    {message.type === 'system' && (
                        <div className="system-message">
                            <span>{message.content}</span>
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
            
            <div className="input-container">
              <form onSubmit={handleSubmit} className="input-form">
                <div className="input-wrapper">
                  <div className="more-options-dropdown">
                    <button
                      type="button"
                      className="more-options-button"
                      onClick={() => setShowMoreOptions(!showMoreOptions)}
                      disabled={isLoading}
                      title="More Options"
                    >
                      +
                    </button>
                    
                    {showMoreOptions && (
                      <div className="dropdown-menu">
                        <input
                          type="file"
                          ref={fileInputRef}
                          onChange={handleFileChange}
                          style={{ display: 'none' }}
                          accept=".pdf"
                        />
                        
                        <button
                          type="button"
                          className="dropdown-item"
                          onClick={() => {
                            fileInputRef.current.click();
                          }}
                          disabled={isLoading}
                        >
                          📎 Attach PDF
                        </button>
                        
                        <button 
                          onClick={() => {
                            console.log('Clear chat button clicked');
                            setShowClearConfirm(true);
                            setShowMoreOptions(false);
                          }}
                          className="dropdown-item clear-option"
                        >
                          🗑️ Clear Chat
                        </button>
                      </div>
                    )}
                  </div>
                  
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
                    placeholder={uploadedFile ? "Ask a question about your document..." : "Ask me anything..."}
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
              {uploadedFile && (
                <div className="file-indicator">
                  <p>Active Document: {uploadedFile.name}</p>
                </div>
              )}
            </div>
          </div>
        </main>
      </div>
      
      {showClearConfirm && (
        <div className="popup-overlay">
          <div className="popup-content">
            <h3>Clear Chat History?</h3>
            <p>Are you sure you want to clear all chat messages? This action cannot be undone.</p>
            <div className="popup-buttons">
              <button 
                onClick={() => {
                  clearHistory();
                  setShowClearConfirm(false);
                }}
                className="popup-button confirm-button"
              >
                Yes, Clear Chat
              </button>
              <button 
                onClick={() => setShowClearConfirm(false)}
                className="popup-button cancel-button"
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
