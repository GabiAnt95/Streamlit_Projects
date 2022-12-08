def user_page():
    import streamlit as st
    from manage_db import add_new_user, conn

    Actions = [None, 'Add New User', 'Delete User',]

    option = st.selectbox('', Actions)

    if option == None:
        st.title('Select an Action you want to execute: ')
    elif option == 'Add New User':
        user_name, password, mail = st.text_input("User_name: "), st.text_input("Password: "), st.text_input("Mail: ")
        st.button("Add New User", on_click = add_new_user(user_name, password, mail, conn))
    else:
        st.title('Under construction')

