import streamlit as st

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        st.write("Bahebeeeeeek!")
        display_gif("./4760029_5e4d5.gif")
        # Your main app code goes here
    else:
        password_protect()

def password_protect():
    password = st.text_input("Enter the password:", type="password")
    if st.button("Login"):
        if password == st.secrets["PASSWORD"]:  # Use the password from Streamlit secrets
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Incorrect password")

def display_gif(gif_path):
    st.image(gif_path)

if __name__ == "__main__":
    main()