#Part 22 // Self Parameter
import Part_22_KlassenObjekte as Part22
#importiert die Python Datei und weißt ihr den Bezeichner "Part22" zu

new_car = Part22.Car()

class Tree:
    def __init__(self): #der self Operrator hilft Python dabei zuzuordnen auf welches
        self.height = None #Objekt im Speicher wir uns gerade beziehen, es setzt also
        self.width = None#eine Referrenz
        self.age = None

#wenn ich ein neues Objekt der Klasse Tree erstelle und mir dieses mit der print Funktion ausgeben
#lasse bekomme ich folgendes ausgegeben:

first_tree = Tree()
first_tree.age = 200
first_tree.height = 8.75
first_tree.width = 1.25
print(first_tree)
# <__main__.Tree object at 0x0000019E47C91FD0> dies ist die Position im Speicher von genau diesem objekt
# Diese Zahl "0x0000019E47C91FD0" ist die Referrenz Adresse zu unserem Objekt und wird beim Aufrufen der __init__
#Methode der Klasse als self Parameter übergeben. Und so weiß Python welches Objekt gerade angesprochen wird
# also wenn ich z.B.
first_tree.age = 210 # schreibe wird im code folgendes ausgeführt
#Tree.__init__(0x0000019E47C91FD0).age = 210
#Die Referrenz Nummer ändert sich bei jedem neuen Starten des Programmes
