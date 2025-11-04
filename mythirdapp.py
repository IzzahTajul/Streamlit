import streamlit as st

# page setup
st.set_page_config(page_title='Colors and Layout', layout="wide")

st.title("Colors, Layout & Charts")
st.write("Let's Make Our App Beautiful and Organized")
st.write("Let's Make Our App Beautiful and Organized")
st.markdown(""" 
<div style="background-color:#E3E3A6;padding:20px;border-radius:10px;"> 
<h3 style="color:#451108">HTML Style Using Markdown</h3>
<p> This is HTML Paragraph Tag</p>
</div>
""",unsafe_allow_html=True)  #telling streamlit to trust the HTML content

#markdown
st.markdown("\n")
#display text in bold and italic
st.markdown("**Streamlit** is a python library for creating interactive *web apps*")
# links
st.markdown("Visit for more info:(https://streamlit.io/) *To Learn* **StreamLit**") 

code1 = '''def hello():
    print('Hi I am a Python Function')'''
st.code(code1,language="python")

# Latex() --> inputs mathetimatical formula 
st.latex('''
(a+b)^2 = a^2 + b^2 + 2*a*b
''')

st.markdown("\n")
st.markdown('**Sigmoid Function**')
st.latex(r'''
\frac {1}{1+e^-score}
''')

# Layouts

col1, col2 = st.columns(2)

with col1:
    st.header("Left Side")
    name = st.text_input('Enter Your Name?')
    st.write("😍 Hello User",name if name else "Guest")

with col2:
    st.header("Right SIde")
    age = st.slider("Pick A Number",1,100,25)
    st.write(f"Next Year You Will Become {age+1} Your Old 😺")

# A Sidebar is like a mini control panel the left side

with st.sidebar:
    st.header("Control Panel")
    user_color = st.color_picker("Pick Your Favourite Color","#000000")
    st.write("You Have Selected:",user_color)
