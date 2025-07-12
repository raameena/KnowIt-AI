# AI Homework Helper 🤖📚

An intelligent homework assistance platform that combines AI-powered tutoring with specialized algorithms for accurate mathematical solutions. Built with a modern React frontend and Flask backend, this project provides comprehensive academic support through advanced AI classification and custom math solving capabilities.

## 🎯 Project Overview

AI Homework Helper is designed to provide comprehensive academic support through:
- **AI-Powered Classification**: Intelligent routing of queries to specialized handlers
- **Custom Algebra Solver**: Precise solutions using SymPy for mathematical equations
- **Multi-Model AI Integration**: Using both Gemini Flash and Pro models for different query types
- **Step-by-Step Explanations**: Detailed breakdowns to enhance learning
- **Subject-Specific Handling**: Tailored responses for Algebra, History, and General queries
- **Structured Responses**: Consistent API responses with final answers and explanations

## ✨ Features

### Current Features
- 🤖 **AI Classification**: Intelligent routing of queries to appropriate handlers
- 🧮 **Algebra Solver**: Custom SymPy-based solver for mathematical equations
- 📊 **Multi-Model AI**: Gemini Flash for classification, Pro for detailed responses
- 🔄 **RESTful API**: Clean backend architecture with Flask
- 🎨 **Modern UI**: React-based frontend with responsive design
- 🌐 **CORS Support**: Seamless frontend-backend communication
- 📝 **Structured Responses**: Consistent JSON format with final_answer and explanation
- 🔍 **Error Handling**: Comprehensive error handling with proper logging

### Query Categories
- **Algebra - Solve for Variable**: Specialized handling for equation solving
- **Math - Other**: General mathematical and scientific queries
- **History**: Historical facts and information
- **General**: All other types of queries

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
- **python-dotenv** - Environment variable management

### Development Tools
- **Git** - Version control
- **VS Code** - Development environment
- **npm** - Package management (frontend)
- **pip** - Package management (backend)

## 📁 Project Structure

```
AI-HW-Helper/
├── backend/
│   ├── app.py              # Flask application with AI routing
│   ├── requirements.txt    # Python dependencies
│   ├── modules/
│   │   └── algebra_solver.py  # Custom algebra solving module
│   └── venv/              # Virtual environment
├── frontend/
│   ├── public/            # Static files
│   ├── src/               # React components
│   ├── package.json       # Node.js dependencies
│   └── README.md          # Frontend documentation
└── README.md              # This file
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

For History/General queries:
```json
{
  "final_answer": "History Answer",
  "explanation": "Detailed response from the AI model..."
}
```

## 🎯 Learning Objectives

This project serves as a comprehensive learning experience covering:

- **Full-Stack Development**: React frontend + Flask backend
- **AI Integration**: Working with Google's Gemini AI models
- **Mathematical Computing**: SymPy integration for equation solving
- **API Design**: RESTful APIs with structured responses
- **Modern Web Development**: CORS, JSON handling, error management
- **Python Programming**: Flask framework, module organization
- **AI Classification**: Intelligent query routing and processing
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

### Phase 2: Enhanced Features 🚧
- [ ] PDF processing capabilities
- [ ] Citation system
- [ ] Improved UI/UX design
- [ ] Additional math subjects (Calculus, Geometry)

### Phase 3: Analytics & Advanced Features 📊
- [ ] User analytics dashboard
- [ ] Data visualization components
- [ ] Advanced search functionality
- [ ] Performance optimization

### Phase 4: Production Ready 🚀
- [ ] Comprehensive error handling and logging
- [ ] Security enhancements
- [ ] Testing suite
- [ ] Deployment configuration

## 🚀 Getting Started

### Prerequisites
- Node.js (v16 or higher)
- Python 3.8+
- Google AI API key

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
