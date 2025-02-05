# strftime converte um objeto datetime para uma string
# strptime converte uma string para um objeto datetime

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2025-1/16 21:32"
mascara_ptbr = "%d/%m/%Y"
print(data_hora_atual.strftime(mascara_ptbr))
mascara_en = "%Y-%m-%d %H:%M"

# converte string para objeto datetime
print(datetime.strptime(data_hora_str, mascara_en))
