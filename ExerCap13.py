import os
import shutil
# Ex1**: Criar e ler um Arquivo**
with open('meuarquivo.txt', 'w') as arquivo:
    arquivo.write('Este é um arquivo criado em Python!\n')
    arquivo.write('Espero que esteja tudo bem.\n')

# # # Lendo o arquivo
with open('meuarquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# # Ex2**: Cria um Diretório**
import os
with open('Repository', 'w') as new_arquivo:
    os.mkdir('new_arquivo')

# Ex3**: Renomear um Diretório**
os.rename('new_arquivo', 'New_Archive')

# Ex4**: Listar Arquivos em um Diretório** 
with os.scandir('C:/Users/Aluno/Desktop/Aluno/26 04 2025/') as input:
    for arquivo in input:
        if arquivo.is_file():
            print(f'Arquivo encontrado: {arquivo.name}')

# Ex5**: Copiar Arquivos em um Diretório**
shutil.copytree('C:/Users/Aluno/Desktop/Aluno/26 04 2025/', 'Copy')

# Ex6**: Remover**
shutil.rmtree('C:/Users/Aluno/Desktop/Aluno/26 04 2025/Copy/')