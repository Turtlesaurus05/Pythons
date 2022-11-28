from PIL import Image
import  requests
import streamlit as st
from streamlit_lottie import st_lottie
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
#Emojis https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="MyWebpage", page_icon=":pray:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return none
    return r.json()

#Assets
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_zSGy1w.json")
img_contact_form = Image.open("Images/Randompassgen.PNG")

#Header section
with st.container():
    st.subheader("Hello, I am Joonatan :wave:")
    st.title("Software engineer student from Finland")
    st.write("I am excited to learn more python and also game development using unity!")
    st.write("[Here is a link to my github >] (https://github.com/Turtlesaurus05/Pythons)")




#what i do section
with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What i do")
        st.write("##")
        st.write("""
        - I am currenlty studying python at home to improve on it alot! And this is my second official python project!
        - Skills i have in coding : I can use a bit of C#, SQL, Javascript, HTML and also Python!
        - I am a second year student at Careeria and i am studying to be a software engineer.        
        """)

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

        with st.container():
            st.write("---")
            st.header("My Projects")
            st.write("##")
            st.subheader("Random password generator")
            st.write("Simply just enter how long you want the password to be and after that you enter how many passwords you would like!")
            st.write("https://github.com/Turtlesaurus05/Pythons/blob/master/Passgen.py")
            st.subheader("Alexa 2.0")
            st.write("We all know Alexa the expensive amazon ai. Well i made my own Alexa for absolutely free! Want it to play a song from youtube? No problem just say 'Alexa play Ariana grande'")
            st.write("https://github.com/Turtlesaurus05/Pythons/blob/master/MyAlexa.py")


