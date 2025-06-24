
# IDENTACAO E BLOCOS


    # A ESTETICA
    # identar codigo e uma forma de manter o codigo fonte mais legivel e manutenivel. Mas em Python ela exerce um segundo papel, atraves da indentacao o interpretado consegue determinar onde um bloco de comando inicia  e onde ele termina.


    # BLOCO DE COMANDO
    # As Linguagens de programacao costuman utilizar caracteres ou palavras reservadas para terminar o inicio e fim do bloco. Em Java e C por exemplo, utilizamos chaves:

        #EXEMPLO BLOCO EM JAVA
            # void sacar(double valor) { // inicio do bloco do metodo 

            #       if (this.saldo >= valor) { // Inicio do bloco do if

            #           this.saldo -= valor;

            #   } // fim do bloco do if

            # } // fim do bloco do metodo

        #EXEMPLO BLOCO EM JAVA SEM FORMATAR
            # void sacar(double valor) { // inicio do bloco do metodo 
            # if (this.saldo >= valor) { // Inicio do bloco do if
            # this.saldo -= valor;
            # } // fim do bloco do if
            # } // fim do bloco do metodo

        #ESSE codigo Vai FUNCIONAR EM JAVA Mesmo Sem Identar


    # UTILIZANDO ESPACOS
    # Existe uma convencao em Python, que define as boas praticas para escrita de codigo na linguagem. Nesse  documento e indicado utlizar 4 espacos em branco por nivel de indentacao,  ou seja, a cada novo bloco adicionamos 4 novos  espacos em branco

    #EXEMPLO EM PYTHON (BLOCO EM PYTHON)
       # def sacar(self, valor: float) -> None: ## inicio do bloco de metodo

            #  if self.saldo >= valor:  ## Inicio do bloco do if

                #     self.saldo -= valor
            
            # fim do bloco do if
            
        # fim do bloco do metedo

    #EXEMPLO EM PYTHON SEM FORMATAR
        # def sacar(self, valor: float) -> None: ## inicio do bloco de metodo
        # if self.saldo >= valor:  ## Inicio do bloco do if
        # self.saldo -= valor
        # fim do bloco do if
        # fim do bloco do metedo

    #  NAO VAI FUNCIONAR ESSE CODIGO, VAI DAR ERRO
    
    
    
    
    
    # ESTRUTURAS CONDICIONAIS 
    # A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressoes logicas sao atendidas
    
        # IF 
            # para criar uma estrutura condicional simples, composta por um unico desvio, podemos utilizar a palavra reservada IF. O comando ira testar a expressao logica, e em caso de retorno verdadeiro as acoes presentes no bloco de codigo do IF serao executadas.
            # EXEMPLO DO IF
                # saldo = 2000.0
                # saque = float(input("Informe o valor do saque: "))
            
                # if saldo >= saque:
                    # print("Realizando saque!")
            
                # if saldo < saque:
                    # print("Saldo insuficiente!")
        
        # IF/ELSE
            # Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas IF e ELSE. Como sabemos se a expressao logica testada no IF for verdadeira, entao o bloco de codigo do if sera executado. Caso contrario o bloco de codigo do ELSE sera executado 
            # EXEMPLO
                # saldo = 2000.0
                # saque = float(input("Informe o valor do saque: "))
            
                # if saldo >= saque:
                    # print("Realizando saque!")
                # else: 
                    # print("Saldo insuficiente!")
            
        # IF/ELIF/ELSE
            # Em alguns cenarios queremos mais  de dois desvios, para isso podemos utilizar a palavra reservada ELIF. O ELIF e composto por uma nova expressao logica, que sera testada e caso retorne verdadeiro o bloco de codigo do ELIF sera executado. Nao existe um numero maximo de ELIFS que podemos utilizar, porem evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do codigo.
            # EXEMPLO
                # opcao = int(input("Informe uma opcao: [1] Sacar \n[2] Extrato: "))
                
                # if opcao == 1:
                    # valor = float(input("Infrome a quantia para o saque: "))
                # elif opcao == 2:
                    # print("Exibindo o extrato...")
                # else:
                    # sys.exit("Opcao invalida")
                    
        # IF aninhado
            # podemos criar estruturas condicionais  aninhadas, para isso basta adicionar estruturas IF/ELIF/ELSE dentro do bloco de codigo de estruturas IF/ELIF/ELSE
            # EXEMPLO
                # if conta_normal:
                    # if saldo >= saque:
                        # print("Saque realizado com sucesso!")
                    # elif saque <= (saldo + cheque_especial):
                        # print("Saque realizado com uso do cheque especial!")
                # elif conta_universitaria:
                    # if saldo >= saque:
                        # print("Saque realizado com sucesso!")
                    # else:
                        # print("Saldo insuficiente!")
                        
        # IF Ternario
            # o IF TERNARIO permite escrever uma condicao  em uma unica linha, ele é composto por tres partes, a primeira parte é o retorno caso a expressao retorne verdadeira, a segunda parte é a expressao logica e a tarceira parte é o retorno caso a expressao nao seja atendida.
            # EXEMPLO
                # status = "Sucesso" if saldo >= saque else "Falha"
                
                # print(f" {status} ao realizar o saque!")
                




# ESTRUTURAS DE REPETICOES
    # SAO ESTRUTURAS UTILIZADAS PARA REPETIR UM TRECHO DE CODIGO UM DETERMINADO NUMERO  DE VEZES. ESSE NUMERO PODE SER CONHECIDO PREVIAMENTE OU DETERMINADO ATRAVES DE UMA EXPRESSAO LOGICA.
    
    # EXEMPLO SEM REPETICAO
        # RECEBA UM NUMERO DO TECLADO  E EXIBA  OS 2 NUMEROS SEGUINTES
        # a = int(input("Informe um numero inteiro: "))
        # print(a)
        # a += 1
            # print(a)
        
        # a += 1
            # print(a)
    # EXEMPLO COM REPETICAO
        # a = int(input("Informe um numero inteiro: "))
        # print(a)
        
        # repita 2 vezes
            # a += 1
            # print(a)
    # ATENCAO POR ENQUANTO NAO TEM NENHUMA SINTAXE O REPITA.
    
    # COMANDO FOR
        # O comando FOR é usado para percorrer um objeto iteravel. Faz sentido usar FOR quando sabemos o numero exato de vezes que nosso bloco de codigo deve ser executado, ou quando queremos percorrer um objeto iteravel.
        # A STRING é um objeto iteravel como exemplo.
        
        #EXEMPLO - FOR
            # texto = input("Informe um texto: ")
            # VOGAIS = "AEIOU"
            
            # for letra in texto:
                # if letra.upper() in VOGAIS:
                    # print(letra, end=" ")
                    
            # print()  # adiciona uma quebra de linha
            # UPPER deixa as letras em maiusculo