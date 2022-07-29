#Num universo de 4 alunos, sortear pelo nome um deles
import random

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

listaAlunos = [aluno1,aluno2,aluno3,aluno4]
escolhido = random.choice(listaAlunos)

print(f'O aluno escolhido foi {escolhido}')