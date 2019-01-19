#em uma fila o primeiro a chegar é o primeiro a sair
passageiros=["neri","selvino","romilda","lisiane","giulia","julio"]
posicaoultimo=len(passageiros)
while True:
    print("Tem %d passageiros na fila!" % posicaoultimo)
    print("Os passageiros na fila são .: ")
    for i, num in enumerate(passageiros):
        print("Passageiro.: [%d] --> %s" % (i+1,num))

    print("#"*80)

    print("Digite 1 para adicionar uma pessoa na fila.: ")
    print("Digite 2 para dizer que a pessoa foi atendida (saiu da fila)) .: ")
    print("Digite 3 para sair")
    acao = int(input("Operação 1, 2 ou 3? "))
    if   acao == 1:
        pessoa=input("Digite o nome da pessoa que entrou na fila .: ")
        passageiros.append(pessoa)
        posicaoultimo+=1
    elif acao == 2:
        if (len(passageiros)) > 0:
            passageiros.pop(0)#exclui a primeira posição da fila
            posicaoultimo-=1
        else:
            print("A fila está vazia")
    elif acao == 3:
        print("Processo finalizado")
        break
    else:
        print("#"*80)
        print("ERROR")
        print("#"*80)
        print("")
        print("Condição inválida, escolha 1, 2 ou 3: ")
        print("")
        print("#"*80)
