import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as py


#reading the dataset
def load_data():
    df = pd.read_csv("Iris.csv")
    return df

data = load_data()
st.title("Iris Data Dashboard")
st.write("An interactive keyboard to explore the iris data")

#creating an option to view the raw data
if st.checkbox("Show the raw data"):
    st.subheader("Iris data")
    st.dataframe(data)
#Show the average sepal length for each species
if st.checkbox("Show the average sepal length"):
    st.subheader("Average sepal length per species")
    av_sepal_length = data.groupby("Species")["SepalLengthCm"].mean()
    st.write(av_sepal_length)

#Display a scatter plot comparing the two features
st.subheader("A scatter plot showing the relationship between the sepal length and widths")    
fig = px.scatter(data, x='SepalLengthCm', y='SepalWidthCm', color='Species')
st.plotly_chart(fig)

#filter data based on species
species = data['Species'].unique()
species_filter = st.multiselect("Select the species", species, default=species)
filtered_data = data[data['Species'].isin(species_filter)]

#Display a pairplot for the selected species
if st.checkbox("Show pairplot of the species"):
    st.subheader("Species Pairplot")

    if species_filter:
       plot = sns.pairplot(filtered_data, hue="Species")

    else:
        plot = sns.pairplot(filtered_data, hue="Species")   
    st.pyplot(plot)
#Show the distribution of a selected feature
if st.checkbox("Show the distribution of the selected species"):
    st.subheader("Distribution of sepal dimensions per selected species")

    plotA = px.histogram(data, x=species_filter, category_orders=dict(Species=["Species"]), nbins=30, marginal='violin')
    st.plotly_chart(plotA)      
