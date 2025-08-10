import streamlit as st
from pathlib import Path
from streamlit.components.v1 import iframe

# ---------------------------
# Basic page config
# ---------------------------
st.set_page_config(
    page_title="Hemamalini L — Portfolio",
    page_icon="🚴‍♀️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------
# Helper functions
# ---------------------------
def load_pdf(path: Path):
    if path.exists():
        return path.read_bytes()
    return None

def project_card(title, short_desc, tech, github_url=None, demo_url=None, imgs=None):
    """Display a project card with optional demo iframe or link."""
    st.subheader(title)
    st.write(short_desc)
    st.markdown(f"**Tech:** {tech}")
    cols = st.columns([1, 3])
    with cols[0]:
        if github_url:
            st.markdown(f"[📁 GitHub]({github_url})")
        if demo_url:
            st.markdown(f"[🔗 Live Demo]({demo_url})")
        if not github_url and not demo_url:
            st.info("No live demo / repo provided. Update the app with your links.")
    with cols[1]:
        # If demo_url is an embeddable app (Streamlit, HuggingFace, etc.) attempt to embed
        if demo_url:
            try:
                iframe(demo_url, height=400)
            except Exception:
                st.write("Unable to embed the demo; open the Live Demo link above.")
        elif imgs:
            for img in imgs:
                st.image(img, use_column_width=True)

# ---------------------------
# Sidebar - contact & resume
# ---------------------------
st.sidebar.title("Contact")
st.sidebar.markdown("**Hemamalini L**  \nTiruchengode, Tamil Nadu")
st.sidebar.markdown("📧 hemamalini291204@gmail.com")
st.sidebar.markdown("🔗 GitHub: [Hemamalini-L](https://github.com/Hemamalini-L)")
st.sidebar.markdown("🔗 LinkedIn: [hemamalini-loganathan](https://www.linkedin.com/in/hemamalini-loganathan-60b4a02a1)")

# Attempt to load resume file (place the PDF next to app.py)
resume_path = Path("Hemamalini_Resume_Updated.pdf")
pdf_bytes = load_pdf(resume_path)
if pdf_bytes:
    st.sidebar.download_button(
        label="📄 Download Resume (PDF)",
        data=pdf_bytes,
        file_name="Hemamalini_Resume_Updated.pdf",
        mime="application/pdf"
    )
else:
    st.sidebar.info("Place 'Hemamalini_Resume_Updated.pdf' in the app folder to enable PDF download.")

st.sidebar.markdown("---")
st.sidebar.markdown("🔧 Want help deploying? Ask me!")

# ---------------------------
# Main page - Header
# ---------------------------
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Hemamalini L")
    st.write("Aspiring AI & Data Science enthusiast — projects: EcoCycle, Fake News Detection, AI Resume Screening.")
    st.write("**Email:** hemamalini291204@gmail.com  •  **GitHub:** Hemamalini-L")
with col2:
    st.image("https://avatars.githubusercontent.com/Hemamalini-L", width=120)  # fallback to GitHub avatar (if public)

st.markdown("---")

# ---------------------------
# Summary & Experience
# ---------------------------
st.header("Summary")
st.write(
    "Aspiring AI and Data Science enthusiast seeking internships or roles in AI/ML domains. "
    "Experienced with building ML pipelines, deploying Streamlit demos, and designing real-world solutions."
)

st.header("Experience")
st.subheader("AI Intern - Lead Scoring System (Infosys Springboard) — Nov 2024 - Feb 2025")
st.markdown("- Implemented an AI-powered B2B lead scoring and account-based marketing model.")

st.subheader("AI Intern - Resume Screening System (AICTE – Edunet Techsakhsham) — Jan 2025 - Mar 2025")
st.markdown("- Created an NLP-based ranking model to automate resume evaluation.")

st.markdown("---")

# ---------------------------
# Projects - replace demo_url/github_url with your actual links
# ---------------------------
st.header("Projects (Live Demos)")

# Project 1: EcoCycle
project_card(
    title="EcoCycle — Smart Cycle Sharing System",
    short_desc=(
        "A Streamlit app for smart cycle sharing with route optimization, booking system, accessibility features "
        "for differently-abled users, and emergency alerts."
    ),
    tech="Python • Streamlit • React (frontend idea) • Simple routing algorithms",
    github_url="https://github.com/Hemamalini-L/EcoCycle-AI",       # update if repo path differs
    demo_url="https://your-ecocycle-demo-url.streamlitapp.com"      # <-- REPLACE with your deployed Streamlit URL
)

st.markdown("---")

# Project 2: Fake News Detection
project_card(
    title="Fake News Detection System",
    short_desc=(
        "A classification pipeline using TF-IDF + Logistic Regression / SVM / Random Forest. "
        "Deployed a Streamlit demo for uploading text and seeing predictions."
    ),
    tech="Python • scikit-learn • TF-IDF • Streamlit",
    github_url="https://github.com/Hemamalini-L/fake-news-detection", # update repo link
    demo_url="https://your-fake-news-demo.streamlitapp.com"            # <-- REPLACE with your deployed Streamlit URL
)

st.markdown("---")

# Project 3: AI Resume Screening and Candidate Ranking
project_card(
    title="AI Resume Screening & Candidate Ranking",
    short_desc=(
        "NLP pipeline to parse resumes, extract features, and rank candidates. Includes Streamlit dashboard visualizations."
    ),
    tech="Python • spaCy/NLTK • scikit-learn • Streamlit • pandas",
    github_url="https://github.com/Hemamalini-L/AI-Resume-Screening",   # update repo link
    demo_url="https://your-resume-screening-demo.streamlitapp.com"       # <-- REPLACE with your deployed Streamlit URL
)

st.markdown("---")

# ---------------------------
# Skills, Education, Awards
# ---------------------------
st.header("Skills")
st.write(
    "- **Languages:** Python, C++, Java (basics)\n"
    "- **Libraries:** NumPy, Pandas, scikit-learn, Matplotlib, Seaborn\n"
    "- **Tools:** Git, Streamlit, Docker (optional), TensorFlow/PyTorch (optional)\n"
    "- **Areas:** Supervised Learning, NLP, EDA, Model Evaluation, Deployment"
)

st.header("Education")
st.write("**B.Tech — Artificial Intelligence and Data Science**  \nVivekanandha College of Technology for Women (Anna University) — Current (8.5 CGPA)")

st.header("Awards & Honors")
st.write(
    "- 2nd Prize — Technical Presentation (EcoCycle) — Paavai College\n"
    "- 2nd Prize — Technical Marketing — Paavai College\n"
    "- Runner-Up — Brand Brilliance Marketing — Sona College of Technology"
)

st.markdown("---")

# ---------------------------
# Live demo tips and admin panel
# ---------------------------
st.subheader("How to use this app for a live demo (presenter notes)")
st.markdown("""
1. **Open each project's Live Demo link** (or embedded iframe) to show a working app.
2. If embedding fails, click the *Live Demo* link to open the deployed Streamlit app in a new tab.
3. For local demos, run those Streamlit apps on your machine and replace `demo_url` with `http://localhost:8501` (or the port you use).
4. To make the demos embeddable, deploy each project to Streamlit Cloud, Hugging Face Spaces, or a VPS.
""")

st.markdown("---")

# ---------------------------
# Footer / Contact CTA
# ---------------------------
st.write("Want this deployed for you or need help updating the repo links? ")
if st.button("📩 Email Hemamalini"):
    st.write("Click the email link below to contact:")
    st.markdown("[Send Email](mailto:hemamalini291204@gmail.com)")

st.caption("Portfolio generated with Streamlit • Edit app.py to customize text, links, and visuals.")
