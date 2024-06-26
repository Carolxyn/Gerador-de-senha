#Gerador de Senhas
import random

letra_maiuscula = chr(random.randint(65, 90))
letra_minuscula = chr(random.randint(97, 122))
char_especial = chr(33)
lista_numeros = []

for i in range(7):  # até 5 números
    numero = random.randrange(10)  # de 0 a 9
    lista_numeros.append(str(numero))  # adicione o número à lista

random.shuffle(lista_numeros)
senha_numerica = ''.join(lista_numeros)

senha_final = letra_maiuscula + letra_minuscula + senha_numerica + char_especial

print(senha_final)