#Part 20 // Funktionen mit Rückgabewert

#jede Funktion hat einen Rückgabewert auch eine die nicht direkt etwas zurückgibt
#im Beispiel der say_hello() Funktion ist es "None" also nichts, es ist die abwesenheit eines Wertes
def say_hello(name):
    print(f"Hallo {name}")
    print("Wilkommen zurück")

print(say_hello("Simon")) #fürt die Funktion aus und gibt dann den Rückgabewert der Funktion in der Konsole aus
#None ist vom Typ NoneType
print(type(None))
if say_hello("Name") == None: #Beweis das es None ist
    print("Es ist None")

#Beispiele
def get_maximum(a, b):
    if a > b:
        return a
    else:
        return b

number_one = int(input("Gebe die erste Zahl ein: "))
number_two = int(input("Gebe die zweite Zahl ein: "))

result = get_maximum(number_one, number_two)
print(f"Die größere Zahl ist {result}") #beide Varianten führen zum selben Ergebnis
print(f"Die größere Zahl ist {get_maximum(number_one, number_two)}")
