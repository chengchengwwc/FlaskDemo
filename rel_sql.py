# -*- coding: utf-8 -*-

#@author: weicheng

#@file: rel_sql.py

#@time: 2018/08/26

from sqlalchemy import create_engine,Column,Integer,String,Sequence,text,ForeignKey
from consts import DB_URI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import and_,or_
from sqlalchemy.orm import sessionmaker,relationship

eng = create_engine(DB_URI)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True,autoincrement=True)
    name = Column(String(50))


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, autoincrement=True)
    email_address = Column(String(128),nullable=True)
    user_id =Column(Integer,ForeignKey('users.id'))
    user = relationship("User",back_populates='addressess')


if __name__ == "__main__":
    #User.addresses = relationship('Address',order_by=Address.id,back_populates='user')
    Base.metadata.drop_all(bind=eng)
    Base.metadata.create_all(bind=eng)

    Session = sessionmaker(bind=eng)
    session = Session()

    user = User(name="XIAOMING")
    #user.addresses = [Address(email_address="DDDD",user_id=user.id),Address(email_address="ssxx",user_id=user.id)]
    session.add(user)
    session.commit()









