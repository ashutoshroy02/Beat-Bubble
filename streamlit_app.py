import streamlit as st
import sounddevice as sd
import wave
import os
import json
import requests
from api_ca import make_api_call  

# Parameters for audio recording
CHUNK = 1024
FORMAT = 'int16'
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "song.wav"

def record_audio():
    st.text("Recording...")
    
    # Recording audio
    audio_data = sd.rec(int(RECORD_SECONDS * RATE), samplerate=RATE, channels=CHANNELS, dtype=FORMAT)
    sd.wait()  # Wait until recording is finished
    st.text("Recording finished.")
    
    # Saving the recorded audio as a .wav file
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 2 bytes for 'int16' format
        wf.setframerate(RATE)
        wf.writeframes(audio_data.tobytes())

def identify_song():
    if not os.path.isfile(WAVE_OUTPUT_FILENAME):
        st.error("No recorded audio found. Please record a song first.")
        return

    response = make_api_call(WAVE_OUTPUT_FILENAME)
    response_data = json.loads(response.text)

    try:
        music_info = response_data.get('metadata', {})
        if 'music' in music_info:
            music_info = music_info['music'][0]
        elif 'humming' in music_info:
            music_info = music_info['humming'][0]
        else:
            st.warning("No music or humming data found.")
            return

        track_name = music_info.get('title', 'Unknown Title')
        
        if 'spotify' in music_info.get('external_metadata', {}):
            spotify_artists = music_info['external_metadata']['spotify'].get('artists', [])
            artist = spotify_artists[0]['name'] if spotify_artists else 'Unknown Artist'
        else:
            artist = 'Unknown Artist'

        album = music_info.get('album', {}).get('name', 'Unknown Album')

        if 'spotify' in music_info.get('external_metadata', {}):
            spotify_track_url = f"https://open.spotify.com/track/{music_info['external_metadata']['spotify']['track']['id']}"
        else:
            spotify_track_url = "Spotify link not available"

        if 'youtube' in music_info.get('external_metadata', {}):
            youtube_video_url = f"https://www.youtube.com/watch?v={music_info['external_metadata']['youtube']['vid']}"
        else:
            youtube_video_url = "YouTube link not available"

        st.success("Song identified!")
        st.write(f"Track Name: {track_name}")
        st.write(f"Artist: {artist}")
        st.write(f"Album: {album}")
        st.write(f"Spotify Track URL: {spotify_track_url}")
        st.write(f"YouTube Video URL: {youtube_video_url}")
        from playsound import playsound
        playsound('song_mil_gaya.mp3')
        
    except KeyError as e:
        st.error(f"Error processing response: {e}")

def main():
    st.title("BEAT BUBBLE")

    if st.button("Record Song"):
        record_audio()

    if st.button("Identify Song"):
        identify_song()

if __name__ == "__main__":
    main()
