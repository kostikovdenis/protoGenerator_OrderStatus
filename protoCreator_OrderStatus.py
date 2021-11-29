import glob
import io
import sys
import uuid

import OrderStatusMessage_pb2


def random_text(prefix: str):
    random = str(uuid.uuid4())
    return f'{random}'


with open("OrderStatusMessage.pb", "wb") as f:
    e = OrderStatusMessage_pb2.Envelop()

    e.header.stdVersion = 1
    e.header.uuID = random_text("")
    e.header.accessKey = random_text("")
    e.header.pdCode = 50
    e.header.pdVersion = 2
    e.header.repBegin = "20210729 14:15:14"
    e.header.repEnd = "20210729 14:39:11"
    e.header.isTest = False

    payload = e.payload.add()
    payload.date = '20210729 11:43:21' # Дата и время операции
    payload.attr1 = 234556 # Id заявки
    payload.attr2 = '380170041'        # ФРГУ-идентификатор ОИВ
    payload.attr3 = '468'              # ФРГУ-идентификатор паспорта услуги
    payload.attr4 = 'test_attr4'       # ФРГУ-идентификатор цели услуги
    payload.attr5 = 'test_attr5'       # Id пользователя
    payload.attr6 = 'test_attr6'       # Тип заявителя
    payload.attr7 = '0'                # Система породившая заявку
    payload.attr8 = '1068878479'       # Полученный статус
    payload.attr9 = 'test_attr9'       # Регион подачи заявления
    payload.attr10 = 'test_attr10'     # 
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
    payload.attr25 = ''
    payload.attr26 = ''
    
# Файл в бинарном формате
    f.write(e.SerializeToString())

# Файл в человекочитаемом формате
with open("OrderStatusMessage.protobuf", "w") as f:
    f.write(str(e))
