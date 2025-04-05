
# 1* - Peça para o usuário digitar um número, verifique se um número é positivo, negativo ou zero.
print ('Exerc1')
escolha = input('Digite um numero inteiro qualquer:')
if escolha > '0':
    print(' O numero é positivo!')
elif escolha == '0':
    print(' O numero é zero!')
else: 
    print(' O numero é negativo!')


# 2* - Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com base na idade.
print ('Exerc2')
choice =  input('Digite sua idade em anos (não digite os meses):')
if choice >= '16':
    print('Você está apto a votar nas próximas eleições!')
else:
    print('Você não poderá votar nas próximas eleições!')



# 3* - Declara uma variável com um número qualquer, determine se um número é par ou ímpar.
print ('Exerc3')
variable = float(input('Declare uma variável com um numero decimal qualquer:  '))
if variable % 2 ==0:
    print('Sua variável declarada é um numero par!')
else:
    print('Sua variável declarada não é um numero par!')



# 4* - Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo é equilátero, isósceles ou escaleno.
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.
print ('Exerc4')
A = int(input('Digite o tamanho do lado A do triangulo (use apenas numero inteiro positivo:)'))
B = int(input('Digite o tamanho do lado B do triangulo (use apenas numero inteiro positivo:)'))
C = int(input('Digite o tamanho do lado C do triangulo (use apenas numero inteiro positivo:)'))
if A==B==C:
    print('O triangulo é equilátero!')
elif A==B or B==C:
    print('O triangulo é isósceles!')
else:
    print('O triangulo é escaleno')


# 5* - Determine se um número é múltiplo de 5 e 7.
print ('Exerc5')
mult5e7 = int(input('Digite um numero qualquer inteiro positivo:  '))
if mult5e7 % 5==0 and mult5e7 % 7==0:
    print('Este numero é multiplo de 5 e 7!')
else:
    print('Este numero não é multiplo de 5 e 7!')


# 6* - Verifique se um número é positivo e maior que 10.
print ('Exerc6')
posandover10 = float(input('Digite um numero qualquer:   '))
if posandover10 >10:
    print('O numero é positivo e maior que 10')
elif posandover10 <=10 and posandover10 >0:
    print('O numero é positivo mas é menor que 10')
elif posandover10 == 0:
    print('O numero é zero')
else:
    print('O numero é negativo')

# 7* - Verifique se um número é divisível por 3 ou 5.
print ('Exerc7')
div3e5 = int(input('Digite um numero qualquer inteiro:  '))
if div3e5 % 3==0 and div3e5 % 5 ==0:
     print('O numero é divisível por 3 ou 5')
else:
     print('O numero não é divisível por 3 ou 5')