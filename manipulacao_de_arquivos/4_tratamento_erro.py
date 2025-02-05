from pathlib import Path

ROOT_PATH = Path(__file__).parent  # RETORNA O CAMINHO DO ARQUIVO

# try e except sao usados para tratar erros e exceções em um código
try:
    arquivo = open("meu_arquivo.py")  # abrindo um arquivo que não existe
except FileNotFoundError as exc:  # chamando o erro, erro de arquivo não encontrado
    print("Arquivo não encontrado!")  # printando uma alternativa para o erro
    print(exc)
except IsADirectoryError as exc:  # erro de tentar abrir um diretorio
    print(f"Não foi possível abrir o arquivo: {exc}")
except Exception as exc: #trata qualquer tipo de erro
    print(f"Algum erro ocorreu ao abrir o arquivo: {exc}")


# try:
#    arquivo = open(ROOT_PATH / "novo-diretorio")
# except IsADirectoryError as exc: #erro de tentar abrir um diretorio
#    print(f"Não foi possível abrir o arquivo: {exc}")
