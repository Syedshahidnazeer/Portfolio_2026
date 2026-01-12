"""
Utility functions for the Portfolio Website.

This module provides helper functions for file loading and path management,
ensuring robust asset retrieval across different execution environments.
"""
import os
import streamlit as st
import base64
from typing import Optional

def load_file(filepath: str) -> str:
    """
    Reads a file from the project directory and returns its content.
    
    Uses absolute paths resolving relative to this script's location (`utils.py`)
    to prevent FileNotFoundError when running from different contexts.

    Args:
        filepath (str): Relative path to the file (e.g., 'styles/main.css').

    Returns:
        str: The content of the file, or an error comment if not found.
    """
    # Get the directory where this script (utils.py) resides
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct absolute path
    abs_path = os.path.join(base_dir, filepath)
    
    try:
        with open(abs_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        error_msg = f"/* Error: File {filepath} not found at {abs_path} */"
        st.error(f"Asset missing: {filepath}")
        return error_msg
    except Exception as e:
        return f"/* Error loading {filepath}: {str(e)} */"

def load_css(file_path: str = "styles/main.css") -> str:
    """
    Loads a CSS file and prepares it for injection.
    
    Args:
        file_path (str): Path to the CSS file.

    Returns:
        str: Raw CSS content.
    """
    return load_file(file_path)

def load_js(file_path: str) -> str:
    """
    Loads a JavaScript file and prepares it for injection.

    Args:
        file_path (str): Path to the JS file.

    Returns:
        str: Raw JS content.
    """
    return load_file(file_path)
def img_to_bytes(file_path:  str) -> str:
    """
    Converts an image file to a base64 encoded string.
    
    Args:
        file_path (str): Relative path to the image file.

    Returns:
        str: Base64 string prefixed with data URI scheme (e.g., 'data:image/png;base64,...').
    """
    # Get the directory where this script (utils.py) resides
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct absolute path
    abs_path = os.path.join(base_dir, file_path)
    
    try:
        with open(abs_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            ext = file_path.split('.')[-1]
            return f"data:image/{ext};base64,{encoded_string}"
    except FileNotFoundError:
        print(f"Error: Image {file_path} not found at {abs_path}")
        return ""
    except Exception as e:
        print(f"Error loading image {file_path}: {str(e)}")
        return ""
