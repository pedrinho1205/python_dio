from pathlib import Path

ROOT_PATH = Path(__file__).parent

# a função with abre e fecha o arquivo automaticamente
# with open(ROOT_PATH / "lorem.txt", "r") as arquivo:
#    print("trabalhando com o arquivo")
# 1 - usar bloco with
# 2 - usar IOError para verificar se o arquivo foi aberto com sucesso
# 3 - usar encoding

try:
    with open(ROOT_PATH / "python.txt") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"erro ao abrir o arquivo {exc}")

try:
    with open(ROOT_PATH / "arquivo-utf8.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Aprendendo manipular arquivos utilizando python")
except IOError as exc:
    print(f"erro ao abrir o arquivo {exc}")
