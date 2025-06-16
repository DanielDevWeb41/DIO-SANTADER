
# OPERADORES ARITMETICOS

# Adicao
print(1 + 1)
# >>> 2 

# Subtracao
print(10 - 2)
# >>>> 8

# Multiplicacao
print(4 * 3 )
# >>> 12

# Divisao
print(15 / 3)
# >>> 5.0

# Divisao Inteira
print(12 // 2)
# >>> 6

# Modulo > RESTO DA DIVISAO
print(10 % 3)
# >>> 1

# Exponenciacao
print( 2 ** 3)
# >>> 8



# EXEMPLOS DE EXPRESSOES

print (10 - 5 * 2)
# >>>>> 0

print((10 - 5) * 2)
# >>>>> 10

print(10 ** 2 * 2)
# >>>> 200

print(10 ** (2 *2))
# >>>>>  10000

print(10 / 2 * 4)
# >>>>> 20.0




# OPERADORES DE COMPARACAO

#Igualdade 
saldo = 450
saque = 200
print(saldo == saque)
# >>>>> false


#Diferenca
print(saldo != saque)
# >>>>> True

#Maior que / maior ou igual
print(saldo > saque)
# >>>> True
print(saldo >= saque)
# >>>> True

#Menor que / Menor ou igual
print(saldo < saque)
# >>>>>> False
print( saldo <= saque)
# >>>>> False






# OPERADORES DE ATRIBUICAO

#ATRIBUICAO SIMPLES
saldo1 = 500
print(saldo1)
# >>>> 500

#ATRIBUICAO COM ADICAO
saldo1 += 200
print(saldo1)
# >>>>> 700

#ATRIBUICAO COM SUBTRACAO
saldo1 -= 100
print(saldo1)
# >>>>>> 600

#ATRIBUICAO COM MULTIPLICACAO
saldo1 *= 2 
print(saldo1)
# >>>>> 1200

#ATRIBUICAO COM DIVISAO
saldo1 //= 2
print(saldo1)

#ATRIBUICAO COM MODULO
saldo1 %= 500
print(saldo1)

#ATRIBUICAO OM EXPONENCIACAO
saldo1 **= 2
print(saldo1)






# Operadores Logicos

#Operador E >>>> AND 
saldo2 = 1000
saque2 = 250
limite = 200

saldo2 >= saque2 and saque2 <= limite
# >>>>> false 
# AS DUAS EXPRECOES PRECISAM SER VERDADEIRAS (SE TIVE-SE POR EXEMPLO 4 AS QUATROS PRECISAM SER VERDADEIRAS PARA DAR VERDADEIRO)


#Operador OU >>>>> OR

saldo2 >= saque2 or saque2 <= limite
# >>>>>> TRUE
# UMAS DAS EXPRECOES PRECISAM SER VERDADEIRAS PARA DAR *TRUE* SE AS DUAS TIVER ERRADAS VAI DAR *FALSE*



#OPERADOR DE NEGACAO >>>> NOT
contatos_emergencia = []

not 1000 > 1500
# >>>> True

not contatos_emergencia
# >>>> True

not "saque 1500;"
# >>>> False

not " "
# >>>> True


#operador Parenteses
conta_especial = True

saldo2 >= saque2 and saque <= limite or conta_especial and saldo2 >= saque2
# >>>> True

(saldo2 >= saque2 and saque2 <= limite) or (conta_especial and saldo2 >= saque2)
# >>>>> True

#SERVE PARA DELIMITIR, AJUDAR A ORGANIZAR UMA EXPRECAO






# OPERADORES DE IDENTIDADE >>>>>> (IS) (IS NOT)
# SAO OPERADORES UTILIZADOS PARA COMPARAR  SE OS DOIS OBJETOS TESTADOS OCUPAM A    MESMA POSICAO NA MEMORIA 


curso = "Curso de Python"
nome_curso = curso
saldo3, limite3 = 200, 200


curso is nome_curso
# >>>>> TRUE

curso is not nome_curso
# >>>>> FALSE

saldo is limite
# >>>>> TRUE





# OPERADORES DE ASSOCIACAO >>>> (in) (not in)
# SAO OPERADORES UTILIZADOS  PARA VERIFICAR  SE UM OBJETO  ESTA PRESENTE EM UMA S SEQUENCIA 

# EXEMPLO

curso_1 = "CURSO DE PYTHON"
frutas = ["Laranja", "uva", "banana"]
saques = [1500, 100]
# ELES TODOS SAO UMA SEQUENCIA

"PYTHON" in curso_1
# >>>>> True

"limao" not in frutas
# >>>> True

200 in saques
# >>>>> False

# ATENCAO IMPORTANTE >>> LETRA MAIUSCULAS ou MINUSCULAS INTERFEREM NO RESULTADO EXEMPLO SE EU DECLARA UVA no maiusculo nas frutas e querer usa o sinal de associacao nele depois vai ter que coloca ele todo maiusculo.

# exemplo: 
# frutas = ["UVA"]
# print("uva" in frutas)
# vai dar FALSE, pois na variavel FRUTAS ele esta em MAISCULA e no Print ele esta minuscula


