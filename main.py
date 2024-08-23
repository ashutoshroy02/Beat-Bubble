import json
import requests
from api_call import response


# Parse the JSON response
response_data = json.loads(response.text)   


try:
        music_info = response_data.get('metadata', {})
        if 'music' in music_info:
            music_info = music_info['music'][0]
        elif 'humming' in music_info:
            music_info = music_info['humming'][0]
        else:
            print("No music or humming data found.")
            music_info = None

        if music_info:
            track_name = music_info.get('title', 'Unknown Title')

            # Safely get artist details
            if 'spotify' in music_info.get('external_metadata', {}):
                spotify_artists = music_info['external_metadata']['spotify'].get('artists', [])
                artist = spotify_artists[0]['name'] if spotify_artists else 'Unknown Artist'
            else:
                artist = 'Unknown Artist'

            album = music_info.get('album', {}).get('name', 'Unknown Album')

            # Check for Spotify link
            if 'spotify' in music_info.get('external_metadata', {}):
                spotify_track_url = f"https://open.spotify.com/track/{music_info['external_metadata']['spotify']['track']['id']}"
            else:
                spotify_track_url = "Spotify link not available"

            # Check for YouTube link
            if 'youtube' in music_info.get('external_metadata', {}):
                youtube_video_url = f"https://www.youtube.com/watch?v={music_info['external_metadata']['youtube']['vid']}"
            else:
                youtube_video_url = "YouTube link not available"

            # Display the information
            print(f"Track Name: {track_name}")
            print(f"Artist: {artist}")
            print(f"Album: {album}")
            print(f"Spotify Track URL: {spotify_track_url}")
            print(f"YouTube Video URL: {youtube_video_url}")

except KeyError as e:
                print(f"KeyError: {e}. Check the structure of the response.")
