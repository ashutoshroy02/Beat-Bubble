import streamlit as st
from frontend import render_frontend
from audio_utils import record_audio
from api_handler import identify_song

def main():
    #load_background
    render_frontend()
    st.write("Please record a song snippet.")
    st.write("Yellow mic - recording ... Green mic- not recording ")
    audio_file_path = record_audio()
    if audio_file_path:
        if st.button("Identify Song"):
            song_details = identify_song(audio_file_path)
            if "error" not in song_details:
                st.success("Song Identified!")
                st.write(f"**Song:** {song_details['track_name']}")
                st.write(f"**Artist:** {song_details['artist']}")
                st.write(f"**Genre:** {song_details['Genre']}")
                st.write(f"**Duration:** {song_details['Duration']} min")
                st.write(f"**Release Date:** {song_details['Release_date']}")
                st.write(f"**Language:** {song_details['Language']}")
                
                st.write(f"[Spotify Link]({song_details['spotify_url']}) | [YouTube Link]({song_details['youtube_url']})")
            else:
                st.error(song_details["error"])
        else:
            st.warning("No audio recorded. Please record a song snippet.")

if __name__ == "__main__":
    main()
