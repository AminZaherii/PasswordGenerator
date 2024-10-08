# import requirements
import streamlit as st


from Password import *
import config


def generate_password():
    if password_type == config.TYPE_COMPLICATED_PASSWORD:
        password = complicated_password.generate()
    elif password_type == config.TYPE_PINCODE:
        password = pincode.generate()
    else:
        if 'password' not in st.session_state:
            password = ''
        else:
            password = st.session_state.password

    return password

def click_generate():
    if 'password' in st.session_state and password_type == config.TYPE_CUSTOM_PASSWORD:
        if complicated_password.validate(st.session_state.password):
            result = ':green[password is strong]'
        else:
            result = ':red[password is week]'
    else:
        result = ''
    st.write(result)
    del st.session_state.password

# create object from class PinCode
pincode = PinCode(length=config.MIN_LENGTH_PASSWORD)

# create object from class ComplicatedPassword
complicated_password = ComplicatedPassword(length=config.MIN_LENGTH_PASSWORD)

# show image as header
st.image('.\media\images\Password-generator-image.jpg')


# create slider for select length of password
length_slider = st.slider(label=':blue[please select length of password]',
                          min_value=config.MIN_LENGTH_PASSWORD,
                          max_value=config.MAX_LENGTH_PASSWORD,
                          step=config.STEP_LENGTH)



# generate password according to selected length and show in text input
pincode.set_length(length=length_slider)
complicated_password.set_length(length=length_slider)

password_type = st.selectbox(label=':blue[please select password type]', options=(config.TYPE_PINCODE, config.TYPE_COMPLICATED_PASSWORD,config.TYPE_CUSTOM_PASSWORD))
password_text_input = st.text_input(label=":blue[Password]", value=generate_password() , key='password')

generate_pincode_button = st.button(label='Generate',on_click=click_generate())
