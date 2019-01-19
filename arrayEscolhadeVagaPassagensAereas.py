#Escolha de assentos vagos de uma rota de avião/onibus
print("-"*80)
assentosVagos=[12,15,0,3,11,99]
qtdRotas=len(assentosVagos)
for rota, assentosDisponiveis in enumerate(assentosVagos):
    print("Rota %d possui %d assentos vagos" % (rota+1, assentosDisponiveis))
while True:
    rotaEscolhida=int(input("Escola uma rota de 1 a %d (para finalizar digite 0)" % qtdRotas))
    if rotaEscolhida == 0:
        print("Processo finalizado")
        break
    if rotaEscolhida >qtdRotas or rotaEscolhida<0:
        print("-"*80)
        print("")
        print("Rota inexistente, escolha uma rota válida \n de 1 até ", qtdRotas)
        print("")
        print("-"*80)
    else:
        qtdPassagens=int(input("(Rota com %d assentos disponíveis, qtd de passagens da compra?  " %assentosVagos[rotaEscolhida-1]))
        if qtdPassagens > assentosVagos[rotaEscolhida-1]:
            print("Qtd de passagens maior que a disponível")
        elif qtdPassagens <1:
            print("Escolha uma qtd de passagens maior que zero (0)")
            for rota, assentosDisponiveis in enumerate(assentosVagos):
                print("Rota %d possui %d assentos vagos" % (rota+1, assentosDisponiveis))

        else:
            assentosVagos[rotaEscolhida-1] -=qtdPassagens
            print("Compra realizada com sucesso")
            print("Rota escolhida.: ", assentosVagos[rotaEscolhida-1])
            print("Qtd passagens efetuada.: ",qtdPassagens)
            break
