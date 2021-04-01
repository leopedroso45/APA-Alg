import gera_workload as gw
import argparse
import sys

parser = argparse.ArgumentParser(description='JobSchedule with deadlines.')
parser.add_argument('-w','--workload',help='workload size')

def main():
    #parse dos argumentos
    args = parser.parse_args()

    #pega a carga do terminal
    cargaworkload = int(args.workload)

    #verifica se a carga eh maior q a qtd de tarefas diarias
    if(cargaworkload<=6):
        print("carga precisa ser maior que 6")
        sys.exit(0)

    #gera o workload
    tarefas = gw.gera_workload(int(args.workload));

    #escreve o workload em um arquivo
    f = open("workload.txt", "w")
    f.write(str(tarefas));

    #chama o job schedule
    melhorordem = printJobScheduling(tarefas, 6)

    print(melhorordem)


def printJobScheduling(backlog, quantidade_tarefas):
    # comprimento do backlog
    comprimento_backlog = len(backlog)

    #ordena todas as tarefas de acordo com a ordem decrescente de ponto de funcao
    for i in range(comprimento_backlog):
        for j in range(comprimento_backlog - 1 - i):
            if backlog[j][2] < backlog[j + 1][2]:
                backlog[j], backlog[j + 1] = backlog[j + 1], backlog[j]

    #pra manter/acompanhar slots com tempo livre
    #cria array com a quantidade de
    resultado = [False] * quantidade_tarefas

    #pra manter os resultados das sequencias de tarefas
    job = ['-1'] * quantidade_tarefas

    #itera sob todas tarefas
    for i in range(len(backlog)):

        #encontra um slot de tempo livre para a tarefa
        # bom notar que nos comecamos pelo ultimo slot possivel
        for j in range(min(quantidade_tarefas - 1, backlog[i][1] - 1), -1, -1):

            # slot disponivel encontrado
            if resultado[j] is False:
                resultado[j] = True
                job[j] = backlog[i]
                break

    # printa a sequencia de tarefas
    return(job)

'''
# Exemplo de entrada
arr = [['a', 2, 100], 
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1 25],
       ['e', 3, 15]]
'''


main()
