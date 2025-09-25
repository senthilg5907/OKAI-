import streamlit as st

# --- Page configuration ---
st.set_page_config(page_title="Greeting App", page_icon="👋", layout="centered")

# --- Header ---
st.markdown("# 👋 Greeting App")
st.write("Enter your name and age and click **Greet** to see a friendly message.")

# --- Inputs ---
name = st.text_input("Name", placeholder="Enter your name")
age = st.slider("Age", min_value=0, max_value=120, value=25, step=1)

# Show a small live preview (optional UX)
st.info("Preview: {} — Age: {}".format(name if name else "(no name yet)", age))

# --- Button & Greeting logic ---
if st.button("Greet"):
    # Basic validation
    if not name or not name.strip():
        st.warning("Please enter your name before greeting.")
    else:
        # Compose an age-based friendly remark
        if age < 13:
            stage = "a child"
        elif age < 20:
            stage = "a teenager"
        elif age < 60:
            stage = "an adult"
        else:
            stage = "a senior"

        # Final greeting
        st.success(f"Hello {name}! You're {age} years old — {stage}. Nice to meet you! 👋")

        # Fun visual celebration for valid input
        st.balloons()
