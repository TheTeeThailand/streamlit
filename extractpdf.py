import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pdfplumber

# Set the title of the app
st.title("PDF Table Data Viewer with Bar Graphs")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    st.write("### Uploaded File:", uploaded_file.name)

    # Extract tables from the PDF
    with pdfplumber.open(uploaded_file) as pdf:
        tables = []
        for page_number, page in enumerate(pdf.pages, start=1):
            page_tables = page.extract_tables()
            for table in page_tables:
                df = pd.DataFrame(table[1:], columns=table[0])  # Use the first row as column headers
                tables.append((page_number, df))

    if tables:
        st.write(f"### Found {len(tables)} tables in the PDF")

        for index, (page_number, table) in enumerate(tables):
            st.write(f"### Table {index + 1} (Page {page_number}):")
            st.dataframe(table)

            # Select columns for bar graph
            columns = table.columns.tolist()
            if len(columns) > 1:
                x_column = st.selectbox(f"Select X-axis column for Table {index + 1}", columns, key=f"x_{index}")
                y_column = st.selectbox(f"Select Y-axis column for Table {index + 1}", columns, key=f"y_{index}")

                # Plot bar graph
                if st.button(f"Generate Bar Graph for Table {index + 1}", key=f"btn_{index}"):
                    plt.figure(figsize=(10, 6))
                    plt.bar(table[x_column], pd.to_numeric(table[y_column], errors='coerce'), color='skyblue')
                    plt.title(f"Bar Graph: {y_column} vs {x_column} (Table {index + 1})")
                    plt.xlabel(x_column)
                    plt.ylabel(y_column)
                    plt.xticks(rotation=45)
                    plt.grid(axis='y', linestyle='--', alpha=0.7)
                    st.pyplot(plt.gcf())
            else:
                st.warning(f"Table {index + 1} does not have enough columns for plotting.")
    else:
        st.warning("No tables were found in the PDF file.")
else:
    st.info("Please upload a PDF file to extract tables and visualize bar graphs.")