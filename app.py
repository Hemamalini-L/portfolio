# app.py
import streamlit as st
from pathlib import Path
from streamlit.components.v1 import iframe

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Hemamalini L — Portfolio",
    page_icon="🚴‍♀️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------
# Helper: load resume PDF
# ---------------------------
def load_pdf_bytes(pdf_path: Path):
    if pdf_path.exists():
        return pdf_path.read_bytes()
    return None

# ---------------------------
# Replace these with your deployed project URLs
# (If you haven't deployed yet, keep them as None or local addresses)
# ---------------------------
ECOCYCLE_DEMO_URL = "https://your-ecocycle-demo.streamlit.app"          # <-- REPLACE
RESUME_SCREENING_DEMO_URL = "https://your-resume-screening.streamlit.app" # <-- REPLACE
FAKENEWS_DEMO_URL = "https://your-fake-news-demo.streamlit.app"         # <-- REPLACE

# ---------------------------
# Sidebar - Contact & Resume
# ---------------------------
st.sidebar.title("Contact")
st.sidebar.markdown("**Hemamalini L**  \nTiruchengode, Tamil Nadu")
st.sidebar.markdown("📧 hemamalini291204@gmail.com")
st.sidebar.markdown("🔗 GitHub: [Hemamalini-L](https://github.com/Hemamalini-L)")
st.sidebar.markdown("🔗 LinkedIn: [hemamalini-loganathan](https://www.linkedin.com/in/hemamalini-loganathan-60b4a02a1)")

# Resume download button (place the PDF next to this app)
resume_file = Path("Hemamalini_Resume_Updated.pdf")
pdf_bytes = load_pdf_bytes(resume_file)
if pdf_bytes:
    st.sidebar.download_button(
        label="📄 Download Resume (PDF)",
        data=pdf_bytes,
        file_name="Hemamalini_Resume_Updated.pdf",
        mime="application/pdf",
    )
else:
    st.sidebar.info("Place 'Hemamalini_Resume_Updated.pdf' in the app folder to enable resume download.")

st.sidebar.markdown("---")
st.sidebar.markdown("📝 Tip: Update the demo URLs at the top of `app.py` with your deployed app links.")
st.sidebar.markdown("---")

# ---------------------------
# Header / Hero section
# ---------------------------
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Hemamalini L")
    st.write("Aspiring AI & Data Science enthusiast — building ML solutions and deploying interactive demos.")
    st.write("**Email:** hemamalini291204@gmail.com  •  **GitHub:** [Hemamalini-L](https://github.com/Hemamalini-L)")
with col2:
    # Try to show GitHub avatar (if public). If not found, it's fine.
    st.image("https://avatars.githubusercontent.com/Hemamalini-L", width=110)

st.markdown("---")

# ---------------------------
# Summary & Experience
# ---------------------------
st.header("Summary")
st.write(
    "Aspiring AI and Data Science enthusiast seeking internships/roles in AI/ML. "
    "Experience in building ML pipelines, NLP systems, and deploying Streamlit demos for live demonstrations."
)

st.header("Experience")
st.subheader("AI Intern — Lead Scoring System (Infosys Springboard)")
st.write("Nov 2024 - Feb 2025")
st.markdown("- Implemented an AI-powered B2B lead scoring and account-based marketing model.")

st.subheader("AI Intern — Resume Screening System (AICTE – Edunet Techsakhsham)")
st.write("Jan 2025 - Mar 2025")
st.markdown("- Built an NLP-based resume ranking system and Streamlit dashboard for visualization.")

st.markdown("---")

# ---------------------------
# Projects section (embedded demos)
# ---------------------------
st.header("Projects — Live Demonstrations")

def show_project(title, description, demo_url=None, github_url=None, height=650):
    st.subheader(title)
    st.write(description)
    cols = st.columns([1, 4])
    with cols[0]:
        if github_url:
            st.markdown(f"[📁 GitHub]({github_url})")
        if demo_url:
            st.markdown(f"[🔗 Open Live Demo]({demo_url})")
        if not github_url and not demo_url:
            st.info("No link provided — update `app.py` with your repo/demo URL.")
    with cols[1]:
        if demo_url:
            # Attempt to embed the demo inside an iframe
            try:
                iframe(demo_url, height=height)
            except Exception:
                st.write("Embedding failed — click the Live Demo link above to open in a new tab.")
        else:
            st.info("Demo URL not set. Replace the placeholder in app.py with your deployed Streamlit URL.")

# Project: EcoCycle
show_project(
    title="🚲 EcoCycle — Smart Cycle Sharing System",
    description=(
        "A Streamlit app for smart cycle sharing with route optimization, booking system, accessibility features "
        "for differently-abled users, and emergency alerts. Demo includes interactive route booking and map visualization."
    ),
    demo_url=ECOCYCLE_DEMO_URL,
    github_url="https://github.com/Hemamalini-L/EcoCycle-AI",
    height=600
)

st.markdown("---")

# Project: Resume Screening
show_project(
    title="📄 AI Resume Screening & Candidate Ranking",
    description=(
        "Upload resumes and a job description (JD). The app parses resumes, extracts features, and ranks candidates "
        "based on relevance to the JD. Interactive dashboard shows scores and explanations."
    ),
    demo_url=RESUME_SCREENING_DEMO_URL,
    github_url="https://github.com/Hemamalini-L/AI-Resume-Screening",
    height=650
)

st.markdown("---")

# Project: Fake News Detection
show_project(
    title="📰 Fake News Detection System",
    description=(
        "Text classification pipeline using TF-IDF and classifiers (Logistic Regression / SVM / Random Forest). "
        "Streamlit demo accepts text input and returns prediction + confidence."
    ),
    demo_url=FAKENEWS_DEMO_URL,
    github_url="https://github.com/Hemamalini-L/fake-news-detection",
    height=600
)

st.markdown("---")

# ---------------------------
# Skills (as requested)
# ---------------------------
st.header("Skills")

st.subheader("Languages")
st.write("- Python\n- C++")

st.subheader("Tools")
st.write("- Git\n- Streamlit")

st.subheader("Areas of Expertise")
st.write("- Supervised Learning\n- NLP (Natural Language Processing)\n- EDA (Exploratory Data Analysis)\n- Model Evaluation\n- Deployment")

st.markdown("---")

# ---------------------------
# Education & Awards
# ---------------------------
st.header("Education")
st.write("**B.Tech — Artificial Intelligence and Data Science**")
st.write("Vivekanandha College of Technology for Women (Anna University) — Current (8.5 CGPA)")

st.header("Awards & Honors")
st.write(
    "- 2nd Prize — Technical Presentation (EcoCycle) — Paavai College\n"
    "- 2nd Prize — Technical Marketing — Paavai College\n"
    "- Runner-Up — Brand Brilliance Marketing — Sona College of Technology"
)

st.markdown("---")

# ---------------------------
# Presenter notes & Tips (useful for live demo)
# ---------------------------
st.subheader("Presenter Notes — How to Demo Live")
st.markdown(
    """
- Make sure each project is **deployed** to Streamlit Cloud (or Hugging Face Spaces) and is **public**.
- Replace the `ECOCYCLE_DEMO_URL`, `RESUME_SCREENING_DEMO_URL`, and `FAKENEWS_DEMO_URL` variables at the top of `app.py` with the deployed URLs.
- If embedding does not work due to headers or embedding policy, open the demo in a new tab using the Live Demo links.
- For local demos during interviews: run your project locally (e.g., `streamlit run app.py` for each project) and set the demo_url to `http://localhost:8501` (or the appropriate port). Then run the portfolio and present on the same machine.
- Keep sample resumes and JDs ready in a folder to quickly upload during the resume screening demo.
"""
)

st.markdown("---")

# ---------------------------
# Footer / Contact CTA
# ---------------------------
st.write("💬 Want me to deploy these for you step-by-step? I can provide exact copy-paste commands to push and deploy to Streamlit Cloud.")
st.caption("Portfolio generated with Streamlit — edit `app.py` to customize text, links, and visuals.")
