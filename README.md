# Resume_Analyzer
Resume Magnifier is an AI-powered web application designed to help users evaluate how well their resume aligns with a specific job description. Built using Streamlit and Python, this tool simplifies the resume screening process by providing an instant match score and clear visual feedback.

Users can easily upload their resume in PDF or DOCX format and paste a job description directly into the app. The system then extracts the textual content, cleans it by removing unnecessary words and symbols, and converts it into numerical form using natural language processing (NLP) techniques. By applying CountVectorizer and cosine similarity, the app calculates how closely the resume matches the given job description.

The result is presented as a match percentage, visually represented through a bar chart for easy interpretation. This helps job seekers quickly identify how relevant their resume is and where improvements may be needed to increase their chances of selection.
