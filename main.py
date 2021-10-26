def CONCESSIONARIA():
    fila = []
    
    while True:
        print('CONCESSIONÁRIA')
        print('1 - VENDAS')
        print('2 - PRE-VENDA')
        print('3 - REMOVER PRE-VENDA')
        print('4 - Sair')
        opcao = int(input('>>'))
        if opcao == 1:
            nome = str(input('Nome do Cliente: '))
            fila.append("NOME:")
            fila.append(nome)
            marca = str(input('Marca do Veículo: '))
            fila.append("MARCA:")
            fila.append(marca)
            modelo = str(input('Modelo do Veículo: '))
            fila.append("MODELO:")
            fila.append(modelo)
            ano = int(input('Ano do Carro: '))
            fila.append("ANO:")
            fila.append(ano)
            preco = float(input('Valor do Veiculo: '))
            fila.append("PREÇO:")
            fila.append(preco)
            print('VENDA REALIZADA COM SUCESSO!')
        
        elif opcao == 2:
            print('\n', fila)
        
        elif opcao == 3:
            del fila[0:10]
            print('Venda removida com Sucesso!')
            print('PRE-VENDAS ATUALIZADA!')
            print('\n', fila)
            
        
        elif opcao == 4:
            break
        else:
            print('Opção Invalida!')

CONCESSIONARIA()    
