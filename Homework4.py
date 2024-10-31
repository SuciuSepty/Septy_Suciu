import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]
litera = []
litere_incercate_afisare = ""
gasit= False
# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

print(" ".join(progres))
print(f"Incercari ramase: {incercari_ramase}")

while incercari_ramase > 0 and "_" in progres:
    gasit=False
    litera = input("Introdu o literă: ").lower()
    if len(litera) != 1 or not litera.isalpha() or litera in litere_incercate:
        print("Te rog sa introduci o litera valida sau care nu a mai fost utilizata precedent")
        continue
    litere_incercate.append(litera)
    for i in range(len(cuvant_de_ghicit)):
        if litera == cuvant_de_ghicit[i]:
            progres[i] = litera
            gasit = True

    if not gasit:
        incercari_ramase -= 1
    print(" ".join(progres))
    print(f"Incercari ramase: {incercari_ramase}")
    print(f"Litere folosite: {', '.join(litere_incercate)}")

if "_" not in progres:
    print(f"Felicitări! Ai ghicit cuvântul: {cuvant_de_ghicit}")
else:
    print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}")