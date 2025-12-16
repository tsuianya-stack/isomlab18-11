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



data = {
    "Product": ["A","B","C","D","E"],
    "Sales": [120, 300, 250, 400, 180]
}

df = pd.DataFrame(data)
st.write(df)

min_sales = st.slider("Minimum sales", 0, 500, 200)

filtered_df = df[df["Sales"] >= min_sales]
st.write(filtered_df)

total_sales = filtered_df["Sales"].sum()
st.metric("Total Sales", total_sales)


students= {"Name":["Alice", "Bob", "Carol"], "Score":[75, 55, 90]}

df = pd.DataFrame(students)

filtered_df=df[df["Score"]>60]

st.write("All students")
st.write(df)

st.write("Students with score > 60")
st.write(filtered_df)


data = {"Product": ["Pen","Book","Bag","Laptop"], "Price":[5, 20, 50, 800]}

df=pd.DataFrame(data)
st.write("Product Data")
st.write(df)

min_price= st.slider("Minimum Price", 0, 1000, 100)
filtered_df=df[df["Price"]>=min_price]
st.write("Product with price over",min_price)
st.write(filtered_df)

name= st.text_input("Please enter your name:")

if st.button("Enter"):
  st.write(f"Welcome {name}.")


data={"Product": ["A", "B", "C", "D"], "Sales":[40, 120, 200, 80]}

df=pd.DataFrame(data)
st.write("Product Sales Data")
st.write(df)

filtered_df=df[df["Sales"]>=100]
total_sales = filtered_df["Sales"].sum()
st.metric("Total Sales", total_sales)

number = np.random.randint(0,100,size=10)
df=pd.DataFrame({"Number":number})
show_chart = st.checkbox("Click")
if show_chart:
  st.line_chart(df)


data = { "Product": ["Apple", "Banana", "Pear"], 
        "Price": [5, 10, 15],
        "Quantity": [10, 9, 12]}
df=pd.DataDrame(data)
st.title("Product Data")

min_quantity = st.slider("Minimum Quantity", 0, 20, 10)
df["Revenue"] = df["Price"]*df["Quantity"]

filtered_data= df[df["Quantity"]>=min_quantity]
st.write("Filtered Table")
st.write(filtered_data)
total_revenue = df["Revenue"].sum()
st.metric("Total Revenue", total_revenue)
st.bar_chat(df["Revenue"])


