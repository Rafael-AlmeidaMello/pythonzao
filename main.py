# 1° Exercício
#numero = float(input("Digite um numero: "))

#if numero > 0:
#    print(f"{numero} é positivo!")
#elif numero < 0:
#    print(f"{numero} é negativo!")
#else:
#    print(f"{numero} é zero!")

# 2° Exercício
#numero = float(input("digite um numero: "))

#if numero % 2 == 0:
#    print("o numero é par")
#else:
#    print("o numero é impar")

# 3° Exercício

#numero1 = float(input("digite o primeiro numero: "))
#numero2 = float(input("digite o segundo numero: "))

#if numero1 > numero2:
#    print(f"O maior numero é {numero1}")
#else:
#    print(f"O maior numero é {numero2}")
 
# 4° Exercício
       
#numero1 = float(input("digite o primeiro numero: "))
#numero2 = float(input("digite o segundo numero: "))
#numero3 = float(input("digite o terceiro numero: "))

#if numero1 > numero2 and numero3:
#    print(f"O maior numero é {numero1}")
#elif numero2 > numero1 and numero3:
#    print(f"O maior numero é {numero2}")
#else:
#        print(f"O maior numero é {numero3}")

# 5° Exercício

#nota1 = float(input("digite a primeira nota: "))
#nota2 = float(input("digite a segunda nota: "))
#media = (nota1 + nota2) / 2

#if media >= 7:
#    print("você foi aprovado!")
#elif media < 7 and media >= 5:
#    print("você está em recuperação")
#else:
#    print("você foi reprovado")

# 6° Exercício

#idade = int(input("digite sua idade: "))

#if idade < 18:
#    print("voce é uma criança")
#elif idade >= 18 and idade <= 59:
#    print("voce é um adulto")
#else: print("voce é um idoso")

# 7° Exercício

#salario = float(input("Digite seu salário: "))
#desconto10 = salario * 0.90
#desconto5 = salario * 0.95

#if salario > 5000:
#    print(f"seu salario liquido é {desconto10:.2f}")
#else:
#    print(f"seu salario liquido é {desconto5:.2f}")

# 8 Exercício

#user = "admin"
#password = "1234"

#passo1 = input("Digite o seu usuário de login: ")
#passo2 = input("Digite sua senha de usuário: ")

#if passo1 == user and passo2 == password:
#    print("Parabéns! Você efetuou a etapa de login")
#else:
#    print("Usuário ou senha incorreta...")

# 9 Exercício

#numero1 = float(input("Digite o primeiro número: "))
#numero2 = float(input("Digite o segundo número: "))

#operacao = input("Digite a operação: +, - , *, / ")

#match operacao:
#    case "+":
#        resposta = numero1 + numero2
#    case "-":
#        resposta = numero1 - numero2
#    case "*":
#        resposta = numero1 * numero2
#    case "/":
#        resposta = numero1 / numero2
#    case _ :
#        print("Você não selecionou nenhuma das opções, programa finalizado.")

#print(f"O resultado é {resposta}")

# 10 Exercício

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura em metros(exemplho: 1.88): "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Você está abaixo do peso, seu IMC é {imc:.2f}")
elif imc >= 18.5 and imc <= 24.9:
    print(f"Você possui peso normal, seu IMC é {imc:.2f}")
elif imc > 24.9 and imc < 30:
    print(f"Você possui sobrepeso, seu IMC é {imc:.2f}")
else:
    print(f"Você é obeso")