






car = 3500.10

valor = round(car)
valor = str(car).replace('.', ',')

print(valor)

def real_br_money_mask(my_value):
    a = '{:,.2f}'.format(float(my_value))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return type(c.replace('v','.'))

print(real_br_money_mask(3500.10))