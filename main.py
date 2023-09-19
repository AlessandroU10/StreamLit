
#libraries
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import random
import string
import sys
from streamlit.web import cli as stcli
from streamlit import runtime

def main():
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Home", "passwords", "Contact"],
            icons=["house-fill", "pass-fill", "envelope"],
            menu_icon="browser-safari",
            default_index=0,
        )

    if selected == "Home":
        st.title('How I Started this website?')
        # Content
        c1, c2, c3, c4, c5, c6 = st.columns(6)
        c1.image(Image.open('images/github-icon-1.png'))
        c2.image(Image.open('images/pycharm-logo.png'))
        c3.image(Image.open('images/ucb-logo.png'))
        c4.image(Image.open('images/youtube-logo.png'))
        c5.image(Image.open('images/spotify-logo.png'))
        c6.image(Image.open('images/windows-logo.png'))

        st.write(
            """
            Greetings, everyone. My name is Alessandro, and I am currently studying Mechatronic Engineering at the Bolivian Catholic University.
            
            The main purpose of this application is to generate completely random passwords. To achieve this, we will employ various libraries 
            that include uppercase and lowercase letters, numbers, as well as special characters. In addition, there will be an option to customize the password, 
            which means you can choose the desired length for your password. You will also have the opportunity to create your own password 
            according to your preferences, with the only restriction being that the minimum allowed length is 5 characters.

            """
        )
        st.subheader('Methodology')
        st.write(
            """
            When the user selects the "Generate Passwords" option, the title "Password Generator" will be displayed. Next, the user will be 
            presented with two options: "Generate a Password" or "Create a New Password."

            If the user chooses "Generate a Password," a main function will be executed that will store strings of characters, including letters, 
            symbols, and digits, in a variable. A condition "if" will be applied where the length of the generated password must be less than 5 characters. 
            If this condition is met, no action will be taken, and a message indicating that the password must be longer than 5 characters will be displayed.

            If the user changes the length to a value greater than 5, an "else" condition will be triggered. Before evaluating the conditions, 
            a variable called "my_long_string" has been created, which contains the character library "string.ascii_letters + string.punctuation + string.digits." 
            Within the "else" condition, a new variable called "password" will be created. The ".join" method will be used on this new variable to combine 
            multiple random characters taken from the "my_long_string" variable. The number of characters selected will depend on the length specified by the user. 
            Finally, the newly generated password will be displayed on a specific button.

            If the user chooses the "Create a Password" option, two variables will be created as input types for the user to store their password. 
            If these two variables are identical, an "if" conditional will be activated, indicating that the passwords match, and they will be displayed. 
            However, if the entered passwords do not match, an "else" conditional will be activated, providing a message that the passwords do not match.
            """
        )
        st.markdown("![Alt Text](https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif)")

    if selected == "passwords":
        st.title('Generator of passwords')
        btn_state = st.checkbox('Do you want to generate your password?')
        if btn_state:
            def main():
                my_long_string = string.ascii_letters + string.punctuation + string.digits
                value = st.number_input('Enter the Password length ')
                value = int(value)

                if value < 5:
                    st.error('Password length must be greater than or equal to 5')
                else:
                    password = ''.join(random.choice(my_long_string) for i in range(value))
                    if st.button('Generate password'):
                        st.success('Password is {}'.format(password))
            main()
        else:
            st.title('Create a Password')
            password1 = st.text_input('Enter your password:', type='password')
            password2 = st.text_input('Re-enter your password:', type='password')

            match_button = st.button('Check Password')
            if password1 and password2:
                if match_button:
                    if password1 == password2:
                        st.success('Passwords match. Your password is: {}'.format(password1))
                    else:
                        st.warning('Passwords do not match. Please re-enter.')

        st.markdown("![Alt Text](https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif)")

    if selected == "Contact":
        st.title('Feedback')
        st.write(
            """
            I would appreciate feedback regarding the application. Any suggestions aimed at enhancing its appearance or code quality are welcome. 
            Constructive comments are also encouraged. If you require access to the implemented code, please feel free 
            to contact me through the provided contact information below. Additionally, you can clone my GitHub repository "streamlit" for examination.
            
            """
        )
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("![Alt Text](https://media.giphy.com/media/idljdFb6h52OwuoKhQ/giphy-downsized-large.gif)")
        with c2:
            st.markdown(" ")
        with c3:
            st.markdown(" ")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.info('**GitHub: [@AlessandroU10](https://github.com/AlessandroU10)**', icon="🦉")
        with c2:
            st.info('**Instagram: [@xAlessandroU21](https://www.instagram.com/xalessandrou21/)**', icon="🐧")
        with c3:
                st.info('**Snapchat: [@AlessandroU10](https://t.snapchat.com/ZnU8aSgs)**', icon="🦊")



if __name__ == "__main__":
    if runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
