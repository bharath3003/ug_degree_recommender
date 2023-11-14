import streamlit as st

if 'Username' not in st.session_state:
    st.session_state["Username"] = ""

User1 = st.session_state['Username']

if User1 != "":
    def engineering_recommender(answers):
        # Calculate scores for each branch based on answers
        scores = {
            'Computer Science': answers.count('a') + answers.count('b'),
            'Electronics and Communication': answers.count('b') + answers.count('c'),
            'Mechanical': answers.count('c') + answers.count('d'),
            'Civil': answers.count('d') + answers.count('a')
        }

        # Determine the branch with the highest score
        recommended_branch = max(scores, key=scores.get)

        return recommended_branch

    def main():
        st.title("Undergraduate Engineering Branch Recommender")

        # Questions and their corresponding choices
        questions = [
            "When faced with a challenging problem, you are more likely to:",
            "When you come across a common issue, your instinct is to:",
            "Given the choice, you would rather:",
            "In a group project, you are most likely to:",
            "When presented with a complex electronic circuit, you would:",
            "If you were to work on a project addressing environmental issues, you would:",
            "When presented with architectural blueprints, you are more likely to:"
        ]

        choices = [
            ['Break it down logically and analyze each part.', 'Seek advice from others to gather diverse perspectives.',
            'Experiment with different approaches to find a solution.', 'Approach it from a practical standpoint.'],
            ['Find established solutions that have worked before.', 'Collaborate with others to brainstorm new ideas.',
            'Experiment with alternative solutions.', 'Analyze the problem to find the root cause.'],
            ['Analyze and optimize existing systems.', 'Collaborate with a diverse team on a challenging project.',
            'Design new solutions from scratch.', 'Implement practical solutions to real-world problems.'],
            ['Independently contribute your specialized skills.', 'Communicate openly and listen to others\' ideas.',
            'Act as a hands-on contributor to the project.', 'Focus on the overall project goals.'],
            ['Analyze its components and functionality.', 'Collaborate with others to improve the design.',
            'Experiment with different circuit configurations.', 'Focus on the practical implementation of the circuit.'],
            ['Research existing solutions and their impacts.', 'Collaborate with a team to devise innovative solutions.',
            'Experiment with sustainable technologies.', 'Focus on implementing practical measures.'],
            ['Analyze the theoretical aspects of the design.', 'Discuss potential improvements with the team.',
            'Experiment with innovative architectural concepts.', 'Focus on the practical aspects of construction.']
        ]

        # Store user responses
        user_responses = []

        # Ask questions and get responses
        for i, question in enumerate(questions):
            st.subheader(f"Question {i + 1}: {question}")
            user_response = st.radio("Choose the option that best describes you:", choices[i], key=i)
            user_responses.append(user_response[0].lower())

        # Recommend the engineering branch
        if st.button("Get Recommendation"):
            recommended_branch = engineering_recommender(user_responses)
            st.success(f"Based on your responses, the recommended branch for you is: **{recommended_branch} Engineering**")

    if __name__ == "__main__":
        main()

else:
    st.warning("You need to log in to access this page.")