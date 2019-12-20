from sqlalchemy import (create_engine, MetaData, Column,
                                Table, Integer,
                                String, Datetime)
from datetime import datetime

engine = create_engine('sqlite:///teste.db', echo=True)

metadata = MetaData(bind=engine)

user_table = Table('usuarios',
                    metadata,
                    Column('id', Integer, primary_key=True),
                    Column('nome', String(40), index=True),
                    Column('idade', Integer, nulltable=False),
                    Column('senha'), String),
                    Column('criada_em', DateTime, default=datetime.now),
                    Column('atualizada_em', Datetime, default=datetime.now, onupdate=datetime.now)
                    )