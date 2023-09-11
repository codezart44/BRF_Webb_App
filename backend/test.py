
import os
import subprocess

from datetime import datetime
from pytz import timezone
from uuid import uuid1, uuid3, uuid4, uuid5, NAMESPACE_DNS, NAMESPACE_OID, NAMESPACE_URL, NAMESPACE_X500

import pandas as pd
import os
from dotenv import load_dotenv

import bcrypt
import sqlite3

con = sqlite3.connect('flask_server/db/dev.db')
first_name = 'Arne'
last_name = 'Barne'
email = 'arne@barne.se'
pw = 'some1sPW22'
pw_enc = pw.encode('utf-8')
print(pw)
print(pw_enc)


salt = bcrypt.gensalt(rounds=12)
pw_hash = bcrypt.hashpw(password=pw_enc, salt=salt)
USER = 1

now = datetime.utcnow()         #.strftime('%Y-%m-%d %H:%M:%S')
user_data = {
    'user_id': [uuid4().hex],
    'first_name': [first_name],
    'last_name': [last_name],
    'email': [email],
    'password': [pw_hash.decode('utf-8')],
    'user_role': [USER],
    'created_at': [now],
    'updated_at': [now]
}
new_user = pd.DataFrame(user_data)

pd.options.display.max_columns = 10
print(new_user)
new_user.to_sql(name='users', con=con, if_exists='append', index=False)
con.close()

quit()


pw = 'some1sPW22'
pw_enc = pw.encode('utf-8')
print(pw)
print(pw_enc)


salt = bcrypt.gensalt(rounds=12)
pw_hash = bcrypt.hashpw(password=pw_enc, salt=salt)

print(pw_hash)
print(pw_hash.decode('utf-8'))


pwMatch = bcrypt.checkpw(password=pw_enc, hashed_password=pw_hash)
print(pwMatch)




quit()

# import bcrypt
from flask_server_advanced.project.extensions import bcrypt

password = 'Some1isUsingML'
BCRYPT_LOG_ROUNDS = 12

pw_hash = bcrypt.generate_password_hash(password=password, rounds=BCRYPT_LOG_ROUNDS).decode('utf-8')
print(pw_hash)

pw_check = bcrypt.check_password_hash(pw_hash=pw_hash, password=password)
print(pw_check)

quit()


# Given by chatGPT as examples
name = "example.com"
oid = "1.3.6.1.4.1.98765"
url = "https://www.example.com"
x500_dn = "CN=John Doe,OU=People,O=Example Corp,C=US"

print(uuid1())      # based on host MAC address and current time

print(uuid3(namespace=NAMESPACE_DNS, name=name))      # uses MD5 for encryption to generate uuid based on name and namespace
print(uuid3(namespace=NAMESPACE_OID, name=oid))
print(uuid3(namespace=NAMESPACE_URL, name=url))
print(uuid3(namespace=NAMESPACE_X500, name=x500_dn))

print(uuid4())      # Uses seudo random numbers to generate uuid, NOTE most commonly used
print(uuid4().hex, 'hexxx')

print(uuid5(namespace=NAMESPACE_DNS, name=name))      # Uses SHA-1 for ebcryption to generate uuid based on name and namespace. 
print(uuid5(namespace=NAMESPACE_OID, name=oid))
print(uuid5(namespace=NAMESPACE_URL, name=url))
print(uuid5(namespace=NAMESPACE_X500, name=x500_dn))




tz_sthml = timezone('Europe/Stockholm')

print(datetime.now(tz=tz_sthml))
print(datetime.now())
print(datetime.utcnow())
print(datetime.utcnow())


class MyDog:
    LEGS = 4
    COLOR = 'black'
    FRIENDLY = True


    def __init__(self) -> None:
        pass

print(MyDog.FRIENDLY)