import cv2
import streamlit as st
import datetime

st.title("Time Stamped Camera")
start = st.button("Start Camera")

while start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        current_time = datetime.datetime.now()
        weekday = current_time.strftime("%A")
        hours_minutes_seconds = current_time.strftime("%H:%M:%S")

        cv2.putText(img=frame, text=weekday, org=(25, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 255, 255),
                    thickness=2, lineType=cv2.LINE_AA)

        cv2.putText(img=frame, text=hours_minutes_seconds, org=(25, 75),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 0, 0),
                    thickness=2, lineType=cv2.LINE_AA)
        streamlit_image.image(frame)
