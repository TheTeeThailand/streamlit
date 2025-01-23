import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of the app
st.title("CSV File Bar Graph Viewer")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)

    # Display the dataframe
    st.write("### Uploaded Data:")
    st.dataframe(data)

    # Select columns for plotting
    columns = data.columns.tolist()

    if len(columns) > 1:
        x_column = st.selectbox("Select X-axis column", columns)
        y_column = st.selectbox("Select Y-axis column", columns, index=1)

        # Plot the bar graph
        if st.button("Generate Bar Graph"):
            plt.figure(figsize=(10, 6))
            plt.bar(data[x_column], data[y_column], color='skyblue')
            plt.title(f"Bar Graph: {y_column} vs {x_column}")
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            st.pyplot(plt.gcf())
    else:
        st.warning("The CSV file must have at least two columns for plotting.")
else:
    st.info("Please upload a CSV file to proceed.")
