import streamlit as st
import pandas as pd
import requests
import uuid  # To generate unique Founder IDs
import asyncio
import time

st.set_page_config(layout="wide", page_title="Investor-Startup Matching & Chat")

# Initialize session state variables efficiently
st.session_state.setdefault("id", uuid.uuid4())
st.session_state.setdefault("file_cache", {})
st.session_state.setdefault("messages", [])  # Store chat history
st.session_state.setdefault("workflow", None)
st.session_state.setdefault("workflow_logs", [])

# ---- Sidebar for CSV Upload ----
st.sidebar.title("📂 Upload Investor CSV")
investor_file = st.sidebar.file_uploader("Upload Investor Data (CSV)", type=["csv"])

# Initialize session state for form visibility
if "show_form" not in st.session_state:
    st.session_state.show_form = False

if investor_file:
    investor_df = pd.read_csv(investor_file)
    st.session_state["investor_df"] = investor_df  # Store in session state
    st.sidebar.write("### 📊 Investor Data")
    st.sidebar.dataframe(st.session_state["investor_df"])  # Show DataFrame in sidebar


# ---- Main Chat Interface ----
col1, col2 = st.columns([6, 1])

with col1:
    st.markdown("<h1 style='text-align: center; '>💼 Founder-Investor Matchmaking Hub</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>🤝 Connecting Visionary Founders with Strategic Investors</h3>", unsafe_allow_html=True)
with col2:
    st.button("Clear ↺", on_click=lambda: st.session_state.update(messages=[], workflow_logs=[]))
    
# Display chat messages from history on app rerun
for i, message in enumerate(st.session_state.get("messages", [])):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

    # Display logs AFTER the user message but BEFORE the next assistant message
    if message["role"] == "user" and "log_index" in message and i < len(st.session_state.messages) - 1:
        log_index = message["log_index"]
        if log_index < len(st.session_state.get("workflow_logs", [])):
            with st.expander("📜 View Workflow Execution Logs", expanded=False):
                st.code(st.session_state.workflow_logs[log_index], language="text")

# Accept user input
if prompt := st.chat_input("💬 Ask a question about your documents..."):
    log_index = len(st.session_state.get("workflow_logs", []))
    
    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt, "log_index": log_index})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    if "investor_df" not in st.session_state:
        st.warning("⚠️ Please upload investor data first.")
    else:
        # Convert user input into a DataFrame
        founder_data = {
            "Founder_ID": f"F{uuid.uuid4().hex[:5]}",  # Generate a unique ID F{uuid.uuid4().hex[:5]}
            "Query": prompt
        }
        founder_df = pd.DataFrame([founder_data])
        st.session_state["founder_df"] = founder_df  # Store in session state
        
        # Send to Flask API as JSON
        flask_url = "http://127.0.0.1:5000/match_founders"
        payload = {
            "founders": founder_df.to_dict(orient="records"),
            "investors": st.session_state.get("investor_df", pd.DataFrame()).to_dict(orient="records"),
        }

        response = requests.post(flask_url, json=payload)
        # print(response)
        text_response = None
        if response.status_code == 200:
            data = response.json()
            matches = data['match_scores']
            text_response = data['text_response']
            df_matches = pd.DataFrame(matches)
            
            st.write("### 🏆 Matching Investors")
            st.dataframe(df_matches)
        else:
            st.error("❌ Error fetching match results!")

        # Display assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            try:
                for word in text_response.split():
                    full_response += word + " "
                    message_placeholder.markdown(full_response + "▌")
                    time.sleep(0.1)  # Simulating typing effect
            except Exception:
                full_response = "Sorry! I don't know the answer."
            message_placeholder.markdown(full_response)

        # Store assistant response
        st.session_state.messages.append({"role": "assistant", "content": full_response})
