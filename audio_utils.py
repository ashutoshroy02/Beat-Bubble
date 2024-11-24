import streamlit as st
from audio_recorder_streamlit import audio_recorder

def record_audio():
    
    audio_data = audio_recorder(pause_threshold=4,
    sample_rate=44100,
    icon_name="fa-solid fa-microphone-lines",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_size="3x")
    if audio_data:
        st.audio(audio_data)
        file_path = "song.wav"
        with open(file_path, "wb") as f:
            f.write(audio_data)  
        return file_path
    else:
        return 