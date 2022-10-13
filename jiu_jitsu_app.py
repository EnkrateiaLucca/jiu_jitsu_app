import streamlit as st


st.header("Jiu Jitsu Analysis App")
# app with streamlit where you can search for a video, and the app will 
# show the videos as boxes in a layout where you can click and watch the video

st.subheader("Search for a video")
# search bar where you can search for a video
category = st.sidebar.selectbox("Select a video", options=["Takedowns", 
                                                           "Submissions",
                                                            "Guard Passes", 
                                                            "Sweeps",
                                                            "Escapes",
                                                            "Drills",
                                                            "Sneaky Moves",
                                                            "Cool Sparring"])
# sidebar with options to select a video
# display video in a box layout like in the pocket app
# when you click on a video, it will play the video

# with open("takedowns.txt", "r") as f:
#     takedowns = f.read().splitlines()
# FOR THE FUTURE WE WILL DO IT IMPORTING FROM A TEXT FILES WITH LINKS TO MOVES

col1, col2 = st.columns(2)

if category=="Takedowns":
    col1.video("https://www.youtube.com/watch?v=F60XQdZn298&ab_channel=FANATICWRESTLING")
    col1.video("https://www.youtube.com/watch?v=fnpTDTatJ2M")
    col1.video("https://www.youtube.com/watch?v=yLR5gyndzPs")
    col2.video("https://www.youtube.com/watch?v=Wn3zq5kv7jU")
    col2.video("https://www.youtube.com/watch?v=xagOTpxeliE")
    col2.video("https://www.youtube.com/watch?v=apTd4T7nQQE")

elif category=="Submissions":
    col1.video("https://www.youtube.com/watch?v=lEYtwschHBo")
    col2.video("https://www.youtube.com/watch?v=l8-JI7NND3E")

elif category=="Guard Passes":
    col1.video("https://www.youtube.com/watch?v=RQf5WZNLmEA")
    col2.video("https://www.youtube.com/watch?v=ZWVg6dzdmP8")

elif category=="Sweeps":
    col1.video("https://www.youtube.com/watch?v=y0C8vIeCrc0")
    col2.video("https://www.youtube.com/watch?v=BKX0OjWStzc")

elif category=="Escapes":
    col1.video("https://www.youtube.com/watch?v=3xEmPci_szw")
    col2.video("https://www.youtube.com/watch?v=OhKYNi0ql-0")

elif category=="Drills":
    col1.video("https://www.youtube.com/watch?v=KvSLdhrzqfE")
    col1.video("https://www.youtube.com/watch?v=9bd0t3CacBE")
    col2.video("https://www.youtube.com/watch?v=ePYW0X5Fa2g")
    col2.video("https://www.youtube.com/watch?v=r-ytZjcPhtA")
    

elif category=="Sneaky Moves":
    col1.video("https://www.youtube.com/watch?v=pDd0ltoMuM8")
    col2.video("https://www.youtube.com/watch?v=wO1kS8wmP2Y")

elif category=="Cool Sparring":
    col1.video("https://www.youtube.com/watch?v=RrhoX7Ws0RM")
    col2.video("")