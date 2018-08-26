# -*- coding: utf-8 -*-

#@author: weicheng

#@file: orm_sql.py

#@time: 2018/08/26


from sqlalchemy import create_engine,Column,Integer,String,Sequence,text
from consts import DB_URI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import and_,or_
from sqlalchemy.orm import sessionmaker


eng = create_engine(DB_URI)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True,autoincrement=True)
    name = Column(String(50))

def get_result(rs):
    print ("*"*20)
    for user in rs:
        print (user.name)




if __name__ == "__main__":
    #Base.metadata.drop_all(bind=eng)
    #Base.metadata.create_all(bind=eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    #session.add_all([User(name=username) for username in ["weicheng","bingqing","xiaobing","lele"]])
    #session.commit()
    rs = session.query(User).all()
    rs = session.query(User).filter(User.id.in_([2,]))
    rs = session.query(User).filter(and_(User.id>2,User.id<4))
    rs = session.query(User).filter(or_(User.id ==2 or User.id == 4))
    rs = session.query(User).filter(User.name.like('%min%'))
    user_message = session.query(User).filter_by(name='xiaoming').first()
    rs = session.query(User).filter(text('id>2 and id<4')).order_by(text('id')).all()
    rs = session.query(User).filter(text('id<:value and name=:name')).params(value=3,name="xiaoming").all()
    rs = session.query(User).from_statement(text('select * from users where name=:name')).params(name='wanglong').all()



