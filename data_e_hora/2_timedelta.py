# datetime representa a diferença entre 2 datas ou horas, permite fazer operações entre datas
from datetime import datetime, timedelta, date

tipo_carro = "P"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    # soma um tempo a data, no caso soma 30 minutos a data atual
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficarpa pronto às {data_estimada}")
elif tipo_carro == "M":
    # soma um tempo a data, no caso soma 45 minutos a data atual
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficarpa pronto às {data_estimada}")
else:
    # soma um tempo a data, no caso soma 60 minutos a data atual
    # é possivel realizar outras operações tambem, alem de passar outros tipos como horas, segundos, dias
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficarpa pronto às {data_estimada}")

print(date.today() - timedelta(days=1))  # subtraindo 1 dia da data de hoje

# tirando uma hora do datetime passado
resultado = datetime(2025, 1, 16, 20, 58, 30) - timedelta(hours=1)
print(resultado.time())  # chamando apenas a hora
