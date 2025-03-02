import os
from dotenv import load_dotenv
import streamlit as st
from video_transcribe.video import get_transcribed_text
from agent.autogen import get_agent_response_from_video



st.title("Ai powered Video Q&A System 🎥")  
st.subheader("Powered by GEMINI") 


video_dir = "videos"
if not os.path.exists(video_dir):
    os.makedirs(video_dir)


uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"])

global trsnscribed_text


if uploaded_file is not None:
    video_path = os.path.join(video_dir, uploaded_file.name)

    # Writing file to "videos" directory
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())


    st.video(video_path)

    trsnscribed_text=get_transcribed_text(video_path)
    #st.write(trsnscribed_text)


else:
    st.write("🤖 Plaese upload a video.")



if uploaded_file is not None:

    query = st.text_input("🔍 Enter your question about the video:")

    
    if st.button("Submit Query"):
        if query:
            chat_response=get_agent_response_from_video(trsnscribed_text,query)
            if chat_response and hasattr(chat_response, 'chat_history') and chat_response.chat_history:
                ai_reply = chat_response.chat_history[-1].get("content", "⚠️ No valid content received.")
                st.write(ai_reply)
            else:
                st.write("\n⚠️ No response received from the AI.")

        else:
            st.warning("⚠️ Please enter a query before submitting.")
