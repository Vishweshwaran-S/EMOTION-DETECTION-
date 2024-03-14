

import streamlit as st 
from textblob import TextBlob
from streamlit_extras.let_it_rain import rain

st.title("Sentiment Analysis App")

message = st.text_area("Please Enter your text")

if st.button("Analyze the Sentiment"):
    blob = TextBlob(message)
    result = blob.sentiment
    polarity = result.polarity
    subjectivity = result.subjectivity
    
    if polarity < 0:
        rain(
            emoji="💔",
            font_size=20,  
            falling_speed=3,  
            animation_length="infinite",  
        )
        st.image("https://emojicdn.elk.sh/😞", width=100)
    elif polarity > 0:
        rain(
            emoji="❤️",
            font_size=20,  
            falling_speed=3,  
            animation_length="infinite",  
        )
        st.image("https://emojicdn.elk.sh/😊", width=100)
    else:
        st.image("https://emojicdn.elk.sh/😐", width=100)

    st.success(result)

