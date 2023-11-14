import streamlit as st
import pandas as pd

# Function to add reviews and ratings to the dataset
def add_review_and_rating(college_name, review, rating, df):
    # Check if the college exists in the dataset
    if college_name in df['University name '].values:
        # Convert existing values to string to avoid NaN issues
        df['Reviews'] = df['Reviews'].astype(str)
        
        # Find the index of the row where the college matches
        index = df.index[df['University name '] == college_name].tolist()[0]
        
        # Add the review and rating to the dataset
        if pd.isna(df.at[index, 'Reviews']) or df.at[index, 'Reviews'].strip() == '':
            df.at[index, 'Reviews'] = review
        else:
            df.at[index, 'Reviews'] += '\n' + review

        # Handle both string and numpy float cases for 'Rating'
        existing_ratings = df.at[index, 'Rating']
        if pd.notna(existing_ratings):
            existing_ratings = [float(x) for x in str(existing_ratings).split() if x]
            existing_ratings.append(rating)
            avg_rating = sum(existing_ratings) / len(existing_ratings)
            df.at[index, 'Rating'] = avg_rating
        else:
            df.at[index, 'Rating'] = rating

        st.success(f"Review and Rating added successfully for {college_name}.")
    else:
        st.error(f"College '{college_name}' not found in the dataset.")

# Function to view reviews and ratings for a specific college
def view_reviews_and_rating(college_name, df):
    # Check if the college exists in the dataset
    if college_name in df['University name '].values:
        reviews = df.loc[df['University name '] == college_name, 'Reviews'].values[0]

        st.header(f"Reviews and Rating for {college_name}")

        if pd.notna(reviews) and reviews.strip() != '':  # Check if reviews are not NaN or empty
            reviews_list = reviews.split('\n')
            for i, review in enumerate(reviews_list[1:], start=1):  # Start enumeration from 1 and skip review 1
                st.info(f"Review {i}:")
                st.write(review)
        else:
            st.warning("No reviews available.")

        # Calculate and display the average rating
        ratings = df.loc[df['University name '] == college_name, 'Rating'].values[0]
        if pd.notna(ratings):
            st.info(f"Overall Rating: {ratings}")
        else:
            st.warning("No rating available.")

    else:
        st.error(f"College '{college_name}' not found in the dataset.")

# Load the dataset
dataset_path = 'C:/Users/User/Desktop/SE_PROJECT/SE_dataset.csv'
df = pd.read_csv(dataset_path)

# Add 'Reviews' and 'Rating' columns if they don't exist
if 'Reviews' not in df.columns:
    df['Reviews'] = ""
if 'Rating' not in df.columns:
    df['Rating'] = ""

# Check if user is authenticated
if 'authenticated' in st.session_state and st.session_state.authenticated:
    # Streamlit UI
    st.title("College Reviews Application")

    # Dropdown for user action
    selected_option = st.selectbox("Choose an action:", ["Add Review and Rating", "View Reviews"])

    # Add Reviews and Rating Section
    if selected_option == "Add Review and Rating":
        st.header("Add Review and Rating")
        college_name_add = st.selectbox("Select College:", df['University name '].unique())
        review_text = st.text_area("Enter Your Review:")
        rating = st.slider("Select Rating (1.0 to 10.0)", 1.0, 10.0, 5.0)
        add_review_button = st.button("Add Review and Rating", key="add_review_button")

        # Handle button click
        if add_review_button:
            add_review_and_rating(college_name_add, review_text, rating, df)

            # Update the CSV file with the new reviews and ratings
            df.to_csv(dataset_path, index=False)

    # View Reviews and Rating Section
    elif selected_option == "View Reviews":
        st.header("View Reviews")
        # Display a dropdown list of unique college names
        college_name_view = st.selectbox("Select College:", df['University name '].unique())
        view_reviews_button = st.button("View Reviews and Rating", key="view_reviews_button")

        # Handle button click
        if view_reviews_button:
            view_reviews_and_rating(college_name_view, df)
else:
    st.warning("You need to log in to access this page.")
