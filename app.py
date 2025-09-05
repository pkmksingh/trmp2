# app.py

import streamlit as st
import subprocess

st.title("🎥 Twitch Relay Control Panel")

if st.button("Start Relay"):
    subprocess.Popen(["python", "stream_manager.py"])
    st.success("Relay started in background!")

st.markdown("✅ This will keep streaming even if Twitch goes offline or this page is closed.")
