texA = input('Digite o texto A: ')
texB = input('Digite o texto B: ')

print("tamanho(A) - tamanho(B) = " + str(len(texA)-len(texB)))
print("A + B = " + texA + texB)
print("A contém B = " + str(texB in texA))
print("A contém B = " + str(texA in texB))
print("Primeira letra de A = " + str(texA[0]))
print("Primeira letra de B = " + str(texB[0]))
print("Última letra de A = " + str(texA[-1]))
print("Última letra de B = " + str(texB[-1]))