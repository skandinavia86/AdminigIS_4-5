import sys
from peewee import *
import datetime
from random import randint

global db
db=SqliteDatabase('bd.db')

class Clients(Model):
     Name=TextField(unique=True)
     City=TextField()
     Address=CharField()

     class Meta:
        database=db
        table_name="clients"

class Orders(Model):
     Client_id=ForeignKeyField(Clients)
     Date=DateField()
     Amount=IntegerField()
     Description=TextField()

     class Meta:
        database=db
        table_name="orders"

def init(tab1, tab2):
    resh1=db.table_exists(tab1)
    resh2=db.table_exists(tab2)
    if resh1 == True and resh2==True:
        return True
    else: 
        return False

cl = [{ 
    "Name": 'name',
    "City" : 'city',
    "Address" : "address",
}]

o_rd = [{
    "Client_id":1,
    'Date': 1,
    "Amount": 1,
    "Description": "description",
}]

if len(sys.argv)<2:
     exit("""Need use commands:
        python peewee_pb.py init
        python peewee_pb.py fill
        python peewee_pb.py show tablename""")

elif sys.argv[1]=='init':
    if init('clients', 'orders') == True:
        db.drop_tables([Clients, Orders])
        db.create_tables([Clients, Orders])
    else:
        db.create_tables([Clients, Orders])

elif sys.argv[1]=='fill':
     for i in range(1, 11):
         cl.append({
            "Name": "name"+str(i),
            "City" : 'city'+str(i),
            "Address" : "address"+str(i),
        })

         o_rd.append({
            "Client_id": i,
            'Date': str(datetime.date(randint(2014,2014), randint(1,12), randint(1,28))),
            "Amount": randint(1,100),
            "Description": "description"+str(i),
        })

     new_cl=Clients.insert_many(cl).execute()
     new_ord=Orders.insert_many(o_rd).execute()

     db.commit()

elif sys.argv[1]=='show':
    if sys.argv[2]=='clients':
        for clien in Clients.select():
            print(clien.id, "\t", clien.Name, "\t", clien.City, "\t", clien.Address)
    elif sys.argv[2]=='orders':
        for or_d in Orders.select():
            print(or_d.Client_id, "\t", or_d.Date, "\t", or_d.Amount, "\t", or_d.Description)

else: print("Error")

print(len(Clients.select()))
print(len(Orders.select()))
db.close()
