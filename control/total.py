from database.db import engine
from sqlalchemy.orm import Session
from sqlalchemy import func
from model.model import Expense,Category
from .category import creat_category
import jdatetime
from datetime import date



def shamsi_month_to_gregorian(year, month):
    start_shamsi = jdatetime.date(year, month, 1)
    end_shamsi = start_shamsi + jdatetime.timedelta(days=31)

    return (
        start_shamsi.togregorian(),
        end_shamsi.togregorian())

def monthly_report(category_name, year, month):
    with Session(engine) as session:
        category = session.query(Category)\
            .filter(Category.name == category_name)\
            .first()

        if not category:
            return 0, 0

        start_date, end_date = shamsi_month_to_gregorian(year, month)

        total = session.query(func.sum(Expense.amount))\
            .filter(
                Expense.category_id == category.id,
                Expense.expense_date >= start_date,
                Expense.expense_date < end_date
            ).scalar() or 0

        return total, category.monthly_limit
