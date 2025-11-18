import streamlit as py
import pandas as pd
import matplotlib.pyplot as plt

st.tile("Personal Expense Tracker")

#Initilazie
if "expenses" not in st.session_state:
  st.session_state.expense = pd.Dataframe(columns=['Date', 'Category', 'Amount', 'Description'])

#Create sth
with st.form["expense_from"):
 st.subheader("Add New Expense")
 date = st.date_input ("Date")
 category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Bills", "Other"])
 amount = st.number_input( "Amount", min_value=0.0, step=0.01)
 description = st.text_input ("Description")

  submitted = st. form_submit_button ("|
  if submitted:
   new_expense = pd.DaraFrame({
  'Date':[date],
  'Category': [category],
  'Amount':[amout],
  'Description':[Description]
})
st.session_state.expenses = pd.contact([st.session_state.expenses, new_expense], ignore_index = True)
st.success("Expense added successfully!")

if not st.session_state.expense.empty:
  st.subheader("Your Expense")
  st.dataframe(st.session_state.expense)

  st.subheader("Summary")
  total_spent = st.session_state.expense['Amount'].sum()
  st.write(f"Total Spent: ${total_spent:2f}")

  category_totals = st.session_state.expense.groupby('Category')['Amount'].sum()
  
  fig,ax = plt.sbplot(figsize = (10,6)
  ax.pie(category_totals.values, labels = category_totals.index, autopct = '%1.1f%')
  ax.set_title("Expense by Category")
  st.pyplot(fig)
