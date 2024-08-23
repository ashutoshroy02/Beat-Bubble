import streamlit as st
import pyaudio
import wave
import os
import json
import requests
from api_ca import make_api_call  # We'll create this function

# Parameters for audio recording
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "song.wav"

def record_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    
    st.text("Recording...")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    st.text("Recording finished.")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
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

    except KeyError as e:
        st.error(f"Error processing response: {e}")

def main():
    st.title("Song Identification App")

    if st.button("Record Song"):
        record_audio()

    if st.button("Identify Song"):
        identify_song()

if __name__ == "__main__":
    main()