from sqlalchemy import create_engine ,Column, Integer, String, Text
from sqlalchemy.orm import declarative_base,sessionmaker


engine =create_engine("sqlite:///store.db")
BASE = declarative_base()

class category(BASE):
    __tablename__ = "categories"

    id = Column (Integer() ,primary_key=True)
    name = Column (String())
    description =Column (Text())

BASE.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

food = category(name="Food", description="Delicious meals")
session.add(food)


electronics = category(name="Electronics", description="All electronics")
session.add(electronics)
session.commit()

clothings = category(name="Clothings", description="Stunning Clothes")
session.add(clothings)
session.commit()

stationaries = category(name="Stationaries", description="Affordable")
session.add(stationaries)
session.commit()

funitures = category(name="funitures", description="Luxuries")
session.add(funitures)
session.commit()


categories = session.query(category).filter(category.name == "Food").all()
for category in categories:
 print(category)

categories
