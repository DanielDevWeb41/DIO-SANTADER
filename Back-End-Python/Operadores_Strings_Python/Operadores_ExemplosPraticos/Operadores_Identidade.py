
# EXEMPLO QUE NAO OCUPAM A MESMA MEMORIA 
saldo = 1000
limite = 500

print(saldo is limite)
# >>>>> FALSE

print(saldo is not limite)
# >>>>>> TRUE



# EXEMPLO QUE OCUPAM A MESMA MEMORIA 
saldo_1 = 2000
limite_1 = 2000

print(saldo_1 is limite_1)
# >>>> TRUE

print(saldo_1 is not limite_1)
# >>>>> FALSE
