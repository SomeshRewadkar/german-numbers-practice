import streamlit as st
import random
from gtts import gTTS
import io

# Title of the app
st.title("Practice German Numbers: Listen & Guess! 🎧")

# Add a header
st.header("🔢 Enter a Range and Guess the Number")

# Create input fields for range selection
min_value = st.number_input("✏️ Enter minimum value:", min_value=0, max_value=9999, value=1)
max_value = st.number_input("✏️ Enter maximum value:", min_value=min_value + 1, max_value=10000, value=10000)

# Initialize session state for random number
if "random_number" not in st.session_state or "last_range" not in st.session_state:
    st.session_state.random_number = random.randint(min_value, max_value)
    st.session_state.last_range = (min_value, max_value)

# Function to generate a new random number
def generate_new_number():
    st.session_state.random_number = random.randint(min_value, max_value)
    st.success("🎉 A new random number has been generated!")

# Generate new number button
if st.button("🔄 Generate New Number"):
    generate_new_number()
    
# Speak the number button
if st.button("🔊 Speak the Number"):
    audio_bytes = speak_number(st.session_state.random_number)
    st.audio(audio_bytes, format="audio/mp3")

# Function to speak the random number in German
def speak_number(number):
    tts = gTTS(text=str(number), lang="de")
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes

# Check number button
if st.button("👀 Reveal Number"):
    st.write(f"🎲 The random number is: **{st.session_state.random_number}**")

# Instructions
st.write("### 📌 Instructions:")
st.markdown("""
1. **🎯 Enter a range** using the number inputs.  
2. **🔄 Click 'Generate New Number'** for a new number within the range.  
3. **🔊 Click 'Speak the Number'** to hear it in German.  
4. **👀 Click 'Reveal Number'** to see it.  
""")

# Links to GitHub and LinkedIn
st.write("### 🔗 Connect with Me:")
st.markdown("""
- 🐙 [GitHub](https://github.com/SomeshRewadkar)
- 💼 [LinkedIn](https://www.linkedin.com/in/somesh-rewadkar-61262a154/)
""")
