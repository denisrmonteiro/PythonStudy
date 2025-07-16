# Utilizando o input

name = input("Digite o nome do filme\n")
lauchYear = int(input("Digite o ano de lançamento\n"))
rateMovie = float(input("Digite a nota do filme\n"))

# Alternativa 1
# print ("O nome do filme é:", name)
# print ("O ano de lançamento é:", lauchYear)
# print ("A nota do filme é:", rateMovie)

#Alternativa 2
print (
    f"Nome do filme: {name}\n"
    f"Ano de lançamento: {lauchYear}\n"
    f"Nota do filme: {rateMovie}"
    )
