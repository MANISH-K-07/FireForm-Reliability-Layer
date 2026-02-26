import streamlit as st
from main import reliability_layer

st.set_page_config(page_title="FireForm Reliability Layer", layout="wide")

st.title("🚒 FireForm Reliability Layer Demo")
st.subheader("Natural Language → Validated Incident Report JSON")

user_input = st.text_area("Enter Incident Description:")

if st.button("Process Report"):

    if user_input.strip() == "":
        st.warning("Please enter incident details.")

    else:

        result = reliability_layer(user_input)

        confidence = result["confidence"]
        threshold = 0.8

        st.markdown("### 📊 Reliability Score")
        st.progress(confidence)

        if confidence < threshold:
            st.error("⚠️ LOW CONFIDENCE OUTPUT — HUMAN VERIFICATION REQUIRED")

        if result["missing_fields"]:
            st.warning(f"Missing Fields Detected: {result['missing_fields']}")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🧾 Extracted Data (LLM Output)")
            st.json(result["extracted"])

            if result["validation_error"]:
                st.error("Initial Validation Failed")
                st.text(result["validation_error"])

        with col2:
            st.markdown("### ✅ Corrected & Validated Output")
            st.json(result["validated"])
