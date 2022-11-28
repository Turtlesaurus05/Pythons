import  requests
import streamlit as st
#Emojis https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Main Page", page_icon=":heart:", layout="wide")

st.title("Main page")
st.sidebar.success("Will be updated later...")
st.sidebar.header("""
My projects:

""")
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




