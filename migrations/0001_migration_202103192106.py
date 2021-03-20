# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Person(peewee.Model):
    name = CharField(max_length=255)
    birthday = DateField()
    class Meta:
        table_name = "person"


