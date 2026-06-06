# AI Career Copilot

An AI-powered Career Intelligence Platform that helps students, job seekers, and professionals optimize their resumes, analyze job descriptions, identify skill gaps, prepare for interviews, and generate personalized career growth plans.

## Project Vision

Most resume analyzers only provide an ATS score.

AI Career Copilot goes beyond resume analysis by acting as a personalized career assistant throughout the entire job application journey.

The platform helps users:

* Analyze and improve resumes
* Match resumes against job descriptions
* Identify missing skills
* Build personalized learning roadmaps
* Prepare for interviews
* Generate application assets such as cover letters and outreach messages
* Track career progress over time



## Features

### Resume Intelligence

* PDF Resume Upload
* Resume Parsing
* Resume Section Detection
* Resume Strengths Analysis
* Resume Weakness Analysis
* Resume Improvement Suggestions

### ATS Optimization

* ATS Score Generation
* Keyword Analysis
* Resume Quality Metrics
* Resume Readability Insights

### Job Description Intelligence

* Job Description Parsing
* Required Skill Extraction
* Resume vs Job Match Analysis
* Missing Skill Detection
* Match Percentage Calculation

### Skill Gap Analysis

* Technical Skill Gap Detection
* Tool and Framework Analysis
* Skill Importance Categorization
* Career Readiness Assessment

### AI Career Coach

* Gemini-Powered Feedback
* Personalized Recommendations
* Career Improvement Guidance
* Role-Based Resume Optimization

### Learning Roadmaps

* 30-Day Learning Plan
* 60-Day Learning Plan
* 90-Day Learning Plan
* Project Recommendations
* Resource Recommendations

### Interview Preparation

* Technical Questions
* Behavioral Questions
* Resume-Based Questions
* Project-Based Questions
* Difficulty Levels:

  * Easy
  * Medium
  * Hard

### Application Assistant

* Cover Letter Generation
* LinkedIn Outreach Messages
* Referral Request Messages
* Cold Email Templates

### Career Dashboard

* ATS Score
* Skill Match Score
* Missing Skills
* Resume Insights
* Learning Roadmap Tracking
* Application Asset Management



## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-learn

### Natural Language Processing

* spaCy

### PDF Processing

* PyPDF

### Visualization

* Matplotlib

### AI Integration

* Google Gemini API

### Database

* SQLite

### Testing

* Pytest

### Environment Management

* Python Dotenv



## Project Architecture

```text
AI-Career-Copilot/
│
├── app/
│   ├── pages/
│   ├── components/
│   ├── services/
│   ├── database/
│   ├── prompts/
│   ├── models/
│   └── utils/
│
├── data/
├── tests/
├── docs/
├── assets/
│
├── main.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```




## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```



## Installation

```bash
git clone https://github.com/your-username/AI-Career-Copilot.git

cd AI-Career-Copilot

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Run the application:

```bash
streamlit run main.py
```



## Future Expansion

The architecture is intentionally designed to support future enhancements:

* Job Scraping
* Multi-Agent Career Assistants
* CrewAI Integration
* RAG-Based Job Search
* Career Recommendation Engine
* Agentic Application Workflows

These features are not currently implemented but are considered during architectural design.



## License

This project is intended for educational, research, and portfolio purposes.



## Author

Akshit Joshi

AI Career Copilot is being developed as a production-quality portfolio project demonstrating software engineering, NLP, machine learning, and generative AI integration.
