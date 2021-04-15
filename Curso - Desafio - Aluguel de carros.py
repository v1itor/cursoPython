valordias = int(input('quantos dias o carro ficou com você? ')) *60
valorkm = int(input('quantos km você andou com o carro? ')) *0.15
print('Você deve R${:.2f} a loja no qual alugou o carro' .format((valordias + valorkm)))