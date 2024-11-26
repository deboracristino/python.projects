# Atribuição Simples
saldo = 300

print(saldo)

#Atribuição com adição
saldo = 200
saldo += 230
print


s=float(input('Digite o salário do funcinário? > '))
s1 = s +( s * 15 /100)
s2 = s +(s * 10 /100)
if s <= 1250:
    print('Voce teve um aumento salarial de 15 por cento , seu salário agora é {:.2f}'. format(s1))
else:
    print ('Voce teve um aumento salarial de 10 por cento, seu valor salarial agora é {:.2f}'.format(s2))