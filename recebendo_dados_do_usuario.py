# curso-de-Python

"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo string
Em Python , string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simpes triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""
# - Aspas duplas triplas -> """Angelina Jolie"""

# Entrada de dados
# print("Qual seu nome?")
# nome = input() # Input -> Entrada 

nome = input('Qual o seu nome? ')

# Exemplo de print 'antigo' 2.x 
#print('Seja bem-vindo(a) %s ' % nome)

# Exemplo de print 'moderno' 3.x
#print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'seja bem-vindo(a){nome}')

# print("Qual sua idade ? ")
# idade= input()
idade = int(input('Qual sus idade ? '))


# Processamento

# Saída 
# Exemplo de print 'antigo' 2.x 
#print('A %s tem %s anos ' % (nome , idade))

# Exemplo de print 'moderno' 3.x
#print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'A {nome} tem {idade} anos ')

"""
# int(idade) => cast

cast é a 'conversão' de um tipo de dado para outro.
"""
print(f'A {nome} nasceu em {2018 - idade}') 

