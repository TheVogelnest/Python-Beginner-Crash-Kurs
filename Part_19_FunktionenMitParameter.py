#Part 19 // Funktionen mit Übergabe Paramter


print("Das ist ein übergabe Paramter") #der String zwischen den Klammern ist das übergabe Paramter


def say_hello(name): #Variable in der Methode können im Methoden Körper verwendet werden und müssen beim Aufruf
    print(f"Hallo {name}")  #der Methode mit übergeben werden, da in Python nicht direkt steht welcher Typ es ist
    print("Wilkommen zurück") #sollte man die Variable ordentlich benennen das man erkennt was gewollt ist


your_name = input("Nenne mir deinen Namen: ")
say_hello(your_name) #Eingabe des User wird der Methode als String übergeben und dann wird die Methode mit
#der Übergabe ausgeführt
