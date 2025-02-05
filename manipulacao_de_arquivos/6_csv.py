import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# codigo para escrever em um arquivo csv
# o writer serve pra escrever no arquivo enquanto o reader para ler

# try:
#     with open(ROOT_PATH / "usuarios.csv", "w", newline='', encoding="utf-8") as arquivo:
#         escritor = csv.writer(arquivo)  # cria o objeto para escrever
#         # escreve no arquivo com o método writerow
#         escritor.writerow(["id", "nome"])
#         escritor.writerow(["1", "João"])
#         escritor.writerow(["2", "Maria"])
# except IOError as exc:
#     print(f"Erro ao criar o arquivo. {exc}")

try:
    with open(ROOT_PATH / "usuarios.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)  # objeto para ler o arquivo
        for row in leitor:
            print(row)
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")

try:
    with open(ROOT_PATH / "usuarios.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo) #ler como dicionario
        for row in leitor: 
            print(f"ID: {row['id']}") #como esta sendo lido como dicionario, ele já ignora a linha de cabeçalho e pode ser acessado os valores pela chave 
            print(f"Nome:{row['nome']}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")
