"""
Configuration file for the Portfolio Website.
Contains static data, profile information, and settings.
"""

PROFILE = {
    "name": "Syed Shahid Nazeer", 
    "title": "AI Generalist",
    "location": "Bengaluru, India",
    "email": "shahidnazeerds@gmail.com",
    "socials": {
        "LinkedIn": "https://www.linkedin.com/in/shahidnazeersyed/", 
        "GitHub": "https://github.com/Syedshahidnazeer", 
        "Twitter": "#"
    },
    "tagline": "Visualizing Intelligence.",
    "intro_text": "Driving innovation with Generative AI and scalable Intelligent Systems."
}

SKILLS = [
    {"name": "Generative AI", "val": 95}, 
    {"name": "LLMs & NLP", "val": 95},
    {"name": "RAG Systems", "val": 90}, 
    {"name": "Prompt Eng.", "val": 90},
    {"name": "Python", "val": 85}, 
    {"name": "MLOps", "val": 80},
    {"name": "Data Science", "val": 85},
    {"name": "SQL/NoSQL", "val": 75}
]

PROJECTS = [
    {
        "title": "Oil Price Prediction",
        "tags": ["Python", "Time-Series", "AI"],
        "gradient": "linear-gradient(45deg, #FF9F1C, #FFD166)"
    },
    {
        "title": "Fake News NLP",
        "tags": ["BERT", "Sentiment Analysis"],
        "gradient": "linear-gradient(45deg, #2EC4B6, #CBF3F0)"
    },
    {
        "title": "App Rating Predictor",
        "tags": ["sklearn", "Regression", "Data"],
        "gradient": "linear-gradient(45deg, #FF5400, #FF9F1C)"
    },
    {
        "title": "RAG QA System",
        "tags": ["Haystack", "LangChain", "LLM"],
        "gradient": "linear-gradient(45deg, #9D4EDD, #C77DFF)"
    }
]

STATS = {
    "hours": "2+ Yrs",
    "projects": "3+ Major",
    "status": "Open to Work"
}
