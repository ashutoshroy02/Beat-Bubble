import streamlit as st
from frontend import set_page_config, render_frontend, render_hero, render_instructions, render_result_card
from audio_utils import record_audio
from api_handler import identify_song

# set_page_config must be the first Streamlit command.
set_page_config()

def main():
    # Load background and CSS
    render_frontend()
    
    # Wrap main content in a central layout
    col1, col2, col3 = st.columns([1, 8, 1])
    
    with col2:
        render_hero()
        render_instructions()
        
        st.write("---")
        st.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>Record Audio</h3>", unsafe_allow_html=True)
        
        # Flex container for centered audio recorder using Streamlit columns
        subcol1, subcol2, subcol3 = st.columns([1, 2, 1])
        with subcol2:
            audio_file_path = record_audio()
        
        st.write("") # Spacing
        
        if audio_file_path:
            if st.button("Identify Song"):
                with st.spinner("Analyzing the beat..."):
                    song_details = identify_song(audio_file_path)
                    
                if "error" not in song_details:
                    st.balloons()
                    render_result_card(song_details)
                else:
                    st.error("Oops! " + song_details["error"])
        else:
            st.markdown("<div style='text-align: center; color: #aaa; margin-top: 15px;'>Waiting for you to record a song snippet... 🎵</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: center; margin-top: 50px; font-size: 0.9rem; color: #888;'>Built by Ashu & Sejal • <a href='https://buymeacoffee.com/ashu2003rof' style='color:#4facfe; text-decoration:none;'>Buy me a coffee ☕</a></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
