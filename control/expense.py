from sqlalchemy.orm import Session,joinedload
from database.db import engine
import select

from model.model import Expense,Category
from control.category import creat_category




def update_expense(expense_id, title, amount, category_name, expense_date):
    with Session(engine) as session:
        expense = session.query(Expense)\
            .filter(Expense.id == expense_id)\
            .first()

        if not expense:
            return False

        category = session.query(Category)\
            .filter(Category.name == category_name)\
            .first()

        if not category:
            return False

        expense.titel = title
        expense.amount = amount
        expense.category_id = category.id
        expense.expense_date = expense_date

        session.commit()
        return True
def category_expense(new_name):
    with Session(engine) as session:
        category=session.query(Category).filter_by(name=new_name).first()
        if not category:
            category=Category(name=new_name)
            session.add(category)
            session.commit()
        return category


def creat_expense(titel,amount,category_name,expense_date):
    with Session(engine) as session: 
        category=category_expense(category_name)
        expense=Expense (titel=titel,amount=amount,category_id=category.id,expense_date=expense_date)
        session.add(expense)
        session.commit()




def delete_expense(expense_id):
    with Session(engine) as session:
        expense = session.query(Expense)\
            .filter(Expense.id == expense_id)\
            .first()

        if not expense:
            return False

        session.delete(expense)
        session.commit()
        return True
    
def get_all_expenses():
    with Session(engine) as session:
        return session.query(Expense)\
            .options(joinedload(Expense.category))\
            .all()



        
