import streamlit as st
import streamlit.components.v1 as components
from config import PROFILE
from utils import load_file
from components.html_templates import (
    get_navbar_html, get_main_dashboard_html, get_projects_view_html,
    get_education_view_html, get_experience_view_html, get_skills_detailed_view_html,
    get_certifications_view_html, get_contact_view_html, get_footer_html)


def main() -> None:
    st.set_page_config(
        page_title=f"{PROFILE['name']} | Neural Portfolio",
        layout="wide",
        initial_sidebar_state="collapsed",
        page_icon="⚡"
    )

    st.markdown("""
        <style>
            .block-container {
                padding-top: 0rem !important;
                padding-bottom: 0rem !important;
                padding-left: 0rem !important;
                padding-right: 0rem !important;
                max-width: 100% !important;
            }
            header, #MainMenu, footer {
                display: none !important;
            }
            iframe {
                width: 100% !important;
            }
            .main {
                overflow: hidden;
            }
        </style>
    """, unsafe_allow_html=True)

    css_content = load_file("styles/main.css")
    js_script = load_file("scripts/mascot.js")
    particles_script = load_file("scripts/particles.js")
    theme_script = load_file("scripts/theme.js")

    app_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="color-scheme" content="light dark">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;700&family=Fredoka:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
        <style>
            {css_content}
        </style>
    </head>
    <body>
        <div class="loading-screen">
            <div class="loading-logo">SHAHID<span style="opacity:0.5">.dev</span></div>
            <div class="loading-subtitle">Crafting Intelligent Systems</div>
            <div class="loading-bar"><div class="loading-bar-fill"></div></div>
        </div>

        <div class="scroll-progress"></div>

        <div class="floating-shapes">
            <div class="floating-shape"></div>
            <div class="floating-shape"></div>
            <div class="floating-shape"></div>
        </div>

        <canvas class="matrix-canvas" id="matrix-canvas"></canvas>

        <button class="scroll-top-btn" id="scroll-top-btn" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 15l-6-6-6 6"/></svg>
        </button>

        <div class="share-toast" id="share-toast">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0"><path d="M20 6L9 17l-5-5"/></svg>
            Link copied to clipboard!
        </div>

        <div class="cmd-palette-overlay" id="cmd-palette-overlay" onclick="closeCmdPalette(event)">
            <div class="cmd-palette">
                <div class="cmd-palette-header">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--text-dim)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                    <input class="cmd-palette-input" id="cmd-palette-input" placeholder="Search commands..." autocomplete="off" />
                    <kbd class="cmd-kbd">ESC</kbd>
                </div>
                <div class="cmd-palette-items" id="cmd-palette-items"></div>
            </div>
        </div>

        {get_navbar_html()}

        {get_main_dashboard_html()}

        {get_education_view_html()}

        {get_experience_view_html()}

        {get_skills_detailed_view_html()}

        {get_projects_view_html()}

        {get_certifications_view_html()}

        {get_contact_view_html()}

        {get_footer_html()}

        <script>
            {theme_script}
            {js_script}
            {particles_script}
        </script>

    </body>
    </html>
    """

    components.html(app_html, height=4000, scrolling=True)

if __name__ == "__main__":
    main()
