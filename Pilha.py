#em uma pilha o primeiro a chegar é o ultimo a sair, só sai o que chegou por ultimo
panquecas=[]
posicaoultimo=len(panquecas)
while True:
    print("Tem %d panquecas na fila!" % posicaoultimo)

    if (len(panquecas))>0:
        print("As panquecas na pilha são .: ")
        for i, num in enumerate(panquecas):
            print("Passageiro.: [%d] --> %s" % (i+1,num))

    print("#"*80)

    print("Digite 1 para adicionar uma panqueca na fila.: ")
    print("Digite 2 tirar panqueca do topo da pilha .: ")
    print("Digite 3 para sair")
    acao = int(input("Operação 1, 2 ou 3? "))
    if   acao == 1:
        #ultimo = str(posicaoultimo+1)
        panquecas.append("panqueca%d"%(posicaoultimo+1))
        posicaoultimo+=1
    elif acao == 2:
        if (len(panquecas)) > 0:
            panquecas.pop(-1)#exclui o topo da pilha
            posicaoultimo-=1
        else:
            print("")
            print("#"*80)
            print("")
            print("ERROR ao excluir pilha vazia")
            print("")
            print("#"*80)
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
