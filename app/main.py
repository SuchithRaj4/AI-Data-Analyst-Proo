import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Data Analyst Pro", layout="wide")

st.title("📊 AI Data Analyst Pro")
st.write("Upload a CSV file to begin analysis.")

# File Upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("✅ Data Preview")
    st.dataframe(df)

    # Basic Info
    st.subheader("📌 Dataset Information")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    # Summary Stats
    st.subheader("📈 Summary Statistics")
    st.write(df.describe())

    # Missing Values
    st.subheader("⚠️ Missing Values Check")
    st.write(df.isnull().sum())
    # Q&A Section
        # Q&A Section
    st.subheader("🤖 Ask a Question About the Data")

    question = st.text_input("Type your question (e.g., 'Who scored the highest in Math?')")

    if question:
        try:
            matched_cols = [col for col in df.columns if col.lower() in question.lower()]

            if len(matched_cols) == 1:
                col = matched_cols[0]
                max_value = df[col].max()
                max_row = df[df[col] == max_value]

                st.write(f"✅ Highest {col}: {max_value}")
                st.write(max_row)

                # Simple Insight
                st.subheader("🧠 Insight")
                st.write(f"The highest value in '{col}' is {max_value}. This indicates the top performer or maximum result in this column.")

            else:
                st.write("⚠️ Please mention exactly one column name in your question.")

        except:
            st.write("⚠️ Unable to answer. Try a simpler question.")

    # PDF Report Section
    st.subheader("📄 Download Report")

    from fpdf import FPDF

    if st.button("Generate PDF Report"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Title
        pdf.cell(200, 10, txt="AI Data Analyst Report", ln=True, align='C')
        pdf.ln(5)

        # Dataset Info
        pdf.set_font("Arial", size=10)
        pdf.cell(200, 8, txt=f"Rows: {df.shape[0]}", ln=True)
        pdf.cell(200, 8, txt=f"Columns: {df.shape[1]}", ln=True)
        pdf.ln(5)

        # Summary Stats
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Summary Statistics:", ln=True)
        pdf.set_font("Arial", size=9)
        stats = df.describe().to_string()
        for line in stats.split('\n'):
            pdf.cell(0, 5, txt=line, ln=True)

        pdf.ln(5)

        # Missing Values
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Missing Values:", ln=True)
        pdf.set_font("Arial", size=9)
        missing = df.isnull().sum().to_string()
        for line in missing.split('\n'):
            pdf.cell(0, 5, txt=line, ln=True)

        pdf.ln(5)

        # Save PDF
        pdf.output("report.pdf")
        st.success("✅ PDF Report Generated! Check the project folder.")
