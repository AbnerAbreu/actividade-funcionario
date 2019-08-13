
nome = input('O seu nome:')
horas = int(input('numero de horas:'))
valor_hora = float(input('o valor que receber por hora:'))
salario = horas * valor_hora

print('O funcionário {} recebe o salário de R${}'.format(nome,salario))