import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from pose_utils import calculate_angle, count_reps
from datetime import datetime

st.set_page_config(page_title="AI Fitness Coach", layout="wide")

st.title("💪 AI Virtual Fitness Coach")
st.caption("Detects workout pose and counts reps in real-time.")

run = st.checkbox('Start Workout')
cam_feed = st.empty()
count_display = st.empty()
log_button = st.empty()

if run:
    counter = 0
    stage = None

    cap = cv2.VideoCapture(0)
    with mp.solutions.pose.Pose(min_detection_confidence=0.5,
                                min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark
                shoulder = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value].x,
                            landmarks[mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_ELBOW.value].x,
                         landmarks[mp.solutions.pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist = [landmarks[mp.solutions.pose.PoseLandmark.LEFT_WRIST.value].x,
                         landmarks[mp.solutions.pose.PoseLandmark.LEFT_WRIST.value].y]

                angle = calculate_angle(shoulder, elbow, wrist)
                counter, stage = count_reps(angle, counter, stage)

                cv2.putText(image, f'Reps: {counter}', (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3, cv2.LINE_AA)

            except:
                pass

            mp.solutions.drawing_utils.draw_landmarks(
                image, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)

            cam_feed.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), channels="RGB")

        cap.release()

    st.success(f"✅ Total reps completed: {counter}")

    if st.button("💾 Save Workout Log"):
        with open("workout_log.csv", "a") as f:
            f.write(f"{datetime.now()}, {counter} reps\n")
        st.success("Workout logged!")
