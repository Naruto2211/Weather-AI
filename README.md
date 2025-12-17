# Weather AI App 🌤️

A distinctively designed, minimal, and simple web application that allows users to ask about the weather in any city. The backend uses an LLM (via LangGraph agents) to understand natural language queries and fetches real-time weather data using a custom tool.

## Features

- **Natural Language Query**: Ask "What's the weather in Tokyo?" or "Is it raining in London?".
- **AI Agent**: Backend powered by LangGraph and OpenRouter (GPT-3.5) to intelligently parse intent.
- **Real-time Data**: Fetches accurate weather data from Open-Meteo API.
- **Modern UI**: Built with React and Vite, featuring a glassmorphism design and smooth animations.

## Tech Stack

- **Frontend**: React, Vite, CSS (Glassmorphism)
- **Backend**: FastAPI, LangChain / LangGraph, Python
- **AI/LLM**: OpenRouter (OpenAI models), Open-Meteo (Weather Data)

## Prerequisites

- **Python 3.10+**
- **Node.js** & **npm**
- **OpenRouter API Key** (Get one at [openrouter.ai](https://openrouter.ai/))

## Installation & Setup

### 1. Backend Setup

 Navigate to the backend directory:
 ```bash
 cd backend
 ```

 Install dependencies (ensure you have the necessary packages):
 ```bash
 pip install fastapi uvicorn langchain langchain_openai langchain_community httpx python-dotenv
 ```

 Configure Environment Variables:
 1. Create a `.env` file in the `backend` folder.
 2. Add your OpenRouter API key:
    ```
    OPENROUTER_API_KEY=sk-or-v1-your-key-here
    ```

 Start the Backend Server:
 ```bash
 python main.py
 ```
 The backend will run on `http://localhost:8000`.

### 2. Frontend Setup

 Navigate to the frontend directory:
 ```bash
 cd frontend
 ```

 Install dependencies:
 ```bash
 npm install
 ```

 Start the Development Server:
 ```bash
 npm run dev
 ```
 The frontend will run on `http://localhost:5173`.

## Usage

1. Open your browser and go to `http://localhost:5173`.
2. Type a question like **"What is the temperature in New York?"** in the input box.
3. Click the **Ask** button.
4. The AI will process your request, check the weather tool, and display the answer.

## Project Structure

```
project x/
├── backend/
│   ├── main.py        # FastAPI entry point
│   ├── agent.py       # LangGraph agent & Weather Tool definition
│   ├── .env           # Environment variables (Ignored by Git)
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── App.jsx    # Main React UI component
    │   └── App.css    # Styling and Animations
    └── ...
```

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

Distributed under the MIT License.
