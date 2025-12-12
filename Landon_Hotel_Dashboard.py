# Upload and Preview External Data in Streamlit

# Import packages
import streamlit as st
import pandas as pd # For data manipulation, analysis, and cleaning, commonly used in data science, finance, and machine learning.


# Write title
st.title("Hotel Data Dashboard")
# Write description
st.write("Upload two hotel data files, merge on `Hotel ID`, and preview.")

# Add file upload widget for revenue and expenses file
rev_exp_file = st.file_uploader("Upload Revenue and Expenses (xlsx)", type="xlsx")
# Add file upload widget for location file
loc_file = st.file_uploader("Upload Location (xlsx)", type="xlsx")

# Check if both files have been uploaded
if rev_exp_file and loc_file:
    # Display a spinner while files are being processed
    with st.spinner("Reading and merging files…"):
        # Use the pandas package, read in revenue and expenses file
        df_rev_exp = pd.read_excel(rev_exp_file)
        # Read in location file
        df_loc = pd.read_excel(loc_file)
        # Merge files on 'Hotel ID'. Assign a DataFrame obj to the variable `df`
        df = (
            df_rev_exp
            .merge(df_loc, on="Hotel ID", how="outer")
        )
    # Display success message when files are merged
    st.success("Files merged successfully!")
    # Add subheader for merged data preview
    st.subheader("Merged Data Preview")
    # Display first couple rows of merged data
    st.dataframe(df.head())

    #Add subheader for full merged data section
    st.subheader("Full Merged Data")
    #Add expander to show entire merged dataset
    with st.expander("Show full dataset"):
        st.dataframe(df)

    # Cache computations that return data
    @st.cache_data
    # Create DataFrame to CSV conversion function
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    # Convert merged dataframe to CSV for download
    csv = convert_df(df)

    # Add download button to allow users to download merged data as CSV file
    st.download_button(
        "Download Full Merged Data as CSV",
        data=csv,
        file_name="merged_hotel_data.csv",
        mime="text/csv"
    )

# If files have not been uploaded, display an informational message
else:
    st.info("Please upload the two files to proceed.")