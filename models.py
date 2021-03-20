from peewee import *

db = PostgresqlDatabase('hello', user='postgres',
                        password='postgres', host='localhost', port=5455)


class Person(Model):
    name = CharField()
    birthday = DateField()
    address = CharField()

    class Meta:
        database = db  # This model uses the "people.db" database.
