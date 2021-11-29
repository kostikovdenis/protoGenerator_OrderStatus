import glob
import io
import sys
import uuid
import random

import OrderStatusMessage_pb2


def random_text(prefix: str):
    random = str(uuid.uuid4())
    return f'{prefix}-{random}'


with open("OrderStatus.pb", "wb") as f:
    e = OrderStatusMessage_pb2.Envelop()

    e.header.stdVersion = 1
    e.header.uuID = random_text("")
    e.header.accessKey = random_text("accessKey")
    e.header.pdCode = 50
    e.header.pdVersion = 1
    e.header.repBegin = "20212010 14:15:14"
    e.header.repEnd = "20212010 14:15:14"
    e.header.isTest = True

    for i in range(1000):
        payload = e.payload.add()
        payload.date = '2010.10.20 15:43:21'
        payload.attr1 = random.randint(111, 11111)
        payload.attr2 = random_text('attr2')
        payload.attr3 = random_text('attr3')
        payload.attr4 = random_text('attr4')
        payload.attr5 = random_text('attr5')
        payload.attr6 = random_text('attr6')
        payload.attr7 = random_text('attr7')
        payload.attr8 = random_text('attr8')
        payload.attr9 = random_text('attr9')
        payload.attr10 = random_text('attr10')
        payload.attr11 = ''
        payload.attr12 = ''
        payload.attr13 = ''
        payload.attr14 = ''
        payload.attr15 = ''
        payload.attr16 = ''
        payload.attr17 = ''
        payload.attr18 = ''
        payload.attr19 = ''
        payload.attr20 = ''
        payload.attr21 = ''
        payload.attr22 = ''
        payload.attr23 = ''
        payload.attr24 = ''
        payload.attr25 = str(random.randint(0, 100))
        payload.attr26 = 'UINREGCODE'

# Файл в бинарном формате
    f.write(e.SerializeToString())

# Файл в человекочитаемом формате
with open("OrderStatus.protobuf", "w") as f:
    f.write(str(e))
