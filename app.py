# app.py

import streamlit as st
from ui.chat_ui import render_chat_interface   # <── fixed import

def main():
    """
    Entry point for TalentScout Hiring Assistant.
    """
    render_chat_interface()

if __name__ == "__main__":
    main()
