#Part 7 // Type Casting Funktionen

value_one = input("Erste Zahl eingeben: ")
value_two = input("Zweite Zahl eingeben: ")

print(value_one + value_two)
# So werden die Zahlen verkettet und nicht addiert da die input() - Funktion standardmäßig Strings entgegen nimmt

type_of_value = type(value_one) #ermittelt den Datentypen und speichert diesen in einer Variable

print("Der Datentyp ist: ")
print(type_of_value)

#Type Casting
str(value_one) #Konvertiert die Variable in einen string um // wenn möglich
float(value_one) #Konvertiert die Variable in einen float um // wenn möglich
int(value_one) #Konvertiert die Variable in einen int um // wenn möglich

type_of_value = type(int(value_one)) #nur in dieser Zeile ein Int beim erneuten Aufrufen wäre es wieder ein String

print("Der neue Datentyp ist: ")
print(type_of_value)

value_one = int(value_one) #eine Möglichkeint den Wert dauerhaft zu Konvertieren
value_two = int(value_two) #Alternativ kann man float() nutzen um auch Gleitkommazahlen verarbeiten zu können
print(f"Das Ergebnis ist: {value_one + value_two}")
