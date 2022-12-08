from manage_db import create_connection
import streamlit_authenticator as stauth
from user_page import user_page

def login_sqlite():

    import streamlit as st
    import sqlite3
    import pandas as pd
    import hashlib

    def comprobacion(user, password, conn):
        password_query = pd.read_sql(f'''SELECT users.password FROM users WHERE users.user_name = "{user}"''', conn)['password'][0]
        if hashlib.sha512(password.encode('utf-8')).hexdigest() == password_query:
            st.header("Welcome!")
        else:
            st.header('Wrong Password or User')

    user = st.text_input('User: ')
    password = st.text_input('Password: ', type  = 'password')

    st.button('Login', on_click = lambda: comprobacion(user, password, create_connection('DataBase/db.sqlite')))



