cislo1 = float(input("Zadej první desetinné číslo: "))
cislo2 = float(input("Zadej druhé desetinné číslo: "))

soucet = cislo1 + cislo2
rozdil = cislo1 - cislo2
soucin = cislo1 * cislo2
podil = cislo1 / cislo2 if cislo2 != 0 else "Nedefinováno (dělení nulou)"

print(f"Součet: {soucet:.2f}")
print(f"Rozdíl: {rozdil:.2f}")
print(f"Součin: {soucin:.2f}")
print(f"Podíl: {podil}")
