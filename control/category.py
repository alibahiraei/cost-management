from sqlalchemy.orm import Session
from database.db import engine
from model.model import Category


def creat_category(new_name,amount):
    with Session(engine) as session :
        category=session.query(Category).filter_by(name=new_name).first()
        if category:
            category.monthly_limit=amount
      
        else :
            category=Category(name=new_name,monthly_limit=amount)
        session.add(category)
        session.commit()
        return category
    
def delete_category(new_name):
    with Session(engine)as session:
        category=session.query(Category).filter(Category.name==new_name).first()
        if not category:
            return False
        if category.expense:
            return False ,'این دسته دارای هزینه ثبت شده است'
        
        session.delete(category)
        session.commit()
        return True,'حذف شد'
    

def update_category(old_name,new_name):
    with Session(engine)as session:
        category=session.query(Category).filter(Category.name==old_name).first()
        if not category:
            return False
        category.name=new_name
        session.add(category)
        session.commit()
        return True


    