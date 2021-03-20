from models import db, Person
from datetime import date

db.connect()


# zeeh = Person(name='Zeeh', birthday=date(1995, 6, 7))

# zeeh.save()

for person in Person.select():
    print(person.name)
    print(person.birthday)
