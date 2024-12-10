from app import create_app, db
from app.models import User
from faker import Faker
import random

fake = Faker()

def seed_database():
   app = create_app()
   with app.app_context():
       print("Reset database!")
       db.drop_all()
       db.create_all()

       users = [
           User(
               name=fake.name(),
               age=random.randint(18, 80)
           ) for _ in range(100)
       ]

       db.session.bulk_save_objects(users)
       db.session.commit()
       print("Database seeded with 100 users!")

if __name__ == "__main__":
   seed_database()