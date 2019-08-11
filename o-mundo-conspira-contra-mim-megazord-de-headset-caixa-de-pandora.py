# coding: utf-8
import os

campeoes = []

def inserirCampeao():
    file = open("manuel-padua.txt", "a")
    print("Nome do campeão: ", end = '')
    nome = input()
    print("Data que o Manuel jogou: ", end = '')
    data = input()

    resultado = nome + "," + data + "\n"
    print("Campeão registrado!")

    file.write(resultado)
    file.close()

def lerArquivo():
    file = open("manuel-padua.txt", "r")
    for line in file:
        dados = line.split(",")
        dados[0] = dados[0].strip('\n')

        if(campeoes.count(dados) == 0):
            campeoes.append(dados)
    file.close()

def imprimirLista():
    lerArquivo()

    for entrada in campeoes:
        print("O nome do campeão que o MANUEL PÁDUA reclamou: " + entrada[0])
        print("A data da partida que o MANUEL PÁDUA fez a reclamação: " + entrada[1])
        print()

while(True):
    print("1) Registrar campeão")
    print("2) Imprimir lista de reclamações")
    print("3) Fechar o programa")
    print("Digite uma opção: ", end = '')
    entrada = input()

    if(entrada == "1"):
        inserirCampeao()
    elif(entrada == "2"):
        print()
        imprimirLista()
        print("Aperte enter para continuar")
        os.system("cls")
        input()
    elif(entrada == "3"):
        break
    else:
        print("Comando inválido!")

    print()