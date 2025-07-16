# Utilizando o input

number1 = int(input("Digite o primeiro numero: "))
number2 = int(input("Digite o segundo numero: "))

# Aritmeticos
sum = number1 + number2
sub = number1 - number2
div = number1 / number2
mult = number1 * number2
mod = number1 % number2
exp = number1 ** number2

print(f"Potencia do numero {number1} por {number2} é {exp}")
print(f"Resto da divisão de {number1} por {number2} é {mod}")

# Comparação
bigger     = number1 > number2;
smaller    = number1 < number2;
equal      = number1 == number2;
diff       = number1 != number2;
bigEqual   = number1 >= number2;
smallEqual = number1 <= number2;

print (f"Maior: {bigger}")
print (f"Small: {smaller}")
print (f"Equal: {equal}")
print (f"Different: {diff}")
print (f"BigEqual: {bigEqual}")
print (f"smallEqual: {smallEqual}")

# Atribuição
number1 += 1 # number1 = number1 + 1
