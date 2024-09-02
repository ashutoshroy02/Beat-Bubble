#frontend

import streamlit as st

st.set_page_config(
    page_title="BEAT BUBBLE ",
    page_icon="🎶"
)

# CSS styles
css = """
<style>
body {
  margin: 0;
  padding: 0;
  text-align: left;
  min-height: 100vh;
  background-image: linear-gradient(80deg, rgb(5, 124, 172), rgb(199, 10, 114));
  overflow: hidden;
}

#up {
    position: absolute; 
    height: 800px;
    width: 800px;
    border-radius: 50%;
    background-image: linear-gradient(80deg, rgb(5, 124, 172), rgb(43, 247, 202, 0.5));
    filter: blur(80px);
    animation: down 40s infinite;
}
#down {
    position: absolute; 
    right: 0;
    height: 500px;
    width: 500px;
    border-radius: 50%;
    background-image: linear-gradient(80deg, rgba(245, 207, 82, 0.8), rgba(199, 10, 114))
    filter: blur(80px);
    animation: up 30s infinite;
}

#left {
    position: absolute;
    height: 500px;
    width: 500px;
    border-radius: 50%;
    background-image: linear-gradient(80deg, rgb(199, 10, 160), rgba(183, 253, 52, 0.8));
    filter: blur(80px);
    animation: left 40s 1s infinite;
}

#right {
    position: absolute;
    height: 500px;
    width: 500px;
    border-radius: 50%;
    background-image: linear-gradient(80deg, rgba(26, 248, 18, 0.6), rgba(199, 10, 52, 0.8));
    filter: blur(80px);
    animation: right 30s .5s infinite;
}

@keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
}
@keyframes floating {
    0% { transform: translateY(0px); }
    50% { transform: translateY(5px); }
    100% { transform: translateY(0px); }
}

@keyframes down {
    0%, 100%{
        top: -100px;
    }
    70%{
        top: 700px;
    }
}

@keyframes up {
    0%, 100%{
        bottom: -100px;
    }
    70%{
        bottom: 700px;
    }
}
@keyframes left {
    0%, 100%{
        left: -100px;
    }
    70%{
        left: 1000px;
    }
}

@keyframes right {
    0%, 100%{
        right: -100px;
    }
    70%{
        right: 1000px;
    }
}

a:hover {
    color: black;
}
a:hover button {
    background-color: white !important;
    color: black !important;
}
</style>
"""

# HTML content
html = """
<section id="up"></section>
<section id="down"></section>
<section id="left"></section>
<section id="right"></section>
"""

st.markdown(css, unsafe_allow_html=True)
st.markdown(html, unsafe_allow_html=True)

st.markdown("<h1 style='color: white; opacity: 0; animation: fadeIn 8s ease forwards, floating 2s ease infinite;'>"
            # "<span style='font-weight:normal; font-family: sans serif; font-size: 50px;'></span>"
            "<span style='font-weight:bold; font-family: serif; font-size: 70px; font-weight:bold;'>BEAT BUBBLE </span>"
            "</h1>", unsafe_allow_html=True)

st.markdown("<p style='opacity: 0; animation: fadeIn 10s ease forwards; font-size: 20px;'><strong></strong><br>" "what if we don't know the name of the song we want to listen ? "
            "what if we only know a <strong>tune</strong> or <strong>just the hum</strong> we want to listen to?<br>"
            "<i><strong>BEAT BUBBLE aims to solve that</strong></i>. <br>" "we will find the song that you just sung or remembered a little bit !</p>", unsafe_allow_html=True)

# st.markdown(f'''
# <a href='https://www.youtube.com/watch?v=fDcFn_MuhKA'><button style="font-weight:bold; opacity: 0; animation: fadeIn 5s ease forwards; background-color:black; border-radius: 20px; padding: 10px 20px; border: none; color: white;">get started</button></a>
# ''', unsafe_allow_html=True)




import streamlit as st
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import io
import requests
import json
import time
import os
import base64
import hashlib
import hmac

# Parameters for audio recording
RATE = 44100
RECORD_SECONDS = 10

# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state['history'] = []

def record_audio():
    st.text("Recording...")
    
    audio_data = sd.rec(int(RECORD_SECONDS * RATE), samplerate=RATE, channels=1, dtype='int16')
    sd.wait()
    
    audio_bytes = io.BytesIO()
    write(audio_bytes, RATE, audio_data)
    audio_bytes.seek(0)  # Rewind the stream to the beginning
    
    st.text("Recording finished.")
    return audio_bytes

def make_api_call(audio_bytes):
    access_key = os.getenv("access_key")
    access_secret = os.getenv("access_secret")
    requrl = "https://identify-ap-southeast-1.acrcloud.com/v1/identify"
    http_method = "POST"
    http_uri = "/v1/identify"
    data_type = "audio"
    signature_version = "1"
    timestamp = time.time()

    string_to_sign = f"{http_method}\n{http_uri}\n{access_key}\n{data_type}\n{signature_version}\n{str(timestamp)}"
    sign = base64.b64encode(hmac.new(access_secret.encode('ascii'), string_to_sign.encode('ascii'), digestmod=hashlib.sha1).digest()).decode('ascii')

    files = [
        ('sample', ('sample.wav', audio_bytes, 'audio/wav'))
    ]

    data = {
        'access_key': access_key,
        'sample_bytes': audio_bytes.getbuffer().nbytes,
        'timestamp': str(timestamp),
        'signature': sign,
        'data_type': data_type,
        'signature_version': signature_version
    }

    response = requests.post(requrl, files=files, data=data)
    response.encoding = "utf-8"
    return response

def identify_song(audio_bytes):
    response = make_api_call(audio_bytes)
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
        artist = music_info.get('artists', [{}])[0].get('name', 'Unknown Artist')
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
    st.sidebar.title("Song History 🎶")
    if st.session_state['history']:
        for entry in st.session_state['history']:
            st.sidebar.write(f"**Track Name:** {entry['track_name']}")
            st.sidebar.write(f"**Artist:** {entry['artist']}")
            st.sidebar.write(f"**Album:** {entry['album']}")
            st.sidebar.write(f"[Spotify Link]({entry['spotify_url']}) | [YouTube Link]({entry['youtube_url']})")
            st.sidebar.write("---")
    else:
        st.sidebar.write("No history yet. Start singing!")
        
    if st.button("☠️"):
        audio_bytes = record_audio()
        identify_song(audio_bytes)
 
if __name__ == "__main__":
    main()
