## **Beat Bubble 🎶**
Beat Bubble is an AI-powered music identification app. It lets you find a song by singing, humming, or playing a snippet of music. With an engaging UI and powerful audio recognition backend, it's perfect for music enthusiasts who want to identify tracks effortlessly.

---

### **Features**
- 🎤 Record a song or hum a tune directly in the app.
- 🔍 Identify songs using advanced audio recognition (powered by ACRCloud API).
- 🎧 Get links to Spotify and YouTube for the identified tracks.
- 📜 View history of previously identified songs.

---

### **Project Structure**
```
beat_bubble/
│
├── main.py                    # Entry point of the app
├── frontend/
│   ├── layout.py              # CSS and HTML layout
│   ├── recorder.py            # Audio recording functionality
├── backend/
│   ├── api_handler.py         # ACRCloud API integration
│   ├── song_identifier.py     # Song identification logic
├── utils/
│   ├── history_manager.py     # Session state management
│   ├── audio_utils.py         # Utility functions for audio
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
```

---
### Live LINK :  https://beatbubblefind.streamlit.app 

### **Installation**

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/ashutoshroy02/SONG-IDENTIFICATION.git]
   cd beat_bubble
   ```

2. **Install Dependencies**
   Use the `requirements.txt` file to install all necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```

#. **Set Up ACRCloud API Credentials**
   - Sign up for an account on [ACRCloud](https://www.acrcloud.com/).
   - Create a new project and obtain your `Access Key` and `Access Secret`.
   - Update the `access_key` and `access_secret` in `backend/api_handler.py`.

---

### **Running the App**

1. Start the Streamlit app:
   ```bash
   streamlit run main.py
   ```

2. Open your web browser. The app will run on:
   ```
   http://localhost:8501
   ```

3. Use the app to:
   - Record your voice or upload a song snippet.
   - Identify the track, and get Spotify or YouTube links.

---

### **Usage**
1. 🎤 **Record Audio**: Click the microphone button and sing, hum, or play music for 10 seconds.
2. 🔍 **Identify the Song**: Press "Identify Song" to find the track details.
3. 📜 **View History**: Check the sidebar to see previously identified songs.

---

### **Requirements**
- Python 3.8+
- ACRCloud API Key
- Libraries: Streamlit, audio-recorder-streamlit, SciPy, Requests, NumPy

---

### **Contributing**
Contributions are welcome! If you’d like to improve the project:
1. Fork the repository.
2. Create a new branch: `
3. Commit your changes: `
4. Push the branch: `
5. Submit a pull request.

---

### **License**
This project is licensed under the MIT License.

---

### **Acknowledgments**
- [Streamlit](https://streamlit.io/) for an excellent framework for building UI.
- [ACRCloud](https://www.acrcloud.com/) for their powerful music recognition API.

```http
  https://console.acrcloud.com/ 
```
