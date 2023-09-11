from uuid import uuid1

def get_uuid():
    return uuid1().hex


for _ in range(5):
    uuid = get_uuid()
    print(uuid)