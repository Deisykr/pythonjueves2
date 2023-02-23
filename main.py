#condicionales con python

nivelAgua=int(input("Digita el nivel de agua"))
if nivelAgua>=0 and <=250:
    print(f"El nivel de agua es muy bajo{nivelAgua} U")
elif nivelAgua>=250 and <=400:
    print(f"El nivel del agua es óptimo{nivelAgua} U")
elif nivelAgua>=450:
    print(f"nivel de agua critico EVACUE{nivelAgua} U")
else:
    print("revisar controles")