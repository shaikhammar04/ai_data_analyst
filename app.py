import streamlit as st
from utils.data_loader import load_csv, get_column_types
import matplotlib.pyplot as plt
import seaborn as sns
from utils.ai_insights import generate_basic_insights

st.set_page_config(page_title="AI Data Analyst", layout="wide")

st.title("📊 AI Data Analyst - Phase 1")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = load_csv(uploaded_file)

        st.success("File loaded successfully!")

        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        st.subheader("Dataset Shape")
        st.write(f"Rows: {df.shape[0]}")
        st.write(f"Columns: {df.shape[1]}")

        column_types = get_column_types(df)

        st.subheader("Column Types")
        st.write("Numeric Columns:", column_types["numeric"])
        st.write("Categorical Columns:", column_types["categorical"])

        st.subheader("Missing Values")
        missing = df.isnull().sum()
        missing_percent = (missing / len(df)) * 100
        missing_df = missing_percent[missing_percent > 0].sort_values(ascending=False)

        if len(missing_df) > 0:
            st.dataframe(missing_df)
        else:
            st.write("No missing values found 🎉")
        st.subheader("Statistical Summary")

        st.dataframe(df.describe().T)


        st.subheader("Correlation Heatmap")
        numeric_df = df.select_dtypes(include=["int64", "float64"])

        if numeric_df.shape[1] > 1:
            corr = numeric_df.corr()

            fig, ax = plt.subplots()
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

            st.pyplot(fig)
        else:
            st.write("Not enough numeric columns for correlation analysis.")

        st.subheader("AI Generated Insights")
        insights = generate_basic_insights(df)
        for insight in insights:
            st.write("•", insight)
            
    except Exception as e:
        st.error(str(e))