# o segundo parametro é o modo de leitura
arquivo = open(
    "C:/Users/PEDRO/Documents/python/manipulacao_de_arquivos/lorem.txt", "r")
# print(arquivo.read())  # retorna o conteúdo do arquivo em uma string
# print(arquivo.read())  # retorna a primeira linha, uma linha de cada vez
print(arquivo.readlines())  # retorna uma lista com cada linha do arquivo

# TIP
# while len(linha := arquivo.readline()):
#    print(linha)

arquivo.close()  # sempre que abrir um arquivo deve-se fechar
