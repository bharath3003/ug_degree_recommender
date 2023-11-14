import streamlit as st

def main():
    st.title("Undergraduate Degree Recommender System")

    st.markdown(
        "Welcome to the Undergraduate Degree Recommender System. This system is designed to assist students "
        "in finding the most suitable undergraduate degree programs based on their interests, academic qualifications, and career goals."
    )

    st.header("Key Features")

    st.markdown(
        "- Personalized Recommendations: Get degree recommendations tailored to your interests and qualifications."
    )
    st.markdown(
        "- Easy to Use: Simple and user-friendly interface to help you discover the right degree for you."
    )
    st.markdown(
        "- Diverse Programs: Explore a wide range of undergraduate degrees available in the Indian education system."
    )
    st.markdown(
        "- Career-Oriented: Find degrees that align with your career goals and aspirations."
    )

    st.header("How to Use")

    st.markdown(
        "1. Begin by exploring the list of available undergraduate degree programs in the 'Find Degrees' section."
    )
    st.markdown(
        "2. For personalized recommendations, provide information about your interests and academic qualifications in the 'Update Profile' section."
    )
    st.markdown(
        "3. Review colleges and degree programs in the 'Review Colleges' section to help other students make informed choices."
    )

if __name__ == "__main__":
    main()
