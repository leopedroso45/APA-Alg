import random

def gera_workload(n):
    crud = ['Cadastrar','Editar', 'Excluir', 'Consultar']
    tipo = ['Usuarios', 'Tarefas', 'Comidas', 'Mercadorias', 'Funcionarios', 'Administradores', 'Gerentes', 'Caixas', 'Turnos']
    workload = []
    for i in range (n):
        nome_tarefa= random.choice(crud)+' '+random.choice(tipo)
        tarefa = [nome_tarefa, random.randint(1, 6),random.randint(1, 10), i]
        workload.append(tarefa)
    return workload
