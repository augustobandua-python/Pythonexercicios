salário = float(input('Qual é o salário do funcionario? €'))
novo = salário + (salário * 10 / 100)
print('Um funcionario que ganhava €{:.2f}, com aumento de 10% passará a ganhar €{:.2f} '.format(salário,novo))
