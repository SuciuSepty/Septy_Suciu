meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []
istoric_tavi= []

for i in range(len(studenti)):
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    tavi.pop()
    istoric_comenzi.append([student, comanda])

    print(student + " a comandat " + comanda + ".")


cefe=len([istoric for istoric in istoric_comenzi if istoric[1] == "ceafa"])
papanas=len([istoric for istoric in istoric_comenzi if istoric[1] == "papanasi"])
guiasu=len([istoric for istoric in istoric_comenzi if istoric[1] == "guias"])

print(f"S-au comandat {guiasu} guias, {cefe} ceafa, {papanas} papanasi.")

print(f"Mai sunt {len(tavi)} tavi.")

print(f"Mai este ceafa: {(meniu.count('ceafa') - cefe) <= 0}")
print(f"Mai sunt papanasi: {(meniu.count('papanasi') - papanas) <= 0}")
print(f"Mai sunt guias: {(meniu.count('guias') - guiasu) <= 0}")

total_bani=0
for i in range(len(istoric_comenzi)):
    istoric_comanda2 = istoric_comenzi[i]
    studentule=istoric_comanda2[0]
    comandanecesara=istoric_comanda2[1]
    if comandanecesara=="ceafa":
        total_bani += 10
    if comandanecesara=="papanasi":
        total_bani += 7
    if comandanecesara=="guias":
        total_bani += 10

print(f"Cantina a încasat: {total_bani} lei")
produse_max_7_lei = [produs for produs in preturi if produs[1] <= 7]
print(f"Produse care costă cel mult 7 lei: {produse_max_7_lei}")