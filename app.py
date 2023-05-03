from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Alex Borio"
PAGE_ICON = ":wave:" #"random"
NAME = "Alex Borio"
DESCRIPTION = """
Data Scientist @ Deloitte Risk Advisory
"""
EMAIL = "alex.borio@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/alex-borio-8542115b/",
    "GitHub": "https://github.com/borio93",
    "Email": "mailto:" + EMAIL,
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    #st.write("📧", EMAIL)
    

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 3 Years experience extracting actionable insights from data in banking sector
- ✔️ Strong hands on experience and knowledge in Python, Power BI and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


st.write('\n')
st.write("---")


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- Programming: Python (NumPy - Pandas - Scikit-learn - Matplot -Seaborn), SQL, VBA
- Data Visualization: Power BI, Tableau, MS Excel
- Modeling: Logistic regression, linear regression, decition trees
- Databases: MySQL, Oracle, Teradata, Hadoop
- Cloud Services: Google Cloud Platform, Amazon Web Services
"""
)


st.write('\n')
st.write("---")


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")

# --- JOB 1
st.write("**Data Scientist | Deloitte**")
st.write("02/2022 - Present")
st.write(
    """
Activities related to projects aimed at Financial Services, with a strong focus on Business Architecture using data analysis and data
modeling technologies with particular attention to IT issues on Risk Management engagements, Data Management, Data
Governance and Reporting.
Key experiences:
- Code migration from SAS (EG 9.3) / R to Python / BigQuery / PySpark
- Machine learning activities (e.g. NLP algorithm to estimate KPI and KRI on the four fundamental pillars of Data Governance: Data Dictionary, Data Quality, Data Lineage and Business Glossary)
- Development of a Data Governance framework to support the II level Function in assessing the degree of maturity and the I level Functions in monitoring the Data Governance safeguards to protect the data under their responsibility, with implementation of the dashboard for monitoring the various indicators calculated
- Development of Dashboards (e.g. monitor the RAF indicator and the underlying indices previously calculated with NLP and Networking Intelligence algorithms)
- Development of an unsupervised algorithm (k-means) in order to create a cluster of equity portfolios (ESG) to be included in an expected return calculation model
- Development of a framework for the automatic maintenance of Data Lineage in a Cloud Environment for Data Governance Project
"""
)

# --- JOB 2
st.write('\n')
st.write("**Data Analyst | Accenture**")
st.write("05/2020 - 02/2022")
st.write(
    """
Activities related to projects aimed at Financial Services, with a strong focus on Financial Risk Management and Data Governance.
Key experiences:
- Statistical analysis on partitioned databases (Oracle / Teradata) to identify KPIs
- Development of a dashboard to monitor the progress of the KIs, KPIs and KRIs
- Creation of SQL scripts to perform back-end and UAT tests
- Development of a framework for Data Masking (Informatica Power Center)
- Statistical analysis on RDBS (Oracle / Teradata / Hadoop)
- Advanced Analytics activities
"""
)


st.write('\n')
st.write("---")


# --- EDUCATION ---
st.write('\n')
st.subheader("Education")

# --- EDU 1
st.write("**Data Engineer | Modis**")
st.write("03/2020 - 05/2020")
st.write(
    """
Intensive training academy (full-time) based on practical and theoretical learning of the main software used by the figure of the Data Engineer and ETL Developer.
The following software has been studied in depth:
- SQL
- MySQL
- Oracle Database
- IBM InfoSphere DataStage
Academy that allowed me to increase my knowledge in the statistical/IT field.
"""
)

# --- EDU 2
st.write("**Master's degree, Statistics | Università degli Studi di Torino**")
st.write("09/2017 - 03/2020")
st.write(
    """
The MSc in Statistics has a particular focus on modern computationally-intensive theory and methods. 
Main disciplines: Business Analytics, Corporate Finance and Strategy, Data Modeling, Econometrics, Epidemiology, Statistical Learning, Strategic Marketing, Time Series Analysis.
"""
)

# --- EDU 3
st.write("**Bachelor's degree, Statistics and Economics | Università degli Studi di Torino**")
st.write("09/2013 - 03/2017")
st.write(
    """
The Bachelor's Degree in Political and Economic Sciences has a particular focus on policy analysis and political economy. 
Main disciplines are: Policy Analysis, Political Economy, Political Economics, Corporate Finance and Strategy.
"""
)