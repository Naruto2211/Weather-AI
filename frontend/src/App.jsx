import { useState } from 'react'
import './App.css'

function App() {
  const [query, setQuery] = useState('')
  const [response, setResponse] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSearch = async () => {
    if (!query.trim()) return
    setLoading(true)
    setResponse('')

    try {
      // Use full URL since we don't have proxy setup yet
      // Ensuring backend allows CORS
      const res = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
      })

      if (!res.ok) {
        const errData = await res.json().catch(() => ({}))
        throw new Error(errData.detail || 'Network response was not ok')
      }

      const data = await res.json()
      setResponse(data.response)
    } catch (error) {
      setResponse('Error: ' + error.message)
    } finally {
      setLoading(false)
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSearch()
    }
  }

  return (
    <div className="app-container">
      <div className="card">
        <h1>Weather AI</h1>
        <div className="input-group">
          <input
            type="text"
            placeholder="Ask about the weather..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyPress={handleKeyPress}
            className="search-input"
          />
          <button
            onClick={handleSearch}
            disabled={loading}
            className="search-button"
          >
            {loading ? (
              <span className="loader"></span>
            ) : (
              'Ask'
            )}
          </button>
        </div>

        {response && (
          <div className="response-area fade-in">
            <p>{response}</p>
          </div>
        )}
      </div>
    </div>
  )
}

export default App
