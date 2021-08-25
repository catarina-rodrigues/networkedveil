import streamlit as st
import text2emotion as te
from pythonosc.udp_client import SimpleUDPClient
import socket
# from pythonosc import udp_client
from pythonosc import osc_message_builder

# ip = "192.168.8.177"  # router IP
ip = "192.168.0.4"
port = 12345
client = SimpleUDPClient(ip, port)

# client = udp_client.UDPClient('ip', 12345)


st.set_page_config(page_title="Networked Veil",
                   layout="centered",
                   initial_sidebar_state="collapsed")

hide_streamlit_style = """
            <style>
                MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.caption('This is a space for collective remembering with care and respect - we are invited to honor those who have left the physical realm. Please take a moment to reflect before leaving a memory.')
st.title('Networked Veil')

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(170, 154, 115);
}
</style>""", unsafe_allow_html=True)


with st.form(key='textInput', clear_on_submit=True, ):
    message = st.text_input(
        label='Add a reflection (English-only messages please)')
    submit = st.form_submit_button(label='Share your memory')

emotion = ''

if submit:
    final_message = f'{message}'
    dict = te.get_emotion(final_message)
    st.write(dict)
    emotion = dict.values()
    print(emotion)

    # emotion = te.get_emotion(final_message)
    # st.write(emotion)
    # print(emotion)

    values = list(emotion)
    print(list(dict.values())[0])
    print(list(dict.values())[1])
    print(list(dict.values())[2])
    print(list(dict.values())[3])
    print(list(dict.values())[4])
    client.send_message("/message", final_message)
    client.send_message("/happy", list(dict.values())[0])
    client.send_message("/angry", list(dict.values())[1])
    client.send_message("/surprise", list(dict.values())[2])
    client.send_message("/sad", list(dict.values())[3])
    client.send_message("/fear", list(dict.values())[4])

    # msg = osc_message_builder.OscMessageBuilder(address='/happy')
    # msg.add_arg(values, arg_type='f')
    # # msg.add_arg(angry, arg_type='f')
    # # msg.add_arg(surprise, arg_type='f')
    # # msg.add_arg(sad, arg_type='f')
    # # msg.add_arg(fear, arg_type='f')
    # msg = msg.build()
    # client.send(msg)

# host_name = socket.gethostbyname(socket.gethostname())
# print(host_name)
