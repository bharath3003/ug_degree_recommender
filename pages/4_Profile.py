import streamlit as st
import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="myappdb"
        )
        return connection
    except Error as e:
        st.error(f"Error: {e}")
        return None

def update_user_info(username, email, age, grade_12_score, jee_score, neet_score, phone, gender, password, about, new_password_updation=False):
    connection = connect_to_database()
    cursor = connection.cursor()

    # Call the stored procedure with the provided parameters
    cursor.callproc("UpdateUserInfo", (username, email, age, grade_12_score, jee_score, neet_score, phone, gender, password, about))  

    # Commit the changes
    connection.commit()

    cursor.close()
    connection.close()
    st.success("User information updated successfully.")


def display_user_prof(User1, user_info):
    st.text(f"Username: {User1}")

    # Check if user_info has enough elements
    if len(user_info) < 10:
        st.warning("Invalid user_info tuple length.")
        return

    email = st.text_input('Email', user_info[1])
    age = st.number_input('Age', min_value=float(0), value=float(user_info[2]))
    grade_12_score = st.number_input('Grade 12 Score', min_value=float(0.0), value=float(user_info[3]))
    jee_score = st.number_input('JEE Score', min_value=float(0.0), value=float(user_info[4]), key='jee_score')

    # Check if neet_score is None
    neet_score_default = 0.0 if user_info[5] is None else float(user_info[5])
    neet_score = st.number_input('NEET Score', min_value=float(0), value=neet_score_default, key='neet_score')

    phone = st.text_input('Phone', user_info[6])

    st.text(f"Gender: {user_info[7]}")
    gender_options = ["Male", "Female", "Prefer not to say"]
    gender = st.radio(f'Gender: {user_info[7]}', options=gender_options, index=gender_options.index(user_info[7]), key='gender')

    password = st.text_input('Password', user_info[8], type="password")
    password2 = st.text_input('Password Confirmation', user_info[8], type="password")

    # Check if user_info has enough elements for 'about'
    if len(user_info) >= 10:
        about = st.text_input('About', user_info[9])
    else:
        about = st.text_input('About')

    if st.button('Update Profile'):
        if password != user_info[8]:
            if password != password2:
                st.warning("New Passwords do not match")
            else:
                update_user_info(User1, email, age, grade_12_score, jee_score, neet_score, phone, gender, password, about, new_password_updation=True)
        else:
            update_user_info(User1, email, age, grade_12_score, jee_score, neet_score, phone, gender, password, about, new_password_updation=False)




def ProfilePage(User1):
    st.subheader(f"Hey, {User1}, feel like changing your profile?")
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{User1}'")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    display_user_prof(User1,result[0])
            


# Check if the user is logged in
if 'Username' not in st.session_state:
    st.session_state["Username"] = ""

User1 = st.session_state['Username']

if User1 != "":
    ProfilePage(User1)

else:
    st.warning("You need to log in to access this page.")