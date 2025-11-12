import streamlit as st
import pandas as pd
import PyPDF2
from nltk.corpus import stopwords
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt')
nltk.download('stopwords')
import matplotlib.pyplot as plt

st.markdown(
    """
    <style>
    .stApp {
    
        background-color: #f0f8ff;  /* light blue background */
        
    }
    div.stButton > button:first-child {
        background-color: #0077B6; /* Tomato red */
        color: white;
        font-weight: bold;
        border-radius: 10px;
    }
    div.stButton > button:hover {
        background-color: #ff4500;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def web_page():
    
    st.title("Resume Magnifier (•⌂•)")
    st.write("Is your resume good enough? Let's find out!")
    get_started_clicked=st.button("Get Started")
    if get_started_clicked:
        
        st.markdown(f"##### Welcome to Resume Magnifier! This application helps you analyze and improve your resume using AI technology. Upload your resume, and let the AI provide insights and suggestions to make it stand out to potential employers.")
        st.subheader("To get started, navigate to the 'Upload Resume' section in the sidebar.")
    
    resume=st.sidebar.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
    job_description=st.sidebar.text_area("Paste the job description here")
    
    analyze_button=st.sidebar.button("Analyze Resume")
    if resume:
        st.success("WOOHH! Resume uploaded successfully!")
        resume_uploaded=True
        uploaded_file = resume
        if uploaded_file.name.endswith(".pdf"):
            import PyPDF2

            reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        
                st.subheader('☻Resume Preview:')
                st.markdown(
                f"""
                <div style='background-color:#f0f2f6; padding:15px; border-radius:8px; border:2px solid #5cb3fd; white-space: pre-wrap;
                '>{text}</div>
        
                """ , unsafe_allow_html=True
                )
                
            if analyze_button:
                st.subheader('☻Job Description Preview:')
                st.markdown(
                f"""
                <div style='background-color:#f0f2f6; padding:15px; border-radius:8px; border:2px solid #5cb3fd; white-space: pre-wrap;
                '>{job_description}</div>
        
                """ , unsafe_allow_html=True
                )
        elif uploaded_file.name.endswith(".docx"):
            from docx import Document
            doc = Document(uploaded_file)
            text = "\n".join([para.text for para in doc.paragraphs])
        #tokenization of resume and job description
        word_tokenize(text)
        print(word_tokenize(text))
        word_tokenize(job_description)
        #Preprocessing of resume text    
        tokens=[w for w in text.lower().split() if w.isalpha()]
        no_stops=[t for t in tokens if t not in stopwords.words('english')]    
        no_special_characters=re.sub(r'[^a-zA-Z\s]','', ' '.join(no_stops))
        cleaned_text=re.sub(r'\s+',' ', no_special_characters).strip()

        #Preprocessing of job description text    
        tokens_job=[w for w in job_description.lower().split() if w.isalpha()]
        no_stops_job=[t for t in tokens_job if t not in stopwords.words('english')]    
        no_special_characters_job=re.sub(r'[^^a-zA-Z0-9+.#\s-]','', ' '.join(no_stops_job))
        cleaned_text_job=re.sub(r'\s+',' ', no_special_characters_job).strip()

        #converting text to numerical form
        vectorizer=CountVectorizer()
        vectors=vectorizer.fit_transform([cleaned_text, cleaned_text_job])
        vector_array=vectors.toarray()
        
        #Calculating cosine similarity between resume and job description

        from sklearn.metrics.pairwise import cosine_similarity
        st.subheader("☻Resume Analysis Result:")

        similarity=cosine_similarity([vector_array[0]],[vector_array[1]])[0][0]
        score=round(similarity*100, 2)
        st.success(f"Your resume matches the job description by {score}%.")
       

        # Create a simple bar chart for visualization
        fig, ax = plt.subplots()
        ax.bar(['Match Score'], [score], color='skyblue')
        ax.set_ylim(0, 100)
        ax.set_ylabel('Percentage (%)')
        ax.set_title('Resume–Job Match Score')

        # Display the histogram in Streamlit
        st.pyplot(fig)
        


        
web_page()       
    
