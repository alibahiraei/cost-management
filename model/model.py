from sqlalchemy.orm import Mapped,mapped_column,relationship
from database.db import Base
from sqlalchemy import Integer , String,ForeignKey,Date
from datetime import date


#model
class Category(Base):
    __tablename__='categories'
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    name:Mapped[str]=mapped_column(String,nullable=False)
    expense:Mapped[list['Expense']]=relationship(back_populates='category')
    monthly_limit:Mapped[int]=mapped_column(Integer,default=0)

class Expense(Base):
    __tablename__='expenses'
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    titel:Mapped[str]=mapped_column(String,nullable=False)
    amount:Mapped[int]=mapped_column(Integer,nullable=False)
    category_id:Mapped[int]=mapped_column(Integer,ForeignKey('categories.id'))
    category:Mapped['Category']=relationship(back_populates='expense')
    expense_date:Mapped[date]=mapped_column(Date,default=date.today)


    


