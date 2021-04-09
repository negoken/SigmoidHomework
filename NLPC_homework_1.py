#Task1

# Să se introducă x - numărul lunei a anului, (exemplu: ianuarie - 1, februarie - 2, decembrie - 12), 
#  în baza lui x, să se printeze numărul de zile în această lună.

# Exemplu:
# Input:  1
# Output: 31


#Solutie Task1
x=int(input("Introduceti numarul lunii din an:"))

# conditie de validare interval
if x <=0 or x >12:
    print("Va rog introduceti o valoare valida!!,eg.[1-12]")
else:
    lunile_anului = {'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
    a = lunile_anului.values()
    print(list(a)[x-1])

#.........................................................................................#
#Task2
# Completare a problemei precedente, pe langa x se introduce și anul (ordinea introducerii nu importă), 
# și la fel să se afle numărul de zile în această lună.

# Exemplu:

# Input: 
# 2020
# 2
# Output:
# 	29

# Solutie Task2:

an = int(input("Introduceti anul dorit:"))
luna = int(input("Introduceti luna aferenta anului de mai sus:"))

# definim paricularitatea unui an bisect
bisect = 0
if an % 400 == 0:
     bisect = 1
elif an % 100 == 0:
     bisect = 0
elif an % 4 == 0:
     bisect = 1

# definim o lista cu lunile care contin 31 de zile
lista = [1,3,5,7,8,10,12]
if luna in lista:
     print(31)

# definim particularitatea pentru luna februarie
elif luna == 2:
     print(28 + bisect)
else:

     print(30)





