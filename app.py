import streamlit as st
from datetime import date

from database.db import SessionLocal, engine
from model.model import Base, Expense, Category

# ساخت جدول‌ها (اگر نبود)
Base.metadata.create_all(bind=engine)

st.title("پروزه مدیریت هزینه ها ")

session = SessionLocal()

# -------------------------
# دریافت دسته‌بندی‌ها
# -------------------------
categories = session.query(Category).all()

if not categories:
    st.warning("No categories found. Add categories first.")
else:
    category_dict = {cat.name: cat.id for cat in categories}

    # -------------------------
    # فرم ثبت هزینه
    # -------------------------
    with st.form("expense_form"):
        title = st.text_input("Title")
        amount = st.number_input("Amount", min_value=0)
        category_name = st.selectbox("Category", list(category_dict.keys()))
        expense_date = st.date_input("Date", value=date.today())

        submitted = st.form_submit_button("Add Expense")

        if submitted:
            new_expense = Expense(
                titel=title,
                amount=amount,
                category_id=category_dict[category_name],
                expense_date=expense_date
            )

            session.add(new_expense)
            session.commit()

            st.success("Expense added successfully!")

# -------------------------
# نمایش هزینه‌ها
# -------------------------
st.divider()
st.subheader("All Expenses")

expenses = session.query(Expense).all()

for exp in expenses:
    st.write(
        f"{exp.titel} | {exp.amount} | {exp.category.name} | {exp.expense_date}"
    )

session.close()