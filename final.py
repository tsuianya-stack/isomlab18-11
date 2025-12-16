import streamlit as st
import pandas as pd
import numpy as np

data = { "Product": ["Apple", "Banana", "Pear"], 
        "Price": [5, 10, 15],
        "Quantity": [10, 9, 12]}

df=pd.DataFrame(data)

filtered_df = df[df["Quantity"] >10]
st.write("Products with quantity >10:", filtered_df)
df["Revenue"] = df["Quantity"] * df["Price"]
st.write(df)


name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0)

if st.button("Agree"):
        st.write("Your name is ",name," and you are ",age," years old.")



months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]
sales = np.random.randint(100, 1000, size=12)

df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

st.write(df)

show_chart = st.checkbox("Show sales chart")

if show_chart:
    st.line_chart(df.set_index("Month"))
