import streamlit as st
import sqlite3
import hashlib
import pickle
import pandas as pd

# =================================================
# PAGE CONFIG (MUST BE FIRST)
# =================================================
st.set_page_config(
    page_title="Traffic Volume Prediction",
    layout="centered"
)

# =================================================
# DATABASE FUNCTIONS
# =================================================
def get_db():
    return sqlite3.connect("users.db")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def init_db():
    conn = get_db()
    cur = conn.cursor()

    # Create users table with role
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    """)

    # Create admin if not exists
    cur.execute("SELECT * FROM users WHERE username='admin'")
    if cur.fetchone() is None:
        cur.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            ("admin", hash_password("admin123"), "admin")
        )

    conn.commit()
    conn.close()

def register_user(username, password):
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, hash_password(password), "user")
        )
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT username, role FROM users WHERE username=? AND password=?",
        (username, hash_password(password))
    )
    user = cur.fetchone()
    conn.close()
    return user

def get_all_users():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, username, role FROM users")
    users = cur.fetchall()
    conn.close()
    return users

# =================================================
# INIT DATABASE
# =================================================
init_db()

# =================================================
# SESSION STATE
# =================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =================================================
# AUTH SECTION
# =================================================
if not st.session_state.logged_in:

    st.title("🔐 Login / Registration")

    tab1, tab2 = st.tabs(["Login", "Register"])

    # ---------------- LOGIN ----------------
    with tab1:
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):
            user = login_user(username, password)
            if user:
                st.session_state.logged_in = True
                st.session_state.username = user[0]
                st.session_state.role = user[1]
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    # ---------------- REGISTER ----------------
    with tab2:
        new_user = st.text_input("New Username", key="reg_user")
        new_pass = st.text_input("New Password", type="password", key="reg_pass")

        if st.button("Register"):
            if register_user(new_user, new_pass):
                st.success("Registration successful! Please login.")
            else:
                st.error("Username already exists")

# =================================================
# MAIN APP (AFTER LOGIN)
# =================================================
else:

    # ---------------- SIDEBAR ----------------
    st.sidebar.success(f"👤 {st.session_state.username}")
    st.sidebar.write(f"Role: **{st.session_state.role}**")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # ---------------- ADMIN PANEL ----------------
    if st.session_state.role == "admin":
        st.sidebar.markdown("### 👑 Admin Panel")

        if st.sidebar.button("View Registered Users"):
            users = get_all_users()
            df = pd.DataFrame(users, columns=["ID", "Username", "Role"])
            st.subheader("📋 Registered Users")
            st.dataframe(df)

    # =================================================
    # 🚦 TRAFFIC VOLUME PREDICTION APP
    # =================================================
    with open("traffic_pipeline.pkl", "rb") as f:
        pipeline = pickle.load(f)

    st.title("🚦 Traffic Volume Prediction")
    st.markdown("Enter traffic and weather details to **predict traffic volume**.")

    col1, col2 = st.columns(2)

    with col1:
        temp = st.number_input("Temperature (K)", value=300.0)
        rain = st.number_input("Rain (mm)", value=0.0)
        snow = st.number_input("Snow (mm)", value=0.0)
        month = st.number_input("Month", 1, 12, 6)
        day = st.number_input("Day", 1, 31, 15)
        hour = st.number_input("Hour", 0, 23, 12)

    with col2:
        minute = st.number_input("Minute", 0, 59, 0)
        second = st.number_input("Second", 0, 59, 0)
        weekday = st.number_input("Weekday (0=Mon, 6=Sun)", 0, 6, 2)
        rush = st.selectbox("Is Rush Hour?", [0, 1])
        weather = st.selectbox(
            "Weather",
            ["Clear", "Clouds", "Rain", "Snow",
             "Thunderstorm", "Drizzle", "Fog", "Mist"]
        )

    if st.button("🚦 Predict Traffic Volume"):
        try:
            sample_df = pd.DataFrame({
                "temp": [temp],
                "rain": [rain],
                "snow": [snow],
                "weather": [weather],
                "month": [month],
                "day": [day],
                "hour": [hour],
                "minute": [minute],
                "second": [second],
                "weekday": [weekday],
                "is_rush_hour": [rush]
            })

            prediction = pipeline.predict(sample_df)[0]
            st.success(f"🚦 Predicted Traffic Volume: **{int(prediction)}**")

        except Exception as e:
            st.error(f"❌ Prediction Error: {e}")
