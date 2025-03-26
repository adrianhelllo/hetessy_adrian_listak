fo_kerdesek = ["Mennyi -5 - (-3)?", "Mennyi 8 + 3 * 2?", "Mennyi 15 / 3 + 4?", "Mennyi 12 - 5 * 2?", "Mennyi 6 * (5 - 3)?"]
valaszok = ["c", "b", "c", "b", "c"]

kerdes1 = ["Nem tudom", "2", "-2", "8"]
kerdes2 = ["22", "14", "16", "24"]
kerdes3 = ["9", "5", "7", "6"]
kerdes4 = ["4", "2", "10", "6"]
kerdes5 = ["6", "12", "8", "10"]

kerdesek = [kerdes1, kerdes2, kerdes3, kerdes4, kerdes5]

helyes_kerdesek = 0
feltett_kerdesek = 0

for i in range(len(kerdesek)):
    print(f"{i + 1}. kérdés: {fo_kerdesek[i]}")
    print(f"Lehetőségek:\n a) {kerdesek[i][0]},\n b) {kerdesek[i][1]},\n c) {kerdesek[i][2]},\n d) {kerdesek[i][3]}, ")
    valasz = input("Add meg a válaszod betűjelét (a, b, c, d): ")

    if valasz == valaszok[i]:
        helyes_kerdesek += 1

    feltett_kerdesek += 1

print(f"A {feltett_kerdesek} kérdésből {helyes_kerdesek} lett jó így a helyes válaszok aránya {helyes_kerdesek}/{feltett_kerdesek}, avagy {int(helyes_kerdesek/feltett_kerdesek*100)} százalék.")