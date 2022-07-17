# streamlit dependencies
import streamlit as st
# data dependencies
import pandas as pd
from PIL import Image

def data_professionals():
    st.info('Explained, Gathered, Analyzed & Unsupervised by The Dream Team')

    contact_form = """
    <form action="https://formsubmit.co/nyamathulani@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send mail</button>
    </form>
    """
    
    # define Github links for each team member
    link1 = "https://github.com/ThulaniNyama"
    link2 = "https://github.com/alnaschutte"
    link3 = "https://github.com/SiyandaMadlopha"
    link4 = "https://github.com/Shoki2"
    link5 = "https://github.com/ElelwaniTshikovhi"
    link6 = "https://github.com/SoulR95"
    dream_team = Image.open('./resources/imgs/dream_works.gif')
    # define Pandas data frame with team members that developed the models, and the app
    df = pd.DataFrame(
        {
            "The Dream Team": [
                f'<a target="_blank" href="{link1}">Thulani Nyama</a>',
                f'<a target="_blank" href="{link2}">Alna Scutte</a>',
                f'<a target="_blank" href="{link3}">Siyanda Mandlopha</a>',
                f'<a target="_blank" href="{link4}">Reshoketswe Makgamatha</a>',
                f'<a target="_blank" href="{link5}">Elelwani Tshikovhi</a>',
                f'<a target="_blank" href="{link6}">Riaan James-Verwey</a>'
            ],
            "Profession": ["Data Scientist", "Data Analyst", "Data Scientist", "Data Analyst", "Data Scientist", "Data Engineer"]
        }
        
    )
    
    contact, members, team, = st.columns([2, 2, 3])

    with contact:
        st.header(":mailbox: Get in touch with us!")
        st.markdown(contact_form, unsafe_allow_html=True)
        local_css("./utils/style.css")
    with members:
        st.image(dream_team, caption='')
    with team:
        st.write("")
        st.write("")
        st.write("")
        st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    # footer display image with caption 
    # image = Image.open('./resources/imgs/EDSA_logo.png')
    # st.image(image, caption='© The Dream Team', use_column_width=True)
    
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style >{f.read()}</style>", unsafe_allow_html=True)