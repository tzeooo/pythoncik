# Sarcina 1
# Lista
lista = [100, 200, 300, 400, 500]
print(f"Prima valoare: {lista[0]}")
print(f"A treia valoare: {lista[2]}")
lista[2] = 350  # Modificăm a treia valoare
print(f"Lista modificată: {lista}")

sublista = lista[:3]  # Extragem primele trei elemente
print(f"Sublista extrasă: {sublista}")

lista.insert(1, 150)  # Metoda insert adaugă un element
print(f"Lista după insert: {lista}")

print(f"Numărul maxim din listă: {max(lista)}")  # Funcția max()
print(f"Numărul minim din listă: {min(lista)}")  # Funcția min()

print(f"200 este în listă? {200 in lista}")  # Operator in
print(f"Multiplicarea listei: {lista * 2}")  # Operator *

# Tuplu
tuplu = (3, 6, 9, 12, 15)
print(f"Tipul de date: {type(tuplu)}")
print(f"Prima valoare: {tuplu[0]}")
print(f"Ultima valoare: {tuplu[-1]}")

subtuplu = tuplu[2:]  # Extragem de la indexul 2 până la final
print(f"Subtuplu extras: {subtuplu}")

print(f"Lungimea tuplului: {len(tuplu)}")  # Funcția len()
print(f"Suma elementelor tuplului: {sum(tuplu)}")  # Funcția sum()
print(f"Tuplul sortat: {sorted(tuplu)}")  # Funcția sorted()

# Set
multime = {10, 20, 20, 30, 40, 40, 50}
print(f"Mulțimea: {multime}")
multime.remove(10)  # Metoda remove elimină un element
print(f"Mulțimea după eliminare: {multime}")
print(f"Lungimea mulțimii: {len(multime)}")  # Funcția len()

# Dicționar
dict_text = {"prenume": "Ion", "oras": "Cluj"}
dict_num = {1: "Ianuarie", 2: "Februarie", 3: "Martie"}
print(f"Element din dict_text: {dict_text['prenume']}")
print(f"Element din dict_num: {dict_num[1]}")

dict_text["varsta"] = 30  # Adăugăm o nouă pereche cheie-valoare
print(f"Dicționar actualizat: {dict_text}")

dict_num.clear()  # Golim dicționarul
print(f"Dicționar numeric după clear: {dict_num}")

print(f"Toate cheile: {dict_text.keys()}")  # Funcția keys()
print(f"Toate valorile: {dict_text.values()}")  # Funcția values()

# Conversie între tipuri de date
dict_to_lista = list(dict_text.items())
print(f"Dicționar convertit în listă de perechi: {dict_to_lista}")
lista_to_set = set(lista)
print(f"Lista convertită în set: {lista_to_set}")

# Sarcina 2
produse = ["Lapte", "Pâine", "Ouă"]
preturi = [12, 5, 8]

for i in range(3):
    print("Produsul {} costă {} lei".format(produse[i], preturi[i]))

varsta = int(input("Introduceți vârsta: "))
print(f"În 10 ani veți avea {varsta + 10} ani.")

cuvinte = {"apple", "banana", "cherry"}
print(f"'apple' este în set? {'apple' in cuvinte}")
print(f"'mango' nu este în set? {'mango' not in cuvinte}")
