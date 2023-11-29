# cadastro de estudante

# apresentação
print('\n\t\t\tcadastro n1')
x = input('Nome do aluno')
y = int(input('Nota final dele'))
z = input('qual curso do estudante ')


print('\n\t\t\tcadastro n2')
a = input('Nome da aluna')
b = int(input('Nota final dela'))
c = input('qual curso da estudante')

# processamento
estudante = {'Nome1': 'Informe o nome...', 'Nota1':0.0, 'Curso1': 'Nome do Curso'}
estudante2 = {'Nome2': 'Informe o nome...', 'Nota2':0.0, 'Curso2': 'Nome do Curso'}

estudante['Nome1'] = x
estudante['Nota1'] = y
estudante['Curso1'] = z

estudante2['Nome2'] = a
estudante2['Nota2'] = b
estudante2['Curso2'] = c

# saida
print('\n\t\t\tcadastro 1 concluido')
print(f'Nome.................{estudante["Nome1"]}')
print(f'Nota.................{estudante["Nota1"]}')
print(f'Curso.................{estudante["Curso1"]}')

print('\n\t\t\tcadastro 2 concluido')
print(f'Nome.................{estudante2["Nome2"]}')
print(f'Nota.................{estudante2["Nota2"]}')
print(f'Curso.................{estudante2["Curso2"]}')



