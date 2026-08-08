import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Mini EDA App", layout="wide")


st.title("📊 Mini AI-Powered EDA Report")
st.write("Upload a CSV file and explore your dataset.")

uploaded_file = st.file_uploader("Choose CSV File", type=["csv"])


if uploaded_file:


    df = pd.read_csv(uploaded_file)


    st.success("Dataset Loaded Successfully!")


    #Sidebar
    st.sidebar.title("Navigation")
    option = st.sidebar.radio(
        "Go To",
        [
            "Dataset",
            "Overview",
            "Missing Values",
            "Statistics",
            "Correlation",
            "Distribution",
            #AI Pandas Assistant"
        ]
    )


    if option == "Dataset":
        st.subheader("Dataset")
        st.dataframe(df)


    elif option == "Overview":
        st.subheader("Dataset Overview")


        col1, col2, col3 = st.columns(3)


        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])
        col3.metric("Duplicates", df.duplicated().sum())


        st.write("### Data Types")
        st.dataframe(df.dtypes.astype(str))


    elif option == "Missing Values":
        st.subheader("Missing Values")


        missing = df.isnull().sum()
        missing = missing[missing > 0]


        if len(missing) == 0:
            st.success("No Missing Values Found 🎉")
        else:
            st.bar_chart(missing)


    elif option == "Statistics":
        st.subheader("Summary Statistics")
        st.dataframe(df.describe())


    elif option == "Correlation":


         numeric = df.select_dtypes(include="number")


         if numeric.shape[1] < 2:
             st.warning("Need at least two numeric columns.")
         else:


            corr = numeric.corr()


            fig, ax = plt.subplots(figsize=(8, 6))
            cax = ax.imshow(corr, cmap="coolwarm")


            ax.set_xticks(range(len(corr.columns)))
            ax.set_xticklabels(corr.columns, rotation=45)


            ax.set_yticks(range(len(corr.columns)))
            ax.set_yticklabels(corr.columns)


            plt.colorbar(cax)


            st.pyplot(fig)


    elif option == "Distribution":


        numeric = df.select_dtypes(include="number").columns


        if len(numeric) == 0:
            st.warning("No Numeric Columns")
        else:


            column = st.selectbox("Select Column", numeric)


            fig, ax = plt.subplots()


            ax.hist(df[column].dropna(), bins=20)


            ax.set_title(column)


            st.pyplot(fig)


else:
    st.info("Upload a CSV file to begin.")
