curso ="curso de Python"
frutas =["laranja", "uva", "limão"]
saques = [1500, 100]

print("Python" in curso) 
print("maçã" not in frutas)
print(200 in saques)

print('TESTE SE AS MEDIDAS DE  RETAS FORMARÃO UM TRIANGULO')
a = float(input('Digite o valor lado A do triangulo> '))
b  = float(input('Digite o lado o valor B do triangulo > '))
c = float(input('Digite o lado C o valor do triangulo > '))
s = a + b
s2 = b + c
s3 = a + c
if c < s and a < s2 and b < s and c < s2 and b < s2 and b < s3 :
    print(' ---É um triangulo porque a soma de dois lados  é maior que o outro lado do triangulo---')
else :
        print ('---Não é um triangulo---')