# Lucrarea de laborator nr. 3 – Programarea jocurilor în Python
# Tema: Funcții lambda, funcții clasice, sortări și aplicații

# --------------------------------------------
# 1. Funcție lambda simplă pentru salutare
greet_user = lambda name: print('Hello My Dear,', name)
user_name = input("What is your name? ")
greet_user(user_name)

print("-" * 50)

# --------------------------------------------
# 2. Sortarea unei liste de tupluri după al doilea element
lista_tupluri = [(3, 11), (1, 7), (7, 8), (16, 88), (23, 15), (5, 2), (9, 10)]

lista_sortata = sorted(lista_tupluri, key=lambda x: x[1])

print("Lista sortată după al doilea element din fiecare tuplu:")
print(lista_sortata)

print("-" * 50)

# --------------------------------------------
# 3. Propria funcție lambda – pătratul unui număr
square = lambda x: x * x
numar = int(input("Introduceți un număr pentru a-i calcula pătratul: "))
print("Pătratul numărului este:", square(numar))

print("-" * 50)

# --------------------------------------------
# 4. Funcții clasice în diferite forme

# a) Funcție fără parametri
def mesaj_bun_venit():
    print("Bine ai venit în jocul nostru!")

# b) Funcție cu parametri
def saluta_jucator(nume):
    print(f"Salut, {nume}!")

# c) Funcție cu parametri cu valori implicite
def scor_final(punctaj=0):
    print(f"Scorul final este: {punctaj}")

# d) Funcție care returnează un rezultat
def dubleaza(x):
    return x * 2

# e) Funcție care nu folosește return
def afiseaza_dublu(x):
    print("Dublul valorii este:", x * 2)

# Apelarea funcțiilor
mesaj_bun_venit()
saluta_jucator("Alex")
scor_final()            # folosim valoarea implicită
scor_final(250)         # valoare specificată

print("Valoarea dublată este:", dubleaza(5))
afiseaza_dublu(5)

print("-" * 50)
print("Toate cerințele laboratorului au fost rezolvate.")
