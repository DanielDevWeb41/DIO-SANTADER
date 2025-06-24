# ESTRUTURA CONDICIONAL ALINHADA 
conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 1500
cheque_especial = 450


 
if conta_normal:
    
    if saldo >= saque:
        print("Saque Realizado Com Sucesso!")
    elif saque <= (saldo + cheque_especial):
         print("Saque Realizado Com uso do Cheque Especial!")
    else:
        print("Nao Foi Possivel Realizar o Saque, Saldo Insuficiente")
        
        
elif conta_universitaria:
    
    if saldo >= saque:
        print("Saque Realizado Com Sucesso!")
    else:
        print("Saldo Insuficiente!")

else:
    print("Sistema nao reconheceu seu tipo de conta, entre em contato com o seu Gerente.")