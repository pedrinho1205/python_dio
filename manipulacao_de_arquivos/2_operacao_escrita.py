arquivo = open(
    "C:/Users/PEDRO/Documents/python/manipulacao_de_arquivos/teste.txt", "w") #deve ser passado um arquivo que não existe no primeiro parâmetro, pois ele será criado  
# escreve a string única no arquivo
arquivo.write("Escrevendo dados em um novo arquivo.")
# recebe um objeto iterável, como uma lista de strings e escreve um item de cada vez, ou seja, escreve uma lista de strings
arquivo.writelines(["\n", "escrevendo", "um", "novo", "texto"])
arquivo.close()
