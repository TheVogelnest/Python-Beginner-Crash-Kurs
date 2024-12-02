#Part 11 // ELIF ud ELSE Zweige der IF-Abfrage

age = int(input("Bitte geben dein Alter ein: "))

if age < 18:
    print("Der Nutzer ist unter 18 Jahre alt!")
elif age == 18: #Wenn die IF-Abfrage False ist wird geschaut ob eine der ELIF Abfragen zutrifft (von oben nach unten)
    print("Der Nutzer ist gerade Volljährig")
else:   #Wenn die IF und jede ELIF Abfragen nicht zutrifft wird ELSE ausgeführt
    print("Der Nutzer ist Volljährig")


print("Programmende")
