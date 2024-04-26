notas = [1,2,3,4,5,6,7,8,9,10,11,12]
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
# #     if nota <= notaMenor:
# #         notaMenor = nota 
# # print (notaMenor)

# rango1 = 0
# rango2 = 0
# rango3 = 0
        
# for nota in notas:
#     if nota >= 0.0 and nota <= 1.99:
#         rango1 += 1
#     elif nota >= 2.0 and nota <= 3.49:
#         rango2 += 1
#     elif nota >= 3.5 and nota <= 5.0:
#         rango3 +=1
# if rango1 > rango2 and rango1 > rango3:
#     print("rango1")
# elif rango2 > rango1 and rango2 > rango3:
#     print ("rango2")
# elif rango3 > rango2 and rango3 > rango1:
#     print("rango3")
# print(rango1)
# print(rango2)
# print(rango3)

menores = []
for i in range(len(notas)):
    menorLocal = 0
    for a in range(len(notas)):
        if notas[i] > notas[a]:
            menorLocal += 1
    menores.append(menorLocal)
menores.sort()

print(menores[round(len(notas)/2)])
print(menores)