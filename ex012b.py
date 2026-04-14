preço = float(input('Qual é o preço deste produto com desconto? €'))
novo = preço - (preço * 50 /100)
print('O produto que custava €{:.2f}, na promoção com desconto de 50%, vai custar €{:.2f}'.format(preço, novo))
