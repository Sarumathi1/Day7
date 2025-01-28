from dotenv import load_dotenv
import chain
import streamlit as st
from home import home_page

load_dotenv()

# Define the pages for navigation
PAGES = {
    "Home": "home",
    "Generate Code": "generate_code"
}

# Initialize session state for page navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"  # Default to "Home"

def navigate_to(page):
    """
    Updates session state to navigate between pages.
    """
    st.session_state.current_page = PAGES[page]

def generate_code_page():
    """
    Displays the Quiz Generator Form
    """
    st.markdown(
        """
        <div style="background-color: #4CAF50; padding: 20px; text-align: center; border-radius: 10px; color: white;">
            <h1 style="font-family: Arial, sans-serif;">Quiz Generator</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Form for quiz generation
    with st.form("code_generator"):
        Language = st.selectbox("Select the lanuage for the cide", [ "python", "java", "C", "C++"])
        difficulty = st.selectbox("Select Difficulty Level", ["Easy", "Medium", "Hard"])
        num_questions = st.number_input("Enter the Number of Questions", min_value=1, max_value=50, step=1)
        
        submitted = st.form_submit_button("Submit", help="Click to generate your quiz!")
        
        if submitted:
            with st.spinner("Generating your quiz..."):
                response = chain.generate_quiz(topic, difficulty, num_questions)
                st.success("Quiz Generated Successfully!")
                st.info(response)

def main():
    # Render the current page
    if st.session_state.current_page == "home":
        home_page(navigate_to)
    elif st.session_state.current_page == "generate_code":
        generate_code_page()

if _name_ == "_main_":
    main()