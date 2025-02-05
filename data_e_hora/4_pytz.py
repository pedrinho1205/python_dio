import pytz
from datetime import datetime, timedelta, timezone

# pytz ajusta a data de acordo com o timezone informado

# ajusta o fuso horario de acordo com a zona passada
data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data2)
print(data)

# trabalhando com fuso horário sem pytz
data_sao_paulo = datetime.now(timezone(timedelta(hours=2)))
print(data_sao_paulo)
