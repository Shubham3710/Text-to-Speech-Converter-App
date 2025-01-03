import streamlit as st
from gtts import gTTS
import tempfile

# Title
st.title("Text-to-Speech Converter")

# Text Input
text_input = st.text_area("Enter the desired text to convert to speech:")

# Language Selection
language = st.selectbox("Select language:", ["en", "es", "fr", "de", "hi"])

# Button to Generate Speech
if st.button("Generate Speech"):
    if text_input.strip():  # Check if text is not empty
        try:
            # Generate text-to-speech
            tts = gTTS(text=text_input, lang=language, slow=False)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
                tts.save(temp_audio_file.name)
                # Read and play audio
                with open(temp_audio_file.name, "rb") as audio_file:
                    audio_bytes = audio_file.read()
                
                st.audio(audio_bytes, format="audio/mp3")  # Audio playback
                st.download_button(
                    label="Download Audio",
                    data=audio_bytes,
                    file_name="output.mp3",
                    mime="audio/mp3",
                )  # Download button
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to convert to speech.")

# Footer
st.markdown("Developed using **Streamlit** and **gTTS**")
