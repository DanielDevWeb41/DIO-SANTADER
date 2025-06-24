# IF, ELSE, ELIF

maior_idade = 18
IDADE_ESPECIAL = 17


idade = int(input("Informe sua idade: "))

if idade >= maior_idade:
    print("Maior de idade, Pode tirar a CNH")
    
if idade < maior_idade:
    print("Ainda nao pode tirar a CNH.")
    
    
    
if idade >= maior_idade:
    print("Maior de idade, Pode tirar a CNH")
else:
    print("Ainda nao pode tirar a CNH.")
    
    
    
if idade >= maior_idade:
    print("Maior de idade, Pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas nao pode fazer aulas praticas.")
else:
    print("Ainda nao pode tirar a CNH.")