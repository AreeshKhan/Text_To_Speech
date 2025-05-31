import streamlit as st
import os
import sys
import base64
from text_to_speech.components.get_accent import get_accent_tld, get_accent_message
from text_to_speech.components.textTospeech import TTSapplication
from text_to_speech.exception import TTSException

st.set_page_config(page_title="Text to Speech", page_icon="🔊", layout="centered")

# CSS styling
st.markdown(
    """
    <style>
    .main {
        font-family: 'Inter', sans-serif;
    }
    .stButton>button {
        background-color: #2563eb !important;
        color: #ffffff !important;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    .stButton>button:hover {
        background-color: #1d4ed8 !important;
        color: #ffffff !important;
    }
    h1, h2, h3, label, p, span, div {
        color: inherit !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔊 Text to Speech Converter")
st.markdown("Transform your text into natural-sounding speech with multiple accents.")

try:
    accent_options = get_accent_message()
    accent_choice = st.selectbox("Select English Accent", accent_options)
    input_text = st.text_area("Enter your text here", height=200)

    if st.button("🔊 Convert to Speech"):
        if not input_text.strip():
            st.warning("Please enter some text.")
        else:
            try:
                # Get the correct tld for the accent
                accent_tld = get_accent_tld(accent_choice)
                if not accent_tld:
                    st.error("Selected accent is not supported.")
                    st.stop()

                # Convert text to speech
                tts_app = TTSapplication()
                base64_audio = tts_app.text2speech(input_text, accent_tld)

                # Save to temporary file
                temp_audio_path = "temp_audio.mp3"
                with open(temp_audio_path, "wb") as f:
                    f.write(base64.b64decode(base64_audio))

                st.success("✅ Speech successfully generated!")

                # Audio player
                st.audio(temp_audio_path, format="audio/mp3")

                # Download button
                with open(temp_audio_path, "rb") as audio_file:
                    st.download_button(
                        label="⬇️ Download Audio",
                        data=audio_file,
                        file_name="converted_speech.mp3",
                        mime="audio/mp3"
                    )

            except TTSException as e:
                st.error(f"TTSException: {e}")
            except Exception as e:
                st.exception(f"An unexpected error occurred: {e}")

except Exception as e:
    raise TTSException(e, sys)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by AREESH KHAN")
