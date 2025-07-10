import React, { useState } from 'react';
import './App.css'; // We'll add our styles to this file

// The component is now named 'App' to match the filename.
function App() {
  // 1. STATE MANAGEMENT with useState
  // Stores the text from the textarea
  const [prompt, setPrompt] = useState('');
  
  // Stores the final answer from the API
  const [result, setResult] = useState(null);
  
  // Stores whether we are currently waiting for the API response
  const [isLoading, setIsLoading] = useState(false);

  // 2. ASYNCHRONOUS API CALL LOGIC
  const handleSubmit = async (event) => {
    // Prevents the browser from reloading the page
    event.preventDefault();

    // Start the loading state and clear old results
    setIsLoading(true);
    setResult(null);

    try {
      // The full URL to your running Flask backend endpoint
      const response = await fetch('http://127.0.0.1:5000/api/solve', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        // Send the user's prompt from our state in the request body
        body: JSON.stringify({ prompt: prompt }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log('Data received from backend:', data); // For testing the connection
      setResult(data);

    } catch (error) {
      setResult({ error: error.message });
    } finally {
      // No matter what happens, stop the loading state
      setIsLoading(false);
    }
  };

  // 3. THE UI BLUEPRINT (RENDERED JSX)
  return (
    <div className="App">
      <div className="ai-container">
        <h1>My AI Homework Helper</h1>
        
        <form onSubmit={handleSubmit}>
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Enter your math problem here..."
          />
          
          <button type="submit" disabled={isLoading}>
            {isLoading ? 'Thinking...' : 'Solve'}
          </button>
        </form>

        <div className="results-area">
          {/* Show a loading message while waiting */}
          {isLoading && <p>Loading, please wait...</p>}
          
          {/* Show an error message if the API call fails */}
          {result && result.error && <p className="error-message">Error: {result.error}</p>}
          
          {/* For now, this will display the test message from your backend.
              We will change this later to show the real math solution. */}
          {result && result.message && (
            <div>
              <h3>Response from Server:</h3>
              <p>{result.message}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

// Make sure the export name is 'App'
export default App;