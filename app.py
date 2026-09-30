import streamlit as st
import time


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="College Student Portal",
    page_icon="🎓",
    layout="wide"
)


# --------------------------------------------------
# OPENING ANIMATION
# --------------------------------------------------

if "started" not in st.session_state:

    st.session_state.started = True

    progress = st.progress(0)

    message = st.empty()

    message.title("🎓 College Student Portal")
    message.write("Loading your campus...")

    for i in range(101):
        progress.progress(i)
        time.sleep(0.01)

    message.success("Campus loaded successfully!")
    time.sleep(0.8)

    progress.empty()
    message.empty()


# --------------------------------------------------
# MAIN TITLE
# --------------------------------------------------

st.title("🎓 College Student Portal")

st.subheader("Learn • Manage • Track • Grow")

st.write(
    "Welcome to your digital college campus. "
    "Manage attendance, assignments, timetable, results, notices and fees."
)

st.divider()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🎓 Student Portal")

st.sidebar.write("Choose an application")

page = st.sidebar.selectbox(
    "Applications",
    [
        "🏠 Home",
        "📊 Attendance",
        "📝 Assignments",
        "🗓️ Timetable",
        "📈 Results",
        "📢 Notices",
        "💰 Fees",
        "👤 Student Profile"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "💡 Use the menu above to access different college applications."
)


# ==================================================
# HOME
# ==================================================

if page == "🏠 Home":

    st.header("🏫 Welcome to Your College")

    st.info(
        "Smart Digital Campus - Manage your college activities from one place."
    )

    st.divider()

    st.subheader("🚀 Student Applications")

    # First row
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("📊 Attendance")
        st.write(
            "Track your subject-wise attendance "
            "and stay updated."
        )

        if st.button(
            "Open Attendance",
            key="home_attendance"
        ):
            st.info("Select 📊 Attendance from the sidebar.")

    with col2:
        st.subheader("📝 Assignments")
        st.write(
            "View assignments and "
            "pending submissions."
        )

        if st.button(
            "Open Assignments",
            key="home_assignments"
        ):
            st.info("Select 📝 Assignments from the sidebar.")

    with col3:
        st.subheader("🗓️ Timetable")
        st.write(
            "Check your daily classes "
            "and upcoming lectures."
        )

        if st.button(
            "Open Timetable",
            key="home_timetable"
        ):
            st.info("Select 🗓️ Timetable from the sidebar.")

    st.write("")

    # Second row
    col4, col5, col6 = st.columns(3)

    with col4:
        st.subheader("📈 Results")
        st.write(
            "Check your examination "
            "marks and academic performance."
        )

        if st.button(
            "Open Results",
            key="home_results"
        ):
            st.info("Select 📈 Results from the sidebar.")

    with col5:
        st.subheader("📢 Notices")
        st.write(
            "Read important college "
            "announcements."
        )

        if st.button(
            "Open Notices",
            key="home_notices"
        ):
            st.info("Select 📢 Notices from the sidebar.")

    with col6:
        st.subheader("💰 Fees")
        st.write(
            "Check your total fees, "
            "paid amount and pending amount."
        )

        if st.button(
            "Open Fees",
            key="home_fees"
        ):
            st.info("Select 💰 Fees from the sidebar.")

    st.divider()

    st.subheader("📌 Quick Information")

    info1, info2, info3, info4 = st.columns(4)

    with info1:
        st.metric(
            "Attendance",
            "84%"
        )

    with info2:
        st.metric(
            "Assignments",
            "5"
        )

    with info3:
        st.metric(
            "CGPA",
            "8.6"
        )

    with info4:
        st.metric(
            "Pending Fees",
            "₹15,000"
        )


# ==================================================
# ATTENDANCE
# ==================================================

elif page == "📊 Attendance":

    st.header("📊 Attendance")

    st.write(
        "View your subject-wise attendance."
    )

    st.divider()

    subjects = {
        "Python": 88,
        "DBMS": 82,
        "Java": 76,
        "Computer Networks": 91,
        "Machine Learning": 85
    }

    for subject, percentage in subjects.items():

        st.subheader(subject)

        st.progress(percentage / 100)

        st.write(
            "Attendance: "
            + str(percentage)
            + "%"
        )

        if percentage < 75:

            st.warning(
                "⚠️ Attendance is below 75%."
            )

        elif percentage < 80:

            st.info(
                "Keep attending classes regularly."
            )

        else:

            st.success(
                "✅ Attendance is good."
            )

        st.divider()


# ==================================================
# ASSIGNMENTS
# ==================================================

elif page == "📝 Assignments":

    st.header("📝 Assignment Manager")

    st.write(
        "Add and manage your college assignments."
    )

    st.divider()

    assignment = st.text_input(
        "Enter Assignment Name"
    )

    subject = st.selectbox(
        "Select Subject",
        [
            "Python",
            "DBMS",
            "Java",
            "Computer Networks",
            "Machine Learning"
        ]
    )

    deadline = st.date_input(
        "Submission Date"
    )

    if st.button(
        "➕ Add Assignment"
    ):

        if assignment.strip() == "":

            st.error(
                "❌ Please enter an assignment name."
            )

        else:

            st.success(
                "✅ Assignment added successfully!"
            )

            st.write(
                "Assignment:",
                assignment
            )

            st.write(
                "Subject:",
                subject
            )

            st.write(
                "Submission Date:",
                deadline
            )

    st.divider()

    st.subheader("📋 Current Assignments")

    assignments = [
        ("Python", "Functions and Loops", "Pending"),
        ("DBMS", "SQL Queries", "Completed"),
        ("Java", "OOP Concepts", "Pending"),
        ("Machine Learning", "Regression", "Pending")
    ]

    for sub, name, status in assignments:

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("📚", sub)

        with col2:
            st.write(name)

        with col3:

            if status == "Completed":
                st.success(status)
            else:
                st.warning(status)


# ==================================================
# TIMETABLE
# ==================================================

elif page == "🗓️ Timetable":

    st.header("🗓️ Weekly Timetable")

    st.write(
        "Your weekly class schedule."
    )

    st.divider()

    days = {
        "Monday": "Python → DBMS → Mathematics",
        "Tuesday": "Java → Networks → Artificial Intelligence",
        "Wednesday": "DBMS → Python → Programming Lab",
        "Thursday": "Artificial Intelligence → Java → Mathematics",
        "Friday": "Networks → Python → Lab"
    }

    for day, classes in days.items():

        st.subheader("📅 " + day)

        st.info(classes)


# ==================================================
# RESULTS
# ==================================================

elif page == "📈 Results":

    st.header("📈 Academic Results")

    st.write(
        "View your subject-wise marks."
    )

    st.divider()

    results = {
        "Python": 86,
        "DBMS": 78,
        "Java": 82,
        "Computer Networks": 88,
        "Artificial Intelligence": 91
    }

    total = 0

    for subject, marks in results.items():

        st.subheader(subject)

        st.progress(marks / 100)

        st.write(
            str(marks) + " / 100"
        )

        total = total + marks

    st.divider()

    average = total / len(results)

    st.metric(
        "Average Marks",
        str(round(average, 2)) + " / 100"
    )


# ==================================================
# NOTICES
# ==================================================

elif page == "📢 Notices":

    st.header("📢 College Notices")

    st.write(
        "Important announcements from your college."
    )

    st.divider()

    st.warning(
        "📅 Internal examinations will begin soon."
    )

    st.info(
        "🎓 Project submissions are now open."
    )

    st.success(
        "🏆 Technical symposium registrations are available."
    )

    st.info(
        "📚 Library timing has been extended during examinations."
    )

    st.warning(
        "🚌 Students are requested to carry their college ID cards."
    )


# ==================================================
# FEES
# ==================================================

elif page == "💰 Fees":

    st.header("💰 Fee Information")

    st.write(
        "View your college fee details."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Fees",
            "₹85,000"
        )

    with col2:

        st.metric(
            "Paid",
            "₹70,000"
        )

    with col3:

        st.metric(
            "Pending",
            "₹15,000"
        )

    st.divider()

    st.subheader("💳 Payment Status")

    st.progress(
        70000 / 85000
    )

    st.write(
        "Payment completed: 82.35%"
    )

    if st.button(
        "💳 Make Payment"
    ):

        st.info(
            "Payment gateway can be connected here."
        )


# ==================================================
# STUDENT PROFILE
# ==================================================

elif page == "👤 Student Profile":

    st.header("👤 Student Profile")

    st.write(
        "Enter your student information."
    )

    st.divider()

    name = st.text_input(
        "Student Name"
    )

    roll_number = st.text_input(
        "Roll Number"
    )

    email = st.text_input(
        "Email Address"
    )

    course = st.selectbox(
        "Course",
        [
            "B.Tech CSE",
            "B.Tech ECE",
            "B.Tech EEE",
            "B.Tech Mechanical",
            "B.Tech Civil"
        ]
    )

    year = st.selectbox(
        "Year",
        [
            "1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year"
        ]
    )

    if st.button(
        "💾 Save Profile"
    ):

        if name.strip() == "":

            st.error(
                "❌ Please enter your name."
            )

        elif roll_number.strip() == "":

            st.error(
                "❌ Please enter your roll number."
            )

        elif email.strip() == "":

            st.error(
                "❌ Please enter your email address."
            )

        else:

            st.success(
                "✅ Profile saved successfully!"
            )

            st.write("### Student Details")

            st.write(
                "Name:",
                name
            )

            st.write(
                "Roll Number:",
                roll_number
            )

            st.write(
                "Email:",
                email
            )

            st.write(
                "Course:",
                course
            )

            st.write(
                "Year:",
                year
            )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "🎓 College Student Portal | "
    "Made with Python & Streamlit"
)