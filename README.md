# 🧠 AI Virtual Personal Fitness Coach

An AI-powered personal fitness coach app built with Streamlit, MediaPipe, and OpenCV. This tool helps users improve their form while doing exercises like squats, pushups, and more — all in real-time using pose detection.

---

## 🚀 Features

- 💪 Real-time pose detection using MediaPipe
- 🔄 Rep counter for exercises (e.g., squats, pushups)
- 🧠 Intelligent feedback for posture correction
- 📊 Streamlit interface for smooth user interaction
- 🎯 Goal: Help users track fitness with minimal setup

---

## 🛠️ Installation

### 1. Clone this repo

```bash
git clone https://github.com/Aiswaryabinu/AI-virtual-personal-fitness-coach.git
cd AI-virtual-personal-fitness-coach
```

### 2. Create & activate virtual environment (recommended)

```bash
python -m venv fitnessenv
# Windows:
fitnessenv\Scripts\activate
# macOS/Linux:
source fitnessenv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Project Structure

```text
├── counter.py         # Exercise rep counter logic
├── detecter.py        # Pose detection & classification
├── fitnessapp.py      # Main Streamlit app file
├── pose_utils.py      # Helper functions for pose angles etc.
├── requirements.txt   # List of required Python packages
├── .gitignore
└── README.md
```

---

## ▶️ How to Run

```bash
streamlit run fitnessapp.py
```

---

## 🧠 Tech Stack

- Python
- Streamlit
- MediaPipe
- OpenCV
- NumPy

---

## 🤖 Future Ideas

- Add support for more exercises
- Real-time voice feedback
- Personalized workout plans
- Integration with wearables

---

## 🙋‍♀️ Author

**Aiswarya Binu**

GitHub: [@Aiswaryabinu](https://github.com/Aiswaryabinu)

---

## 📄 License

This project is licensed under the MIT License.
