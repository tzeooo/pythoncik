# 1
name = input("Bună! Te rog să introduci numele tău: ")
print(f"Salut, {name}!")
# 2
numar_intreg = 21
numar_real = 3.14
text_scurt = "Aboba"
text_lung = """Pisicuta pis-pis-pis
te-am visat aseara in vis
te spalam, te pieptanam"""
# 3
print(f"Tipul de date al variabilei 'numar_intreg' este: {type(numar_intreg)}")
print(f"Tipul de date al variabilei 'text_scurt' este: {type(text_scurt)}")
# 4
print(f"Lungimea textului scurt este: {len(text_scurt)}")
# 5
text_mare = text_scurt.upper()
print(f"Textul in litere mari: {text_mare}")
# 6. intepreteaza doar textul din 8 pan la 15 caractere
subtext = text_lung[9:21]
print(f"Subsirul taiat este:{subtext}")
# 7. introducem variabilele, in string.format la sfarsit, si independenta de (0,1,2) le pune,
#f-string le introducem deodata unde ne este nevoie (cum faceam deobicei)
# string.format()
print("Mesaj folosind format: {0} are varsta de {1} ani.".format(name, numar_intreg))
# f-string
varsta = 22
print(f"Mesaj folosind f-string: {name} va avea in martie varsta de {varsta} ani.")

#subiectul 2

#txt = "More results from text..."
#substr = txt[4:12]
#print(substr)
#print(substr.strip())

# va da - results, caci substr= results, substr.strip scoate spatiile, el nu le are asa ca iese doar results curat


#txt = "More results from text..."
#print(txt.split())

#splitueste, imparte cuvintele aparte, adica va fi o lista ['More', 'results', 'from', 'text']

#age = 36
#txt = "My name is Mary, and I am {}"
#print(txt.format(age))

# va da My name is Mary, and i am 36, caci inloc de {} se pune variabila age, din vina la txt.format
