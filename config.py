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

EDUCATION = [
    {
        "degree": "Bachelor of Technology (B.Tech)",
        "field": "Computer Science & Engineering",
        "institution": "Annamacharya Institute Of Technology & Sciences, Kadapa",
        "duration": "2018 - 2022",
        "grade": "67.98%"
    },
    {
        "degree": "Higher Secondary Education (12th)",
        "field": "PCM (Physics, Chemistry, Maths)",
        "institution": "Sri Chaitanya Junior College, Kadapa",
        "duration": "Completed 2018",
        "grade": "74.8%"
    },
    {
        "degree": "Secondary Education (10th)",
        "field": "General",
        "institution": "Nagarjuna Model School, Kadapa",
        "duration": "Completed 2016",
        "grade": "8.8 GPA"
    }
]

CERTIFICATIONS = [
    {
        "title": "Data Science Certification",
        "issuer": "Excelr",
        "date": "Jan 2023",
        "desc": "Machine Learning, Python, Data Viz"
    },
    {
        "title": "Business Analytics",
        "issuer": "Internshala",
        "date": "Nov 2022",
        "desc": "Data Analysis, Statistical Models"
    },
    {
        "title": "AWS Cloud Practitioner",
        "issuer": "Amazon Web Services",
        "date": "Nov 2022",
        "desc": "Cloud Fundamentals & Services"
    },
    {
        "title": "Google Data Analytics",
        "issuer": "Google",
        "date": "Nov 2022",
        "desc": "Data Analysis Professional Cert"
    }
]

STATS = {
    "hours": "2+ Yrs",
    "projects": "3+ Major",
    "status": "Open to Work"
}
