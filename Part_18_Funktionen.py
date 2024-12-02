#Part 18 // Funktionen

#dienen zur Struktur des Codes
#ist quasi ein Unterprogramm des Gesamt Programmes
#können mehrfach aufgerufen werden um redundanten Code zu vermeiden

def first_function(): #Schlüsselwort "def" + Bezeichner der Funktion mit ()
    print("Das ist die erste Funktion")
    print("Ende des Codes")


first_function() #Aufruf der Funktion, erst dann wird diese ausgeführt
first_function()
first_function() #diese kann beliebig oft aufgerufen werden
