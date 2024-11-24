import time
import requests
import json
import os
import base64
import hashlib
import hmac

ACCESS_KEY = "3f2508ad4cea3f7817512c045c6a061b"
ACCESS_SECRET = "WSwB6Orpx1Mxt1EvfdGuS2Jryv2UM7CPb5EnubzW"
REQ_URL = "https://identify-ap-southeast-1.acrcloud.com/v1/identify"

def make_api_call(audio_file_path):
    timestamp = time.time()
    string_to_sign = f"POST\n/v1/identify\n{ACCESS_KEY}\naudio\n1\n{str(timestamp)}"
    sign = base64.b64encode(hmac.new(ACCESS_SECRET.encode('ascii'), string_to_sign.encode('ascii'), digestmod=hashlib.sha1).digest()).decode('ascii')
    
    with open(audio_file_path, 'rb') as audio_file:
        files = [('sample', ('test.wav', audio_file, 'audio/wav'))]
        data = {
            'access_key': ACCESS_KEY,
            'sample_bytes': os.path.getsize(audio_file_path),
            'timestamp': str(timestamp),
            'signature': sign,
            'data_type': 'audio',
            'signature_version': '1'
        }
        response = requests.post(REQ_URL, files=files, data=data)
        response.encoding = "utf-8"
        return response

def identify_song(audio_file_path):
    response = make_api_call(audio_file_path)
    response_data = json.loads(response.text)

    if 'metadata' in response_data:
        music_info = response_data['metadata'].get('music', [{}])[0]
        track_name = music_info.get('title', 'Unknown Title')
        artist = music_info.get('artists', [{}])[0].get('name', 'Unknown Artist')
        album = music_info.get('album', {}).get('name', 'Unknown Album')
        Duration=music_info.get('duration_ms')
        Genres=music_info.get('genres',[{}])[0].get('name','Unknown genre')
        release_date=music_info.get('release_date')
        Language=music_info.get('language')
        track_id_spotify=music_info.get('external_metadata',{}).get('spotify',{}).get('track',{}).get('id')
        spotify_url = music_info.get('external_metadata', {}).get('spotify', {}).get('track', {}).get('id', 'Not Available')
        youtube_url = music_info.get('external_metadata', {}).get('youtube', {}).get('vid', 'Not Available')
        
        return {
            "track_id":track_id_spotify,
            "track_name": track_name,
            "artist": artist,
            "album": album,
            "Duration":round(Duration/60000,2),
            "Genre":Genres,
            "Language":Language,
            "Release_date":release_date,
            "spotify_url": f"https://open.spotify.com/track/{spotify_url}" if spotify_url != "Not Available" else spotify_url,
            "youtube_url": f"https://www.youtube.com/watch?v={youtube_url}" if youtube_url != "Not Available" else youtube_url
        }
        
    else:
        return {"error": "No song identified"}
