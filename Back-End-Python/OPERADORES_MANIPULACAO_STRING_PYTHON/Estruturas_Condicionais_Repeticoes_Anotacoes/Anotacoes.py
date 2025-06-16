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

# Esse Codigo Vai FUNCIONAR EM JAVA Mesmo Sem Identar


# UTILIZANDO ESPACOS
# Existe uma convencao em Python, que define as boas praticas para escrita de codigo na linguagem. Nesse  documento e indicado utlizar 4 espacos em branco por nivel de indentacao,  ou seja, a cada novo bloco adicionamos 4 novos  espacos em branco

#EXEMPLO EM PYTHON (BLOCO EM PYTHON)
def sacar(self, valor: float) -> None: ## inicio do bloco de metodo

    if self.saldo >= valor:  ## Inicio do bloco do if

        self.saldo -= valor
    
    # fim do bloco do if
    
# fim do bloco do metedo

#EXEMPLO EM PYTHON SEM FORMATAR
# def sacar(self, valor: float) -> None: ## inicio do bloco de metodo
# if self.saldo >= valor:  ## Inicio do bloco do if
# self.saldo -= valor
# fim do bloco do if
# fim do bloco do metedo

#  NAO VAI FUNCIONAR ESSE CODIGO, VAI DAR ERRO