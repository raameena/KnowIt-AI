# AI Homework Helper 🤖📚

An intelligent homework assistance platform that combines AI-powered tutoring with specialized algorithms for accurate mathematical solutions. Built with a modern React frontend and Flask backend, this project provides comprehensive academic support through advanced AI classification and custom math solving capabilities.

## 🎯 Project Overview

AI Homework Helper is designed to provide comprehensive academic support through:
- **AI-Powered Classification**: Intelligent routing of queries to specialized handlers
- **Custom Algebra Solver**: Precise solutions using SymPy for mathematical equations
- **Wolfram Alpha Integration**: Advanced mathematical computations and scientific queries
- **Multi-Model AI Integration**: Using both Gemini Flash and Pro models for different query types
- **Step-by-Step Explanations**: Detailed breakdowns to enhance learning
- **Subject-Specific Handling**: Tailored responses for Algebra, History, and General queries
- **Modular Architecture**: Clean, maintainable codebase with separated concerns

## ✨ Features

### Current Features
- 🤖 **AI Classification**: Intelligent routing of queries to appropriate handlers
- 🧮 **Algebra Solver**: Custom SymPy-based solver for mathematical equations
- 🔬 **Wolfram Alpha Integration**: Advanced mathematical and scientific computations
- 📊 **Multi-Model AI**: Gemini Flash for classification, Pro for detailed responses
- 🔄 **RESTful API**: Clean backend architecture with Flask
- 🎨 **Modern UI**: React-based frontend with responsive design
- 🌐 **CORS Support**: Seamless frontend-backend communication
- 📝 **Structured Responses**: Consistent JSON format with final_answer and explanation
- 🔍 **Error Handling**: Comprehensive error handling with proper logging
- 🏗️ **Modular Design**: Separated concerns with dedicated modules for each functionality

### Query Categories
- **Algebra - Solve for Variable**: Specialized handling for equation solving with SymPy
- **Math - Other**: General mathematical and scientific queries using Wolfram Alpha
- **History**: Historical facts and information using Gemini Pro
- **General**: All other types of queries using Gemini Flash

## 🛠️ Tech Stack

### Frontend
- **React 19.1.0** - Modern UI framework
- **CSS3** - Styling and responsive design
- **JavaScript ES6+** - Modern JavaScript features

### Backend
- **Python 3.x** - Core programming language
- **Flask 3.1.1** - Lightweight web framework
- **Google Generative AI 0.8.5** - AI model integration
- **Flask-CORS 6.0.1** - Cross-origin resource sharing
- **SymPy 1.14.0** - Mathematical equation solving
- **Wolfram Alpha API** - Advanced mathematical computations
- **python-dotenv** - Environment variable management
- **requests** - HTTP library for API calls

### Development Tools
- **Git** - Version control
- **VS Code** - Development environment
- **npm** - Package management (frontend)
- **pip** - Package management (backend)

## 📁 Project Structure

```
AI-HW-Helper/
├── backend/
│   ├── app.py                    # Main Flask application with routing logic
│   ├── requirements.txt          # Python dependencies
│   ├── modules/
│   │   ├── algebra_solver.py    # Custom algebra solving with SymPy
│   │   ├── wolfram_api_solver.py # Wolfram Alpha API integration
│   │   ├── tutor.py             # AI tutoring and explanation generation
│   │   ├── query_classifier.py  # AI-powered query classification
│   │   ├── query_translator.py  # Natural language to Wolfram Alpha translation
│   │   ├── history_handler.py   # History-specific query processing
│   │   └── general_handler.py   # General query processing
│   └── venv/                    # Virtual environment
├── frontend/
│   ├── public/                  # Static files
│   ├── src/                     # React components
│   ├── package.json             # Node.js dependencies
│   └── README.md                # Frontend documentation
└── README.md                    # This file
```

## 🔧 API Endpoints

### POST `/api/solve`
Processes homework questions and returns AI-generated responses with structured data.

**Request Body:**
```json
{
  "prompt": "solve for x in 2x + 5 = 15",
  "subject": "math"
}
```

**Response Examples:**

For Algebra problems:
```json
{
  "final_answer": "{5}",
  "explanation": "Of course! The answer is x = 5. Here's how we solve it step by step..."
}
```

For Math-Other problems (Wolfram Alpha):
```json
{
  "final_answer": "6x + 2",
  "explanation": "Of course! The derivative is 6x + 2. Here's how we get there step-by-step..."
}
```

For History/General queries:
```json
{
  "final_answer": "History Answer",
  "explanation": "Detailed response from the AI model..."
}
```

## 🏗️ Architecture Overview

### Backend Modules
- **`query_classifier.py`**: Uses Gemini Flash to classify queries into categories
- **`query_translator.py`**: Translates natural language to Wolfram Alpha format
- **`algebra_solver.py`**: Handles equation solving using SymPy
- **`wolfram_api_solver.py`**: Integrates with Wolfram Alpha API for advanced math
- **`tutor.py`**: Generates step-by-step explanations using Gemini Pro
- **`history_handler.py`**: Processes history-specific queries
- **`general_handler.py`**: Handles general queries

### Query Flow
1. **Classification**: Query is classified using AI
2. **Routing**: Query is routed to appropriate handler
3. **Processing**: Specialized processing based on category
4. **Response**: Structured response with answer and explanation

## 🎯 Learning Objectives

This project serves as a comprehensive learning experience covering:

- **Full-Stack Development**: React frontend + Flask backend
- **AI Integration**: Working with Google's Gemini AI models and Wolfram Alpha
- **Mathematical Computing**: SymPy and Wolfram Alpha integration
- **API Design**: RESTful APIs with structured responses
- **Modern Web Development**: CORS, JSON handling, error management
- **Python Programming**: Flask framework, modular architecture
- **AI Classification**: Intelligent query routing and processing
- **External API Integration**: Wolfram Alpha API with proper error handling
- **Code Organization**: Modular design with separated concerns
- **Version Control**: Git workflow and project management

## 🚧 Development Roadmap

### Phase 1: Core Functionality ✅
- [x] Basic Flask backend setup
- [x] React frontend structure
- [x] AI integration with Gemini
- [x] Basic API communication
- [x] Query classification system
- [x] Algebra solver implementation
- [x] Multi-model AI integration
- [x] Wolfram Alpha integration
- [x] Modular architecture refactoring

### Phase 2: Enhanced Features 🚧
- [ ] PDF processing capabilities
- [ ] Citation system
- [ ] Improved UI/UX design
- [ ] Additional math subjects (Calculus, Geometry)
- [ ] User authentication system

### Phase 3: Analytics & Advanced Features 📊
- [ ] User analytics dashboard
- [ ] Data visualization components
- [ ] Advanced search functionality
- [ ] Performance optimization
- [ ] Caching system

### Phase 4: Production Ready 🚀
- [ ] Comprehensive error handling and logging
- [ ] Security enhancements
- [ ] Testing suite
- [ ] Deployment configuration
- [ ] Documentation improvements

## 🚀 Getting Started

### Prerequisites
- Node.js (v16 or higher)
- Python 3.8+
- Google AI API key
- Wolfram Alpha API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-hw-helper.git
   cd ai-hw-helper
   ```

2. **Set up the backend**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   # Create .env file in backend directory
   echo "GOOGLE_API_KEY=your_api_key_here" > .env
   echo "WOLFRAM_APP_ID=your_wolfram_api_key_here" >> .env
   ```

4. **Set up the frontend**
   ```bash
   cd ../frontend
   npm install
   ```

### Running the Application

1. **Start the backend server**
   ```bash
   cd backend
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   python app.py
   ```
   The backend will run on `http://localhost:5000`

2. **Start the frontend development server**
   ```bash
   cd frontend
   npm start
   ```
   The frontend will run on `http://localhost:3000`

3. **Access the application**
   Open your browser and navigate to `http://localhost:3000`

## 🔍 Usage Examples

### Algebra Problems
- "solve for x in 2x + 5 = 15"
- "what is y if 3y - 12 = 0"
- "find the value of z in 4z + 8 = 20"

### Math-Other Problems (Wolfram Alpha)
- "find the derivative of f(x) = x^2 + 2x"
- "what is the integral of 5x dx"
- "calculate the slope of y = 4x - 8"
- "what is the limit of 1/x as x approaches 0"

### History Questions
- "who was the first president of the united states?"
- "what happened in 1776?"
- "who discovered electricity?"

### General Queries
- "what is the capital of France?"
- "how does photosynthesis work?"
- "what is the speed of light?"

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔄 Recent Updates

### Latest Refactoring (Current)
- **Modular Architecture**: Separated concerns into dedicated modules
- **Wolfram Alpha Integration**: Added advanced mathematical computations
- **Improved Error Handling**: Better exception handling and logging
- **Code Organization**: Cleaner, more maintainable codebase
- **Enhanced Query Processing**: More sophisticated routing and handling

### Key Improvements
- Reduced main app.py from 164 lines to ~80 lines
- Added timeout handling for API calls
- Implemented proper exception chaining
- Created specialized modules for each query type
- Enhanced logging and error reporting
