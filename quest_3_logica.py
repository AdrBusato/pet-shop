# Exercício 3/4 da atividade prática

# Início da função dog_weight()
def dog_weight():
    print('------------------------- MENU 1 DE 3 - cachorro peso --------------------------')
    while True:
        try:
            # weightD : peso do cachorro
            weightD = int(input('Entre com o peso do cachorro (KG): '))
            if weightD < 3:
                return 40
            elif 3 <= weightD < 10:
                return 50
            elif 10 <= weightD < 30:
                return 60
            elif 30 <= weightD < 50:
                return 70
            elif weightD > 50:
                print('Não aceitamos cachorros tão grandes')
            else:
                print('Por favor, entre com o peso do cachorro novamente.')
                continue  # retorna para a pergunta
        except ValueError:  # caso o usuário digite a letra B ou números com decimais por exemplo...
            print('Você digitou um valor não numérico!')
# Fim da função dog_weight()

# Início da função dog_cut()

def dog_cut():
    print('------------------------- MENU 2 DE 3 - cachorro pelo --------------------------')
    while True:
        cutD = input('Deseja adicionar mais algum serviço \n' +
                     'c- Pelo Curto \n' +
                     'm- Pelo Médio \n' +
                     'l- Pelo Longo \n' +
                     '>> ')  # cutD : pelo do cachorro
        cutD = cutD.lower()  # caracteres se tornarem minúsculos caso sejam digitados em caixa alta
        if cutD == 'c':
            return 1.00
        elif cutD == 'm':
            return 1.50
        elif cutD == 'l':
            return 2.00
        else:
            print('Pare de digitar opções diferentes de c/m/l')
            continue  # retorna para o início do laço
# Fim da função dog_cut()

# Início da função dog_extra()

def dog_extra():
    print('------------------------- MENU 3 DE 3 - cachorro extra -------------------------')
    acumulator = 0
    while True:
        add_extra = input('Deseja adicionar mais algum serviço? \n' +
                          '1- Corte de Unhas -> R$ 10,00 \n' +
                          '2- Escovar Dentes -> R$ 12,00 \n' +
                          '3- Limpeza de Orelhas -> R$ 15,00 \n' +
                          '0- Não desejo mais nada (Encerrar pedido) \n' +
                          '>> ')
        if add_extra == '1':
            acumulator = acumulator + 10
            continue  # volta para o início do while True
        elif add_extra == '2':
            acumulator = acumulator + 12
            continue  # volta para o início do while True
        elif add_extra == '3':
            acumulator = acumulator + 15
            continue  # volta para o início do while True
        elif add_extra == '0':
            return acumulator
        else:
            print('Pare de digitar opções diferentes de 0/1/2/3')

# Fim da função dog_extra()

# Início do Main
print('-------------------- Bem-vindo ao pet shop Adrielson Busato --------------------')
weight = dog_weight()
cut = dog_cut()
extra = dog_extra()
total = (weight * cut) + extra
print('O total a pagar em (R$): {:.2f} (peso: {} * pelo: {} + extra(s): {})' .format(
    total, weight, cut, extra))
