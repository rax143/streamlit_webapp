import streamlit as st
import pandas as pd
import seaborn as sns


#Add title and sub-header
st.title("Data Analytics")
st.subheader("In the project you will get option for subheader Data Analytics")


#Upload dataset
upload = st.file_uploader("Please upload your file in CSV format")
if upload is not None:
	file_data = pd.read_csv(upload)


#Show Dataset
if upload is not None:                  # Here we are checking if file is uploaded
	if st.checkbox("Preview_data") :	# here we are checking if checkbox is ticked
		if st.button("Head"):			# checking if head button is clicked
			st.write(file_data.head())
		if st.button("Tail"):			# checking if tail button is clicked
			st.write(file_data.tail())

#Show datatype of each column
if upload is not None:                  # Here we are checking if file is uploaded
	if st.checkbox("Check Datatype of column"):
		st.text("Data types")
		st.write(file_data.dtypes) 		# There is some bug in this


#Show shape of data
if upload is not None:                  # Here we are checking if file is uploaded
	data_shape = st.radio('Which type of data you want to see?',("Row","Column"))

	if data_shape == "Row":
		st.text("This shape of your data")
		st.write(file_data.shape[1])
	if data_shape == "Column":
		st.text("This shape of your data")
		st.write(file_data.shape[0])


#Show null values in dataset
if upload is not None:
	nullValues = file_data.isnull().values.any()     
	if nullValues:
		if st.checkbox("Show null values data graphically"):
			sns.heatmap(file_data.isnull())
			st.set_option('deprecation.showPyplotGlobalUse', False)
			st.pyplot()


#Show null values in dataset
if upload is not None:
	duplicateValues = file_data.duplicated().any()
	if duplicateValues:
		st.warning("Data contains some duplicate values")
		dupData = st.selectbox("Do you want to remove duplicate data?", ("Select option","Yes", "No"))
		if dupData == "Yes":
			file_data = file_data.drop_duplicates()
			st.write("Duplicate data removed successfully")
		elif dupData == "Yes":
			st.write("No problem carry on !!!")


# Get overall statistics
if upload is not None:
	if st.checkbox("Get description about data?"):
		st.write(file_data.describe() , include = all)


# About app
if st.button("About App"):
	st.write("Made with help of streamlit")
	st.write("Thanks to streamlit")

#By
if st.button("Made By"):
	st.success("Made by Rahul with lots of love")


