import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


def main():
    st.title("Arabic Sign Language Converter")
    st.write("Speak in Arabic and see the corresponding sign language animation.")

    # Create a file uploader to upload audio
    audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

    # Check if audio file is uploaded
    if audio_file is not None:
        # Convert audio to text using speech recognition
        r = sr.Recognizer()
        audio = sr.AudioFile(audio_file.name)
        with audio as source:
            audio_data = r.record(source)
            text = r.recognize_sphinx(audio_data, language="ar-EG")

        # Display the recognized text
        st.write("Recognized Text: ", text)

        # Convert the recognized text to sign language animation using text-to-speech
        tts = gTTS(text, lang="ar")
        tts.save("animation.mp3")

        # Play the sign language animation audio
        playsound("animation.mp3")

if __name__ == "__main__":
    main()
