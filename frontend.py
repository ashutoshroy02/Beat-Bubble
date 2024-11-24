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


def render_frontend():
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(html, unsafe_allow_html=True)
    st.markdown("<h1 style='color: white; animation: fadeIn 8s ease;'>BEAT BUBBLE</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>What if we don't know the name of a song but remember a tune?<br><strong>BEAT BUBBLE</strong> will find it for you!</p>", unsafe_allow_html=True)
