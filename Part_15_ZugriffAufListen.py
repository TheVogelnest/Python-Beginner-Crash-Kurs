#Part 15 // Listen und deren Zugriff auf dessen Inhaltes

list_numbers = [3, 4, 34, 5, 345, 6, 3456] #Max Index = 6 (7 Elemente)
list_names = ['Fritz', 'Inessa', 'Susi', 'Simon']
list_random = ['ABC', 33, 'DEF', 1.23, 44]

print(list_random) #gibt die GESAMTE Liste in der Konsole aus // Ausgabe: ['ABC', 33, 'DEF', 1.23, 44]
print(list_random[0]) #gibt den Spezifischen Index einer Liste aus // Index fängt immer bei 0 an zu zählen // Ausgabe: ABC

#print(list_random[7]) würde zu einem fehler "list index out of range" führen

print(list_numbers[-1]) #Hier wird ein negativer Index verwendet mit dem man z.B. wie hier das letzte Element der List
#sich in der Konsole ausgeben lässt
print(list_numbers[-1]) #oder das 2. letzte usw. // Kann zum selben error führen wie in Zeile 10 beschrieben

print(list_names)
#erste Element der list_names = Fritz
list_names[0] = 'Xavier' #Der erste eintrag der Liste wurde überschrieben bzw. verändert
print(list_names)
