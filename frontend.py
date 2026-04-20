import streamlit as st

def set_page_config():
    st.set_page_config(
        page_title="Beat Bubble",
        page_icon="🎶",
        layout="centered"
    )

css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

/* Hide Streamlit default elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main Body Background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2a5298);
    font-family: 'Outfit', sans-serif;
    color: #ffffff;
}

/* Ensure all text uses Outfit */
p, h1, h2, h3, span, div {
    font-family: 'Outfit', sans-serif !important;
}

/* Glassmorphism Container */
.glass-container {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 30px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    margin-bottom: 25px;
}

/* Typography styles */
.hero-title {
    font-size: 4.5rem;
    font-weight: 800;
    background: linear-gradient(to right, #00f2fe, #4facfe, #00f2fe);
    background-size: 200% auto;
    color: #000;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 3s linear infinite;
    text-align: center;
    margin-bottom: 0px;
    padding-bottom: 10px;
    line-height: 1.2;
}

@keyframes shine {
    to { background-position: 200% center; }
}

.hero-subtitle {
    font-size: 1.2rem;
    font-weight: 300;
    text-align: center;
    color: #cbd5e1;
    margin-top: 5px;
    margin-bottom: 30px;
}

/* Streamlit Button Styling */
div.stButton > button:first-child {
    background: linear-gradient(135deg, #FF416C, #FF4B2B) !important;
    color: white !important;
    border: none !important;
    padding: 12px 28px !important;
    font-size: 18px !important;
    font-weight: 600 !important;
    border-radius: 50px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(255, 65, 108, 0.4) !important;
    width: 100% !important;
}

div.stButton > button:first-child:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(255, 65, 108, 0.6) !important;
    background: linear-gradient(135deg, #FF4B2B, #FF416C) !important;
}

/* Animated circles in the background */
.bg-circle {
    position: fixed;
    border-radius: 50%;
    filter: blur(80px);
    z-index: -1;
    pointer-events: none;
}

.circle-1 {
    top: -10%;
    left: -10%;
    width: 500px;
    height: 500px;
    background: rgba(0, 242, 254, 0.2);
    animation: float 20s infinite alternate;
}

.circle-2 {
    bottom: -10%;
    right: -10%;
    width: 600px;
    height: 600px;
    background: rgba(255, 65, 108, 0.15);
    animation: float 25s infinite alternate-reverse;
}

@keyframes float {
    0% { transform: translate(0, 0) scale(1); }
    100% { transform: translate(50px, 50px) scale(1.1); }
}

/* Result Card */
.result-card {
    background: rgba(20, 20, 20, 0.5);
    border-radius: 15px;
    padding: 25px;
    display: flex;
    flex-direction: column;
    gap: 15px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    margin-top: 20px;
}

.result-header {
    display: flex;
    align-items: center;
    gap: 15px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 15px;
}

.disc-icon {
    font-size: 3rem;
    animation: spin 4s linear infinite;
}

@keyframes spin { 100% { transform: rotate(360deg); } }

.song-title {
    font-size: 2rem;
    font-weight: 800;
    margin: 0;
    color: #fff;
    line-height: 1.2;
}

.song-artist {
    font-size: 1.2rem;
    color: #aaa;
    margin: 0;
}

.meta-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    margin-top: 10px;
}

.meta-item {
    background: rgba(255,255,255,0.05);
    padding: 12px;
    border-radius: 10px;
}

.meta-label {
    font-size: 0.8rem;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.meta-value {
    font-size: 1.1rem;
    font-weight: 600;
    color: #fff;
}

.action-buttons {
    display: flex;
    gap: 15px;
    margin-top: 20px;
}

.link-btn {
    flex: 1;
    display: inline-block;
    text-align: center;
    padding: 10px 15px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.2s;
    color: white !important;
}

.spotify-btn {
    background-color: #1DB954;
}

.spotify-btn:hover {
    background-color: #1ed760;
}

.youtube-btn {
    background-color: #FF0000;
}

.youtube-btn:hover {
    background-color: #ff3333;
}

/* Instructions Step */
.instruction-step {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 15px;
    padding: 15px;
    background: rgba(255,255,255,0.03);
    border-radius: 12px;
    border-left: 4px solid #4facfe;
    transition: transform 0.2s;
}
.instruction-step:hover {
    transform: translateX(5px);
    background: rgba(255,255,255,0.05);
}

.step-icon {
    font-size: 1.8rem;
}

</style>
"""

html_bg = """
<div class="bg-circle circle-1"></div>
<div class="bg-circle circle-2"></div>
"""

def render_frontend():
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(html_bg, unsafe_allow_html=True)

def render_hero():
    st.markdown("""
        <h1 class="hero-title">Beat Bubble</h1>
        <p class="hero-subtitle">Can't remember the song? Record a snippet and let Beat Bubble find it instantly.</p>
    """, unsafe_allow_html=True)

def render_instructions():
    st.markdown("""
        <div class="glass-container">
            <h3 style="margin-top: 0;">How it works</h3>
            <div class="instruction-step">
                <div class="step-icon">🎙️</div>
                <div>Click the microphone icon and record 7-8 seconds of the song.</div>
            </div>
            <div class="instruction-step">
                <div class="step-icon">🎧</div>
                <div>Review your recording to make sure it sounds clear.</div>
            </div>
            <div class="instruction-step">
                <div class="step-icon">✨</div>
                <div>Click <b>Identify Song</b> and let the magic happen!</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_result_card(details):
    # Ensure variables don't break HTML parsing
    spotify = details.get('spotify_url', '#')
    youtube = details.get('youtube_url', '#')
    
    spotify_html = f'<a href="{spotify}" target="_blank" class="link-btn spotify-btn">Spotify</a>' if spotify and spotify != "Not Available" else ''
    youtube_html = f'<a href="{youtube}" target="_blank" class="link-btn youtube-btn">YouTube</a>' if youtube and youtube != "Not Available" else ''
    
    html = f"""
    <div class="result-card">
        <div class="result-header">
            <div class="disc-icon">💿</div>
            <div>
                <h2 class="song-title">{details.get('track_name', 'Unknown Song')}</h2>
                <h3 class="song-artist">{details.get('artist', 'Unknown Artist')}</h3>
            </div>
        </div>
        
        <div class="meta-grid">
            <div class="meta-item">
                <div class="meta-label">Genre</div>
                <div class="meta-value">{details.get('Genre', '-')}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Duration</div>
                <div class="meta-value">{details.get('Duration', '-')} min</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Release Date</div>
                <div class="meta-value">{details.get('Release_date', '-')}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Language</div>
                <div class="meta-value">{details.get('Language', '-')}</div>
            </div>
        </div>
        
        <div class="action-buttons">
            {spotify_html}
            {youtube_html}
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
