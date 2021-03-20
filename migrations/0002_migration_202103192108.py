# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Person(peewee.Model):
    name = CharField(max_length=255)
    birthday = DateField()
    address = CharField(max_length=255)
    class Meta:
        table_name = "person"


def forward(old_orm, new_orm):
    person = new_orm['person']
    return [
        # Apply default value '' to the field person.address
        person.update({person.address: ''}).where(person.address.is_null(True)),
    ]
