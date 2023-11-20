import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
from streamlit_option_menu import option_menu
import time

st.set_page_config("Learn","🔍","wide")



def load_lottieurl(url):
        r=requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/snowflake.css")

animation_symbol = "❄"

st.markdown(f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
     """,
    unsafe_allow_html=True
    )

def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
delete = st.empty()
local_css("style/style.css")
a=1

if "page" not in st.session_state:
    st.session_state.page = 0

def nextpage(): st.session_state.page += 1
def restart(): st.session_state.page = 0

placeholder = st.empty()
a=0
if st.session_state.page == 0:
  with placeholder.container():
        lottie0 = load_lottieurl("https://lottie.host/a5e65d67-dd32-4131-9912-810704bfcc45/GlWoA3u0aM.json")
        st.header("***Write your name here :-***")
        Name = st.text_input("Name",label_visibility = "collapsed")
        if st.button("Done", type="primary"):
            if len(Name) == 0:
                    st.error('Please enter your name', icon="🚨")
            elif len(Name) == 1 or len(Name)== 2:
                    st.warning('Enter a proper name', icon="⚠️")
            elif Name.isalpha() == False:
                    st.warning('Enter alphabets only', icon="⚠️")
            else:
                nextpage()
                st.toast('If the button work in one click', icon='🐍')
                st.toast('then please try to click it 2-3 times', icon='🐍')
        st_lottie(lottie0,height = 400,key="L0")


elif st.session_state.page == 1:
  with placeholder.container():
    lottie1 = load_lottieurl("https://lottie.host/9c0a47c9-c2dc-46fa-b659-f757f6f9e89d/LMJzQ5CeeO.json")
    st.success('Your name is succesfully registered!', icon="✅")
    st_lottie(lottie1,height=400,key="L1")
    time.sleep(5)
    st.toast('Click on "Click me" button', icon='🐍')
    if st.button("Click me",on_click=nextpage):
        st.toast('If the button work in one click', icon='🐍')
        st.toast('then please try to click it 2-3 times', icon='🐍')
    
    
    
    
elif st.session_state.page == 2:
    selected = option_menu(
            menu_title=None,
            options=["Home","Modules","Contact"],
            icons=["house","book","envelope"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                    "container": {"padding": "0!important", "background-color": "#fafafa"},
                    "icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {
                        "font-size": "25px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#eee",
                    },
                    "nav-link-selected": {"background-color": "green"},
                }
            )
    
    if selected == "Home":
        lottie2 = load_lottieurl("https://lottie.host/5b2b8d7f-f156-4914-895f-efa111e70c4e/YD7OEcWBPG.json")
        st.info('If you are using it in the phone then please rotate your phone to get better experience', icon="ℹ️")

        with st.container():
                left_column,right_column = st.columns((2,1))
                with left_column:
                    st.title("Welcome to coding learner software :wave:")
                    st.divider()
                    
                    st.subheader("***Hello everyone***")  
                    st.write("###")        
                    st.subheader("***I have created a website to get the codes of some modules that I like***")  
                    st.write("###")
                    st.subheader("***So lets get stared!!***")  
                    
                with right_column:
                    st_lottie(lottie2,height=400,key="L2")
            
            
    if selected =="Modules":
        st.balloons()
        lottie3 = load_lottieurl("https://lottie.host/d363df57-589a-4abe-af07-a0c331060b2b/hLxts5Ulen.json")
        with st.container():
            left_column,right_column = st.columns((2,1))
            with left_column:
                st.title("Project 📜")
                st.divider()
                st.subheader("🟡 ***:red[Here are some modules below]***")
                "###"
                st.subheader("🟡 ***:red[Click on the button to know about them A to Z]***")
                "###"
                st.subheader("🟡 ***:red[In future there will be more modules]***")
                "###"
                st.subheader("🟡 ***:red[Make a great use of these]***")
                "###"
                "---"
                st.header(":black[Here is the list of different modules 📃]")
                "###"
                
                st.link_button("Turtle", "https://docs.python.org/3/library/turtle.html#methods-of-rawturtle-turtle-and-corresponding-functions")
                st.link_button("Streamlit", "https://docs.streamlit.io/library/get-started")
            with right_column:
                st_lottie(lottie3,height=500,key="L3")


    if selected =="Contact":
        st.snow()
        lottie4 = load_lottieurl("https://lottie.host/592c3d29-6205-48de-b316-0c15ae3562b0/PCtnM9bTk4.json")
        with st.container():
            st.write("---")
            st.header("Get in touch with me!!")
            st.write("##")

            contact_form = """
            <form action="https://formsubmit.co/manthanrauthan1@email.com" method="POST">
                 <input type="hidden" name="_recaptcha" value="false">
                 <input type="text" name="name" placeholder = "Your name" required>
                 <input type="email" name="email" placeholder = "Your email address" required>
                 <textarea name ="message" placeholder = "Your message here" required></textarea>
                 <button type="submit">Send</button>
            </form>
            """
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st_lottie(lottie4,height=400,key="L4")
                
            

