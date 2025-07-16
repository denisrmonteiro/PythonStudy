movieName = "Top Gun"
movieName2 = "top gun"

print (movieName == movieName2)

movieDescription = """
            Top Gun Maverick é um filme de aviação e aventura
        muito consagrado
"""
print (movieName)
# 1 - Multiplicação de strings
line = "="
print (line * 70)
print (movieDescription)

# 2 - Procurar palavra dentro de texto
print ("Filme" in movieDescription)

# 3 - Slices
# string[inicio:fim]

print (movieDescription[0:])
print (movieDescription[:30])
print (movieDescription[30:])

# 4 - Incremento
# string[inicio:fim:passo]

print (movieDescription[::2])

# Inverter string
print (movieDescription[::-1])

# Metodos
print (movieDescription.upper())
print (movieDescription.lower())
print (movieDescription.find("k"))
print (movieDescription.count("a"))
print (movieDescription.split(" "))