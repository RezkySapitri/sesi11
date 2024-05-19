def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

p = 5
l = 3
hasil1, hasil2= hitung_persegi_panjang(p,l)
print(f"luas {hasil1}, keliling {hasil2}")  