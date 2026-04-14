# 🚦 Intelligent Traffic Monitoring And Analysis System using AI Techniques
### Machine Learning + Authentication Based Web Application

---

## 📌 Project Overview

The Intelligent Traffic Volume Prediction System is a Machine Learning based web application that predicts traffic volume using the Random Forest Regressor algorithm.

This project integrates:

- 🔐 Login & Registration System
- 👑 Admin Panel
- 🗄 SQLite Database
- 🔒 Secure Password Hashing (SHA-256)
- 🌐 Streamlit Web Interface
- 🤖 Machine Learning Model Deployment

This is a complete end-to-end ML + Full Stack Python project.

---

## 🎯 Objectives

- Predict traffic volume using historical data
- Implement Random Forest regression model
- Build secure authentication system
- Integrate database for user management
- Deploy ML model using Streamlit

---

## 🧠 Machine Learning Model

### Algorithm Used:
Random Forest Regressor

### Input Features:

- Temperature (K)
- Rain (mm)
- Snow (mm)
- Weather
- Month
- Day
- Hour
- Minute
- Second
- Weekday (0=Mon, 6=Sun)
- Is Rush Hour (0/1)

### Output:
Predicted Traffic Volume (Integer Value)

---

## 🔐 Authentication System

### Features:

- User Registration
- User Login
- Role-Based Access (Admin / User)
- SHA-256 Password Hashing
- SQLite Database Storage

### Default Admin Credentials:

Username: admin  
Password: admin123  

---

## 👑 Admin Panel

Admin can:

- View all registered users
- See user roles
- Monitor system users

---

## 🗄 Database

Database: SQLite  
File: users.db  

Stores:
- User ID
- Username
- Encrypted Password
- Role

---

## 🛠 Tech Stack

Backend:
- Python
- Scikit-learn
- Pandas
- NumPy
- SQLite3
- Pickle

Frontend:
- Streamlit

Security:
- hashlib (SHA-256)

---

## 📂 Project Structure

```
Intelligent-Traffic-Volume-Prediction-By-using-ML
│
├── app.py
├── traffic_pipeline.pkl
├── traffic volume.csv
├── users.db
├── login.png
├── register.png
├── prediction.png
├── arch.png
├── class.png
├── dfd.png
├── sequence.png
└── README.md
```

---

## ▶️ How to Run the Project

### Step 1: Clone Repository

```
git clone https://github.com/your-username/Intelligent-Traffic-Volume-Prediction-By-using-ML.git
cd Intelligent-Traffic-Volume-Prediction-By-using-ML
```

### Step 2: Install Dependencies

```
pip install streamlit pandas numpy scikit-learn
```

### Step 3: Run Application

```
streamlit run app.py
```

---

## 🚦 Application Workflow

1. User registers or logs in
2. Admin can view registered users
3. User enters traffic & weather details
4. System processes input
5. Random Forest model predicts traffic volume
6. Result displayed on screen

---

# 📸 Application Screenshots

## 🔐 Login Page
<img width="1026" height="538" alt="image" src="https://github.com/user-attachments/assets/d93a7cdf-2ebb-4e75-bd20-412109b977d6" />


---

## 📝 Registration Page

<img width="952" height="581" alt="image" src="https://github.com/user-attachments/assets/bc4e789a-3b68-4a5a-a1ae-36cdfcd8fe7b" />


---

## 🚦 Traffic Prediction Page

![Prediction Page](prediction.png)<img width="1127" height="875" alt="image" src="https://github.com/user-attachments/assets/bf2c3d3a-5b48-4824-9575-253fff914941" />


---

## 📊 Sample Output

🚦 Predicted Traffic Volume: 4897

<img width="1054" height="748" alt="image" src="https://github.com/user-attachments/assets/ac4d6c5b-b031-48b1-b959-f5970af8ed05" />

---

## 🚀 Future Enhancements

- Add password strength validation
- Add user deletion (Admin control)
- Deploy on Streamlit Cloud
- Add graphical visualization
- Compare multiple ML models

---

## 🎓 Academic & Technical Highlights

✔ Machine Learning Model Deployment  
✔ Authentication System Implementation  
✔ Role-Based Access Control  
✔ Database Integration  
✔ Secure Password Encryption  
✔ Real-world Traffic Prediction System  

---

## 👩‍💻 Author

Gouri Priya  
B.Tech (4th Year)  
Machine Learning Enthusiast  
Cyber Security & Forensics Aspirant  

---
