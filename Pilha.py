#em uma pilha o primeiro a chegar é o ultimo a sair, só sai o que chegou por ultimo
panquecas=["panqueca1","panqueca2","panqueca3","panqueca4","panqueca5","panqueca6"]
posicaoultimo=len(panquecas)
while True:
    print("Tem %d panquecas na fila!" % posicaoultimo)
    print("As panquecas na pilha são .: ")
    for i, num in enumerate(panquecas):
        print("Passageiro.: [%d] --> %s" % (i+1,num))

    print("#"*80)

    print("Digite 1 para adicionar uma panqueca na fila.: ")
    print("Digite 2 tirar panqueca do topo da pilha .: ")
    print("Digite 3 para sair")
    acao = int(input("Operação 1, 2 ou 3? "))
    if   acao == 1:
        ultimo = str(posicaoultimo+1)
        panquecas.append('panqueca'+ultimo)
        posicaoultimo+=1
    elif acao == 2:
        if (len(panquecas)) > 0:
            panquecas.pop(-1)#exclui o topo da pilha
            posicaoultimo-=1
        else:
            print("A fila está vazia")
    elif acao == 3:
        print("Processo finalizado")
        break
