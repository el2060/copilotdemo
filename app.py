import streamlit as st
import openai

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Streamlit app code
def main():
    st.title("YouTube Quiz Generator")

    # Input field for YouTube link
    youtube_link = st.text_input("Enter YouTube link")

    # Generate quiz questions
    if st.button("Generate Quiz"):
        if youtube_link:
            # Call OpenAI API to generate quiz questions
            quiz_questions = generate_quiz_questions(youtube_link)

            # Display the generated quiz questions
            for i, question in enumerate(quiz_questions):
                st.write(f"Question {i+1}: {question}")
        else:
            st.warning("Please enter a YouTube link")

# Function to generate quiz questions using OpenAI API
def generate_quiz_questions(youtube_link):
    # Call OpenAI API to generate quiz questions based on the YouTube link
    # You can customize the API call based on your requirements
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Generate three quiz questions based on the YouTube video: {youtube_link}",
        max_tokens=100,
        n=3,
        stop=None,
        temperature=0.7
    )

    # Extract the generated quiz questions from the API response
    quiz_questions = [choice["text"].strip() for choice in response.choices]

    return quiz_questions

if __name__ == "__main__":
    main()
