


carrinho_id =  5        # postData.get('carrinho_id')
anel_id = 3
quantidade = 12
carrinho = {'1': [5, 'Anel No Solitário em Ouro', '7'], '2': [5, 'Anel Ouro Solitario 18k', '6'], '3': [5, 3, 12]}


def get_key(val, session):
        for key, value in session.items():
            if val == key:
                return True
    
        return False


loop = True
n = 1
ns = str(n)

while loop == True:
    if get_key(ns, carrinho):
        print(n)
        n += 1
        ns = str(n)
        print(ns)
    else:
        print(f'-->>{carrinho}')
        loop = False
        novo_carrinho = {ns: [carrinho_id, anel_id, quantidade ]}
        carrinho.update(novo_carrinho)
        print(carrinho)
        exit()


#########################################
