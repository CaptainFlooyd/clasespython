primero_valor = input('DIGITE UM VALOR: ')
segundo_valor = input('DIGITE OUTRO VALOR: ')
if primero_valor > segundo_valor:
    print(primero_valor,"Esse valor é maior que",segundo_valor)
elif segundo_valor > primero_valor:
    print(segundo_valor, "É maior que", primero_valor)
elif primero_valor == segundo_valor:
    print(primero_valor, 'é igual á',segundo_valor)


else:
    print('Digite apenas números')



