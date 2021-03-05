cnpj = input('Digite o CNPJ: ')
cnpj_validador = cnpj[:-2].replace('.', '').replace('/', '').replace('-', '')

if len(cnpj_validador) == 12 and cnpj_validador.isdigit():

    # Primeiro dígito
    i = 5
    soma = 0
    for x in cnpj_validador:
        soma += int(x) * i
        i -= 1
        if i == 1:
            i = 9

    primeiro_digito = 11 - (soma % 11) if 11 - (soma % 11) <= 9 else 0
    cnpj_validador += str(primeiro_digito)

    # Segundo dígito
    i = 6
    soma = 0
    for x in cnpj_validador:
        soma += int(x) * i
        i -= 1
        if i == 1:
            i = 9

    segundo_digito = 11 - (soma % 11) if 11 - (soma % 11) <= 9 else 0
    cnpj_validador += str(segundo_digito)

    # Conclusão
    if (cnpj_validador[-2:] == cnpj[-2:]):
        print('CNPJ válido')
    else:
        print('CNPJ inválido')

else:
    print('CNPJ inválido')


