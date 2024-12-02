#Part 12 // Logische Operratoren

#Logisches ODER => Wenn von meheren Ausdrücken einer TRUE zurückgibt ist der gesamtausdruck TRUE
#Logisches UND => Wenn mehere Audrücke (Abfragen) vorhanden sind müssen ALLE TRUE zurückgeben damit der Gesammtausdruck
                  # true ist
#Logisches NICHT Negiert den

number_one = int(input("Bitte gebe die erste Zahl zwischen 0 und 50 ein: "))
number_two = int(input("Bitte gebe die zweite Zahl zwischen 0 und 50 ein: "))
number_three = int(input("Bitte gebe dritte Zahl zwischen 0 und 50 ein: "))

win = "Du hast die Lotterie Gewonnen! Herzlichen Glückwunsch"
lose = "Tut mir leid du hast verloren. Versuche es doch noch einmal"

winning_number_one = 15
winning_number_two = 1
winning_number_three = 45

if number_one == winning_number_one and number_two == winning_number_two and number_three == winning_number_three:
    print(win)
#Durch das and müssen alle drei Bedingungen true sein damit der Block der if-Abfrage ausgeführt wird. Der Code wird von
#links nach rechts überprüft
else:
    print(lose)

if 5 == 3 or 5 == 5:
    print("Eine der beiden Abfragen stimmt")
else:
    print("keine der beiden Abfragen stimmt")


if 5 < 10 or not 10 == 10: #Das NOT dreht das boolische Ergebnis um 10 == 10 ergibt TRUE durch das NOT ergibt dies FALSE
    print("true")   #durch OR muss nur eines von beiden stimmen also ist die Bedingung erfükkt
else:
    print("false")

if 5 < 10 and not 10 == 10: # hier ist die Selbe abfrage aber es müssen beide Abfragen TRUE zurück geben, durch den NOT
    print("true")   #Operrator gibt die 2. Abfrage FALSE zurück wodurch der IF-Block nicht ausgeführt wird
else:
    print("false")
