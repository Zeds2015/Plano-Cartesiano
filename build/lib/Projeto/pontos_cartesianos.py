from projeto import PontosEm2D

ponto_a = PontosEm2D(2,2)
print(ponto_a)
ponto_b = PontosEm2D(2,0)
print(ponto_b)

ponto_c = ponto_a + ponto_b
ponto_d = ponto_a - ponto_b
ponto_e = ponto_a * ponto_b
ponto_f = ponto_b / ponto_a
ponto_g = ponto_a // ponto_a
disso_eu_sei = ponto_a == (2,2)
sera = ponto_a == ponto_b

print(ponto_c)
print(ponto_d)
print(ponto_e)
print(ponto_f)
print(ponto_g)
print(disso_eu_sei)
print(sera)