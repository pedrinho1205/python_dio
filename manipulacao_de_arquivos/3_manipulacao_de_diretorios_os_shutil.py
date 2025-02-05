import os
import shutil
from pathlib import Path

# __file__ retorna o caminho do arquivo em execução sem ele próprio
ROOT_PATH = Path(__file__).parent
# print(ROOT_PATH)
# o parent isola o nome do arquivo e retorna apenas o restante do caminho, ele retorna a pasta do arquivo
print(ROOT_PATH.parent)
# os.mkdir(ROOT_PATH / "novo-diretorio") #cria uma pasta no caminho passado
# arquivo = open(ROOT_PATH / "novo.txt", "w")
# arquivo.close()

# renomeia o arquivo passado como primeiro argumento para o passado como segundo argumento
# os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# os.remove(ROOT_PATH / "alterado.txt")  # remove o arquivo passado
# move o arquivo para o caminho passado como segundo parametro
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")
