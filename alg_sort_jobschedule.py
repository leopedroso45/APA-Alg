#!/usr/bin/python3
# -*- coding: utf-8 -*-

DEFAULT_OUT = "out_alg_sort_selection.txt"
DEFAULT_SEED = None

DEFAULT_N_START = 1
DEFAULT_N_STOP = 10
DEFAULT_N_STEP = 1
DEFAULT_TRIALS = 3
import random
from subprocess import Popen, PIPE
from time import sleep, time
from multiprocessing import Process
import shlex
import json

import sys
import os
import argparse
import logging
import subprocess

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import matplotlib.colors as colors
import matplotlib.cm as cmx

import timeit


def sort_jobschedule(backlog):
	# comprimento do backlog
	comprimento_backlog = len(backlog)
	quantidade_tarefas = 6
	# ordena todas as tarefas de acordo com a ordem decrescente de ponto de funcao
	for i in range(comprimento_backlog):
		for j in range(comprimento_backlog - 1 - i):
			if backlog[j][2] < backlog[j + 1][2]:
				backlog[j], backlog[j + 1] = backlog[j + 1], backlog[j]

	# pra manter/acompanhar slots com tempo livre
	# cria array com a quantidade de
	resultado = [False] * quantidade_tarefas

	# pra manter os resultados das sequencias de tarefas
	job = ['-1'] * quantidade_tarefas

	# itera sob todas tarefas
	for i in range(len(backlog)):

		# encontra um slot de tempo livre para a tarefa
		# bom notar que nos comecamos pelo ultimo slot possivel
		for j in range(min(quantidade_tarefas - 1, backlog[i][1] - 1), -1, -1):

			# slot disponivel encontrado
			if resultado[j] is False:
				resultado[j] = True
				job[j] = backlog[i]
				break

	f = open("resultado.txt", "w")
	f.write(str(job));

	return (job)


def gera_workload(n):
    crud = ['Cadastrar','Editar', 'Excluir', 'Consultar']
    tipo = ['Usuarios', 'Tarefas', 'Comidas', 'Mercadorias', 'Funcionarios', 'Administradores', 'Gerentes', 'Caixas', 'Turnos']
    workload = []
    for i in range (n):
        nome_tarefa= random.choice(crud)+' '+random.choice(tipo)
        tarefa = [nome_tarefa, random.randint(1, 6),random.randint(1, 10), i]
        workload.append(tarefa)
    return workload

def main():
	# Definição de argumentos
	parser = argparse.ArgumentParser(description='JobSchedule')
	help_msg = "arquivo de saída.  Padrão:{}".format(DEFAULT_OUT)
	parser.add_argument("--out", "-o", help=help_msg, default=DEFAULT_OUT, type=str)

	help_msg = "semente aleatória. Padrão:{}".format(DEFAULT_SEED)
	parser.add_argument("--seed", "-s", help=help_msg, default=DEFAULT_SEED, type=int)

	help_msg = "n máximo.          Padrão:{}".format(DEFAULT_N_STOP)
	parser.add_argument("--nstop", "-n", help=help_msg, default=DEFAULT_N_STOP, type=int)

	help_msg = "n mínimo.          Padrão:{}".format(DEFAULT_N_START)
	parser.add_argument("--nstart", "-a", help=help_msg, default=DEFAULT_N_START, type=int)

	help_msg = "n passo.           Padrão:{}".format(DEFAULT_N_STEP)
	parser.add_argument("--nstep", "-e", help=help_msg, default=DEFAULT_N_STEP, type=int)

	help_msg = "tentativas.        Padrão:{}".format(DEFAULT_N_STEP)
	parser.add_argument("--trials", "-t", help=help_msg, default=DEFAULT_TRIALS, type=int)

	# Lê argumentos from da linha de comando
	args = parser.parse_args()

	print("asdyughasuyidsauy")

	trials = args.trials
	f = open(args.out, "w")
	f.write("#Jobschedule\n")
	f.write("#n time_s_avg time_s_std (for {} trials)\n".format(trials))
	np.random.seed(args.seed)
	print("##################################")
	print("NSTART")
	print(args.nstart)
	print("##################################")
	print("NSTOP")
	print(args.nstop+1)
	print("##################################")
	print("NSTEP")
	print(args.nstep)
	for n in range(args.nstart, args.nstop+1, args.nstep):
		#print(n)
		resultados = [0 for i in range(trials)]
		tempos = [0 for i in range(trials)]
		for trial in range(trials):
			#print("\n-------")
			#print("n: {} trial: {}".format(n, trial+1))
			entrada = gera_workload(n)
			#print("Entrada: {}".format(entrada))
			tempo_inicio = timeit.default_timer()
			resultados[trial] = sort_jobschedule(entrada)
			tempo_fim = timeit.default_timer()
			tempos[trial] = tempo_fim - tempo_inicio
			#print("Saída: {}".format(resultados[trial]))
			#print('Tempo: {} s'.format(tempos[trial]))
			#print("")

		tempos_avg = np.average(tempos)  # calcula média
		tempos_std = np.std(a=tempos, ddof=False)  # ddof=calcula desvio padrao de uma amostra?


		f.write("{} {} {}\n".format(n, tempos_avg, tempos_std))
	f.close()


if __name__ == '__main__':
	sys.exit(main())
