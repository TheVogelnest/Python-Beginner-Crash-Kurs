#Part 6 // Input() Funktion

#Dies ist quasi der gegenspieler zur print() funktion, welche Daten ausgeben kann
#Die Input() Funktion hingegegn nimmt eingaben vom User entgegen

print("Anfang des Programmes")

name = input() #Die input Funktion sorgt dafür das das Programm pausiert und erwartet eine eingabe und speichert diese
#in diesem beispiel in die Variable "name" // Standardmäßig als string
print("Mein Name ist " + name +"!")
age = input("Bitte dein Alter eingeben:") #Man kann der Input Methode einen String übergeben um den User einen Hinweis für den Input zu geben
print('Mein alter ist ' + age)
print("Ende des Programmes")
