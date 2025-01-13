import streamlit as st
import pandas as pd

# Task 1: Initialize Session State for storing student data
if "students" not in st.session_state:
    st.session_state.students = []  # Initialize as an empty list

# Title
st.title("Student Tracker")

# Section: Adding Student Data
st.header("Add Student")
name = st.text_input("Enter Student Name:")
score = st.number_input("Enter Score:", min_value=0, max_value=100, step=1)

if st.button("Add Student"):
    if name.strip() == "":
        st.error("Student name cannot be empty.")
    else:
        # Add student data to session state
        st.session_state.students.append({"Name": name, "Score": score})
        st.success(f"Student '{name}' with score {score} added!")

# Task 2: Displaying and Filtering Student Data
if st.session_state.students:
    st.header("Student Data")
    
    # Convert session state data to a DataFrame
    df = pd.DataFrame(st.session_state.students)
    
    # Display the DataFrame
    st.write("All Students:")
    st.dataframe(df)

    # Filtering based on minimum score
    st.subheader("Filter Students by Minimum Score")
    min_score = st.slider("Select Minimum Score", min_value=0, max_value=100, value=50, step=1)
    
    # Filter DataFrame
    filtered_df = df[df["Score"] >= min_score]
    st.write(f"Students with scores >= {min_score}:")
    st.dataframe(filtered_df)
else:
    st.info("No students have been added yet.")
