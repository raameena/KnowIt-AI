# AI Homework Helper 🤖📚

An intelligent homework assistance platform that combines AI-powered tutoring with custom algorithms for accurate mathematical solutions. Built with a modern React frontend and Flask backend, this project demonstrates full-stack development, API integration, and data science concepts.

## 🎯 Project Overview

AI Homework Helper is designed to provide comprehensive academic support through:
- **AI-Powered Tutoring**: Leveraging Google's Gemini AI for intelligent responses
- **Custom Math Algorithms**: Precise solutions for calculus, linear algebra, and other mathematical subjects
- **Step-by-Step Explanations**: Detailed breakdowns to enhance learning
- **PDF Document Processing**: Extract and analyze content from uploaded documents
- **Citation Management**: Proper quote extraction with academic citations
- **Analytics Dashboard**: User progress tracking and subject analytics

## ✨ Features

### Current Features
- 🤖 **AI Integration**: Google Gemini 1.5 Pro for intelligent responses
- 📊 **Subject-Specific Handling**: Tailored responses for different academic subjects
- 🔄 **RESTful API**: Clean backend architecture with Flask
- 🎨 **Modern UI**: React-based frontend with responsive design
- 🌐 **CORS Support**: Seamless frontend-backend communication

### Planned Features
- 📄 **PDF Processing**: Extract and analyze document content
- 📝 **Citation System**: Quote extraction with proper academic citations
- 📈 **Analytics Dashboard**: User progress and subject usage statistics
- 🧮 **Custom Math Algorithms**: Precise solutions for calculus and linear algebra
- 📊 **Data Visualization**: Interactive charts and progress tracking
- 🔍 **Advanced Search**: Smart content filtering and organization

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

### Development Tools
- **Git** - Version control
- **VS Code** - Development environment
- **npm** - Package management (frontend)
- **pip** - Package management (backend)

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

## 📁 Project Structure

```
AI-HW-Helper/
├── backend/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   ├── modules/           # Custom modules
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
Processes homework questions and returns AI-generated responses.

**Request Body:**
```json
{
  "prompt": "Solve the quadratic equation x² + 5x + 6 = 0",
  "subject": "math"
}
```

**Response:**
```json
{
  "message": "AI-generated solution with step-by-step explanation"
}
```

## 🎯 Learning Objectives

This project serves as a comprehensive learning experience covering:

- **Full-Stack Development**: React frontend + Flask backend
- **API Integration**: Working with external AI services
- **Modern Web Development**: RESTful APIs, CORS, JSON handling
- **Python Programming**: Flask framework, environment management
- **Data Science Concepts**: Analytics, visualization, algorithm development
- **UI/UX Design**: Creating intuitive and beautiful user interfaces
- **Version Control**: Git workflow and project management

## 🚧 Development Roadmap

### Phase 1: Core Functionality ✅
- [x] Basic Flask backend setup
- [x] React frontend structure
- [x] AI integration with Gemini
- [x] Basic API communication

### Phase 2: Enhanced Features 🚧
- [ ] Custom math algorithms implementation
- [ ] PDF processing capabilities
- [ ] Citation system
- [ ] Improved UI/UX design

### Phase 3: Analytics & Advanced Features 📊
- [ ] User analytics dashboard
- [ ] Data visualization components
- [ ] Advanced search functionality
- [ ] Performance optimization

### Phase 4: Production Ready 🚀
- [ ] Error handling and logging
- [ ] Security enhancements
- [ ] Testing suite
- [ ] Deployment configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request