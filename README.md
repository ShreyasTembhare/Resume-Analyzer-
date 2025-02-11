🌴 AI Resume Analyzer 🌴
A Powerful Tool for Resume Analysis, Predictions, and Recommendations

==================================================
🚀 FEATURES
==================================================
For Applicants:
✔️ Extracts and organizes personal & professional details.
✔️ Identifies skills, keywords, and missing information.
✔️ Provides AI-driven job recommendations based on resume content.
✔️ Suggests courses & certifications to enhance qualifications.
✔️ Offers interview & resume improvement tips.
✔️ Generates an overall resume score.

For Recruiters & Administrators`   
✔️ Converts resume data into structured formats (CSV, Database).
✔️ Stores uploaded resumes for future reference.
✔️ Collects user feedback & ratings.
✔️ Provides detailed data analytics (job trends, experience levels, ratings, resume scores).

Feedback System:
✔️ Users can rate resumes on a 1-5 scale.
✔️ Overall ratings and review trends are visualized using pie charts.

==================================================
🎯 SCOPE
==================================================
1️⃣ Structured Resume Data Extraction - Converts raw resume content into structured formats (CSV, MySQL).
2️⃣ Resume Recommendations - AI-based suggestions to optimize resume quality.
3️⃣ Industry Insights - Analyzes job market trends and popular roles based on resume data.
4️⃣ University & College Use Case - Helps educational institutions analyze students’ resumes before placements.
5️⃣ User Engagement - Encourages users to improve resumes through feedback and analytics.

==================================================
🛠 TECH STACK
==================================================
Frontend:
- Streamlit
- HTML
- CSS
- JavaScript

Backend:
- Flask
- Python

Database:
- MySQL

Modules & Dependencies:
- pandas
- pyresparser
- pdfminer3
- NLTK (Natural Language Toolkit)
- Plotly

==================================================
🛠 SYSTEM REQUIREMENTS
==================================================
🔹 Python (3.9.12) - Download: https://www.python.org/downloads/release/python-3912/
🔹 MySQL Database - Download: https://www.mysql.com/downloads/
🔹 Visual Studio Code (or any code editor) - Download: https://code.visualstudio.com/Download
🔹 Visual Studio Build Tools (for C++ support) - Download: https://aka.ms/vs/17/release/vs_BuildTools.exe

==================================================
📥 INSTALLATION & SETUP
==================================================
To run this project locally, follow these steps:

1️⃣ Clone the Repository:
   git clone https://github.com/shreyastembhare/AI-Resume-Analyzer.git
   cd AI-Resume-Analyzer

2️⃣ Create & Activate a Virtual Environment (Recommended):
   python -m venv venv
   For macOS/Linux: source venv/bin/activate  
   For Windows: venv\Scripts\activate  

3️⃣ Install Dependencies:
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm

4️⃣ Configure the Database:
   - Create a new MySQL database named `cv`.
   - Update database credentials in `App.py` accordingly.

5️⃣ Run the Application:
   python app.py

🚀 The application should now be running on: http://127.0.0.1:5000/


