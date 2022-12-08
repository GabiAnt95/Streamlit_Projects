from resize_image import resize_page
from login_sqlite import login_sqlite
import streamlit as st
from streamlit_multipage import MultiPage

#app = MultiPage()
#app.st = st

#app.add_app("Resize Image", resize_page)
#app.add_app("Login", login_sqlite)

#app.run()

Utilities = [None, 'Resize Images', 'Split PDF', 'Split by Unique Values Excel', 'Login Sqlite']

option = st.selectbox('', Utilities)

if option == None:

    st.title('Select a Function from the Left List')
elif option == 'Resize Images':
    resize_page()
elif option == 'Login Sqlite':
    login_sqlite()
else:
    st.title('Under building')



