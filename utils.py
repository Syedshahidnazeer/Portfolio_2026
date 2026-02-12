import os
import base64
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_file(filepath: str) -> str:
    abs_path = os.path.join(BASE_DIR, filepath)
    try:
        with open(abs_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"Asset missing: {filepath}")
        return f"/* Error: File {filepath} not found at {abs_path} */"
    except Exception as e:
        return f"/* Error loading {filepath}: {str(e)} */"


def img_to_bytes(file_path: str) -> str:
    abs_path = os.path.join(BASE_DIR, file_path)
    try:
        with open(abs_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            ext = file_path.rsplit(".", 1)[-1]
            return f"data:image/{ext};base64,{encoded_string}"
    except FileNotFoundError:
        return ""
    except Exception:
        return ""
