temp = dict()
estoque = list()

print('ATACADISTA')
print('-' * 30)

while True:
    print('ATACADISTA')
    print('-' * 30)

    print('1 -> CADASTRAR PRODUTO')
    print('2 -> LISTA PRODUTOS')
    print('3 -> BUSCAR PRODUTO')
    print('4 -> MOSTRAR VALOR DO ESTOQUE ')
    print('5 -> ENCERRAR PROGRAMA')

    resp = int(input('Digite a opção desejada:'))
    if resp == 1:
        temp['Nome'] = str(input('Digite o nome do produto:'))
        temp['Preço'] = float(input(f'Digite o preço de {temp["Nome"]}'))
        temp['Estoque'] = int(input('Digite a quantidade no estoque'))
        estoque.append(temp.copy())
        temp.clear()
        print('PRODUTO CADASTRADO!')
    elif resp == 2:
        for p in estoque:
            print(f'Produto: {p["Nome"]} | Preço: {p["Preço"]} | Quantidade: {p["Estoque"]}')
    elif resp == 3:
        buscador = str(input('Digite o nome do produto para saber se ele tem em estoque')).lower()
        resultadobusca = 'Produto não encontrado'
        if len(estoque) == 0:
                print('Nenhum produto cadastrado!')
        for p in estoque:
            if buscador == p["Nome"].lower():
                resultadobusca = (f'Produto: {p["Nome"]} | Preço: {p["Preço"]} | Quantidade: {p["Estoque"]}')
        print(resultadobusca)
    elif resp == 4:
         valortotal = 0
         for p in estoque:
           valortotal += p['Estoque'] * p['Preço'] 
         print(f'O valor total do estoque é R${valortotal:.2f}')
    elif resp == 5:
        print('FIM DO PROGRAMA OBRIGADO!')
        break
    else:
        print('Opção invalida!')