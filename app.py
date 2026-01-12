"""
Main Application Entry Point.

This script initializes the Streamlit application, loads assets, and renders
the HTML structure. It follows a clean architecture pattern by delegating
logic to `utils`, `config`, and `components`.
"""
import streamlit as st
import streamlit.components.v1 as components
from config import PROFILE
from utils import load_css, load_js
from components.html_templates import (
    get_navbar_html, 
    get_main_dashboard_html,
    get_projects_view_html
)

def main() -> None:
    """
    Main execution function.
    Sets up page config, loads resources, and renders the app.
    """
    # 1. Page Configuration
    st.set_page_config(
        page_title=f"{PROFILE['name']} | Neural Portfolio",
        layout="wide",
        initial_sidebar_state="collapsed",
        page_icon="⚡"
    )

    # 1.1 Global CSS Injection (Fix for Deployment)
    # This must be done in the parent Streamlit context, not inside the iframe.
    st.markdown("""
        <style>
            /* Remove default Streamlit padding */
            .block-container {
                padding-top: 0rem !important;
                padding-bottom: 0rem !important;
                padding-left: 0rem !important;
                padding-right: 0rem !important;
                max-width: 100% !important;
            }
            
            /* Hide Streamlit UI elements */
            header, #MainMenu, footer { 
                display: none !important; 
            }
            
            /* Ensure iframe takes full height */
            iframe {
                height: 100vh !important;
                width: 100vw !important;
            }
            
            /* Hide scrollbars for cleaner look */
            .main {
                overflow: hidden;
            }
        </style>
    """, unsafe_allow_html=True)

    # 2. Asset Loading
    # Using robust utility functions from utils.py
    css_content = load_css("styles/main.css")
    js_script = load_js("scripts/mascot.js")
    particles_script = load_js("scripts/particles.js")

    # 3. HTML Assembly
    app_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=JetBrains+Mono:wght@700&family=Fredoka:wght@400;600&family=Playfair+Display:ital,wght@1,400&display=swap" rel="stylesheet">
        
        <!-- CSS Injection -->
        <style>
            {css_content}
        </style>
    </head>
    <body>
        {get_navbar_html()}
        
        <!-- Main Dashboard View -->
        {get_main_dashboard_html()}
        
        <!-- Projects View -->
        {get_projects_view_html()}
        
        <!-- JS Injection -->
        <script>
            {js_script}
            {particles_script}
        </script>
        

    </body>
    </html>
    """

    # 4. Render Application
    # Using height=1000 and scrolling=True to ensure full viewport usage
    components.html(app_html, height=1000, scrolling=True)

if __name__ == "__main__":
    main()
