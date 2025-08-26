# ui/chat_ui.py

import os
import json
import streamlit as st
from chatbot.agent import generate_response
from prompts.base_prompts import (
    greeting_prompt,
    info_collection_prompt,
    tech_stack_prompt,
    dynamic_generation_prompt,
    exit_keywords,
    exit_message,
)

# Save candidate info to JSON
def save_candidate_data(candidate):
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", "candidates.json")

    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(candidate)

    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)


def render_chat_interface():
    st.set_page_config(page_title="TalentScout Hiring Assistant", layout="centered")

    st.markdown(
        "<h2 style='text-align: center;'>🤖 TalentScout Hiring Assistant</h2>",
        unsafe_allow_html=True,
    )

    # Initialize states
    if "conversation" not in st.session_state:
        st.session_state.conversation = []
    if "ended" not in st.session_state:
        st.session_state.ended = False
    if "started" not in st.session_state:
        st.session_state.started = False
    if "user_info" not in st.session_state:
        st.session_state.user_info = {}
    if "tech_stack_collected" not in st.session_state:
        st.session_state.tech_stack_collected = False

    # Greeting
    if not st.session_state.started:
        st.markdown(
            f"<div class='chat-bubble bot'><strong>Assistant:</strong><br>{greeting_prompt}</div>",
            unsafe_allow_html=True,
        )
        if st.button("Begin"):
            st.session_state.started = True
            st.rerun()
        return

    # Collect user info
    if not st.session_state.user_info:
        st.markdown(info_collection_prompt, unsafe_allow_html=True)

        with st.form("candidate_info"):
            full_name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            phone = st.text_input("Phone Number")
            years_exp = st.text_input("Years of Experience")
            location = st.text_input("Current Location")
            desired_pos = st.text_input("Desired Position")
            submitted = st.form_submit_button("Save & Continue")

            if submitted:
                st.session_state.user_info = {
                    "Full Name": full_name,
                    "Email": email,
                    "Phone": phone,
                    "Experience": years_exp,
                    "Location": location,
                    "Desired Position": desired_pos,
                }
                save_candidate_data(st.session_state.user_info)
                st.rerun()
        return

    # Collect tech stack
    if not st.session_state.tech_stack_collected:
        st.markdown(tech_stack_prompt, unsafe_allow_html=True)
        tech_stack = st.text_input("Tech Stack (comma separated)")

        if st.button("Submit Tech Stack"):
            st.session_state.user_info["Tech Stack"] = tech_stack
            st.session_state.tech_stack_collected = True

            bot_msg = (
                f"Thanks, {st.session_state.user_info['Full Name']}! "
                f"Based on your tech stack, here are some questions:"
            )
            st.session_state.conversation.append(("bot", bot_msg))

            # ✅ Fixed: no system role, just user prompt
            prompt = dynamic_generation_prompt(tech_stack)
            questions = generate_response([("user", prompt)])

            st.session_state.conversation.append(("bot", questions))
            st.rerun()
        return

    # Main conversation loop
    if not st.session_state.ended:
        for role, msg in st.session_state.conversation:
            role_class = "bot" if role == "bot" else "user"
            label = "Assistant" if role == "bot" else "You"
            st.markdown(
                f"<div class='chat-bubble {role_class}'><strong>{label}:</strong><br>{msg}</div>",
                unsafe_allow_html=True,
            )

        with st.form("chat_form", clear_on_submit=True):
            user_input = st.text_input("Your reply", placeholder="Type here...")
            send = st.form_submit_button("Send")

            if send and user_input.strip():
                st.session_state.conversation.append(("user", user_input.strip()))

                if any(exit_word in user_input.lower() for exit_word in exit_keywords):
                    st.session_state.conversation.append(("bot", exit_message))
                    st.session_state.ended = True
                else:
                    bot_reply = generate_response([("user", user_input.strip())])
                    st.session_state.conversation.append(("bot", bot_reply))

                st.rerun()
    else:
        st.success("✅ Session ended. Refresh the page to start again.")
