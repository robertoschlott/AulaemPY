#Exercicio 1


largura = float(input("Informe a largura do retângulo: "))
comprimento = float(input("Informe o comprimento do retângulo: "))


perimetro = 2 * (largura + comprimento)
area = largura * comprimento


print(f"O perímetro do retângulo é: {perimetro}")
print(f"A área do retângulo é: {area}")


#Exercicio 2


a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))


multiplicacao = a * b
divisao_inteira = a // b
divisao_float = a / b


print(f"A multiplicação de {a} e {b} é: {multiplicacao}")
print(f"A divisão inteira de {a} por {b} é: {divisao_inteira}")
print(f"A divisão float de {a} por {b} é: {divisao_float:.2f}")


#Exercicio 3


PI = 3.141593


graus = float(input("Informe o valor em graus: "))


radianos = graus * (PI / 180)


print(f"{graus} graus equivalem a {radianos:.6f} radianos.")


#Exercicio 4



PI = 3.141593


raio = float(input("Informe o raio do círculo: "))


diametro = 2 * raio
circunferencia = 2 * PI * raio
area = PI * (raio ** 2)


print(f"Diâmetro: {diametro}")
print(f"Circunferência: {circunferencia:.6f}")
print(f"Área: {area:.6f}")


#Exercicio 5


n1 = float(input("Informe a primeira nota (n1): "))
n2 = float(input("Informe a segunda nota (n2): "))
n3 = float(input("Informe a terceira nota (n3): "))


media = (n1 + n2 + n3) / 3


if 8.5 <= media <= 10:
    conceito = 'A'
elif 7.0 <= media < 8.5:
    conceito = 'B'
elif 5.5 <= media < 7.0:
    conceito = 'C'
else:
    conceito = 'F'

print(f"A média do aluno é: {media:.2f}")
print(f"O conceito do aluno é: {conceito}")


#Exercicio 7


def numero_por_extenso(n):
    
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas_10_90 = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

    if n == 0:
        return "zero"

    if n < 0:
        return "menos " + numero_por_extenso(abs(n))

    extenso = ""

    
    c = n // 100
    n %= 100
    if c > 0:
        extenso += centenas[c] + " "

    
    if n >= 10 and n <= 19:
        extenso += dezenas[n - 10] + " "
        n = 0
    elif n >= 20:
        d = n // 10
        n %= 10
        if d > 0:
            extenso += dezenas_10_90[d] + " "

    
    if n > 0:
        extenso += unidades[n] + " "

    return extenso.strip()


num = int(input("Informe um número inteiro de até 4 dígitos: "))


print(f"O número {num} por extenso é: {numero_por_extenso(num)}")




