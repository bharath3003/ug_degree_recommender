import streamlit as st
import pandas as pd

if 'Username' not in st.session_state:
    st.session_state["Username"] = ""

User1 = st.session_state['Username']

if User1 != "":
# Mock user data storage (replace with a database in a real-world application)
    user_data = pd.DataFrame(columns=['Field', 'Location', 'Selected College'])

    def load_data():
        data = pd.read_csv('C:/Users/User/Desktop/SE_PROJECT/SE_dataset.csv')  # Update the file path accordingly
        return data

    def filter_medical_data(data, neet_score):
        filtered_data = data[data['Field '] == 'Medical'].sort_values(by='NEET cut off', ascending=True)

        if neet_score < 381:
            st.write('No college available :(')
            return None
        elif 381 <= neet_score <= 720:
            filtered_data = filtered_data[filtered_data['NEET cut off'] <= neet_score]
            st.write('Available Colleges: ')
            st.write(filtered_data)

            # Find the college with the cutoff closest to the submitted score
            selected_college = min(filtered_data['University name '].unique(), key=lambda x: abs(filtered_data[filtered_data['University name '] == x]['NEET cut off'].values[0] - neet_score))

            # Retrieve the location associated with the selected college
            selected_location = filtered_data[filtered_data['University name '] == selected_college]['Location'].values[0]
            
            # Store user data (replace with database operations in a real-world application)
            user_data.loc[len(user_data)] = ['Medical', selected_location, selected_college]

            # Display the final selected college from the DataFrame
            st.write("Final Suggested College:")
            st.write(user_data.iloc[-1])
            
            return user_data.iloc[-1]
        else:
            st.write('Wrong input for NEET score.')
            return None

    def filter_engineering_data(data, branch, jee_score):
        if branch in data['Course'].unique():
            filtered_data = data[data['Course'] == branch].sort_values(by='JEE cut off', ascending=True)

            if jee_score < 100:
                filtered_data = filtered_data[filtered_data['JEE cut off'] <= jee_score]
                st.write('Available Colleges: ')
                st.write(filtered_data)
                if len(filtered_data) == 0:
                    st.write('No colleges available.')
                    return None
                else:
                    # Find the college with the cutoff closest to the submitted score
                    selected_college = min(filtered_data['University name '].unique(), key=lambda x: abs(filtered_data[filtered_data['University name '] == x]['JEE cut off'].values[0] - jee_score))
                    
                    # Retrieve the location associated with the selected college
                    selected_location = filtered_data[filtered_data['University name '] == selected_college]['Location'].values[0]

                    # Store user data (replace with database operations in a real-world application)
                    user_data.loc[len(user_data)] = ['Engineering', selected_location, selected_college]

                    # Display the final selected college from the DataFrame
                    st.write("Final Suggested College:")
                    st.write(user_data.iloc[-1])
                    
                    return user_data.iloc[-1]
            else:
                st.write('Wrong input for JEE score.')
                return None
        else:
            st.write('Wrong input for Course.')
            return None

    def main():
        st.title("Undergraduate College Recommender System")

        data = load_data()
        selected_data = None

        st.write("Select your field: Engineering, Medical")
        stream = st.selectbox("", ["Engineering", "Medical"])

        if stream == 'Medical':
            st.write("Provide Your NEET score:")
            neet_score = st.number_input("", min_value=0, max_value=720, step=1)

            # Add a "Submit" button to regenerate the final selected college
            if st.button("Submit"):
                selected_data = filter_medical_data(data, neet_score)
                # Display the final selected college from the DataFrame
                if selected_data is not None:
                    pass  # Do not show the DataFrame here
                    # You can add more columns as needed
        elif stream == 'Engineering':
            st.write("Select your Course: CS, MECH, CIVIL, ECE")
            branch = st.selectbox("", ["CS", "MECH", "CIVIL", "ECE"])

            st.subheader('Share your JEE score:')
            jee_score = st.number_input("", min_value=0.0, max_value=100.0, step=0.1)

            # Add a "Submit" button to regenerate the final selected college
            if st.button("Submit"):
                selected_data = filter_engineering_data(data, branch, jee_score)
                # Display the final selected college from the DataFrame
                if selected_data is not None:
                    pass  # Do not show the DataFrame here
                    # You can add more columns as needed

    if __name__ == "__main__":
        main()

else:
    st.warning("You need to log in to access this page.")