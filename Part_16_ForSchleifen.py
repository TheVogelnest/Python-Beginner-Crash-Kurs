#Part 16 // For Schleifen und dessen verwendung

#Eignet sich hauptsächlich für 2 Aufgaben
#1. das Durchlaufen Iterierbarer Objekte (z.B. Liste) //kommt in diesem Part dran
#2. als Zählerschleife // kommt in Part 17 dran

list_random = ['ABC', 33, 'DEF', 1.23, 44]

for objekt in list_random: #For Kopf: Schlüsselwort "for", Bezeichner "names", Schlüsselwort "in", Das zu durchlaufende
    #obejkt "list_random"
    print(objekt) #jetzt wird jedes Objekt in der liste mit der print funktion ausgegeben
    #der Schleifen Körper wird für jedes Element, Obejkt im itterierbaren Objekt ausgeführt

variable_one = "Ich bin einfach Text"
for objekt in variable_one:
    print(objekt) #hier wird für jeden Char im string "variable_one" einmal der Schleifen körper ausgeführt
