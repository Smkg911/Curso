notas = [4.0,2.0,4.6,3.1,2.7,4.2,0.5,1.6,0.8,1.9,5.0,4.1]
notaMayor = 0
for nota in notas:
    if nota >= notaMayor:
        notaMayor = nota
print(notaMayor)

# for indice in range(12):
#         if ((notas[indice]*0.05)+notas[indice]) <= 5.0:
#             notas[indice] = notas[indice] + (notas[indice] *0.05)
# print(notas)

# for indice in range(12):
#     if notas[indice] > 4.0: 
#         notas[indice] -= 0.5
#     elif notas[indice] < 2.0: 
#         notas[indice] += 0.5
# print (notas)

# notaMenor = 5.0
# for nota in notas:
#     if nota <= notaMenor:
#         notaMenor = nota 
# print (notaMenor)

rango1 = 0
rango2 = 0
rango3 = 0
        
for nota in notas:
    if nota >= 0.0 and nota <= 1.99:
        rango1 += 1
    elif nota >= 2.0 and nota <= 3.49:
        rango2 += 1
    elif nota >= 3.5 and nota <= 5.0:
        rango3 +=1
if rango1 > rango2 and rango1 > rango3:
    print("rango1")
elif rango2 > rango1 and rango2 > rango3:
    print ("rango2")
elif rango3 > rango2 and rango3 > rango1:
    print("rango3")
print(rango1)
print(rango2)
print(rango3)