import streamlit as st
import pandas as pd
import numpy as np

data = { "Product": ["Apple", "Banana", "Pear"], 
        "Price": [5, 10, 15],
        "Quantity": [10, 9, 12]}

df=pd.DataFrame(data)

filtered_df = df[df["Quantity" >10]]
st.write(filtered_df)
total_revenue = df[df["Quantity"]*df["Sales"]]
st.write(total_revenue)
