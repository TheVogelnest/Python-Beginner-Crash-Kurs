#Part 21 // Klassen und Objekte

class Car:  #Innerhalb einer Klasse muss die __init__ Methode ausgeführt werden und dort
    def __init__(self): #die Propertys der Klasse deklariert werden, durch None können
        self.car_color = None   #wir Propertys erstellen bei denen wir erstmal noch keinen
        self.car_brand = None   #Wert speichern möchten
        self.car_horse_power = None #Funktionen sind außerhalb von Klassen und Methoden innerhalb
#erkennt man am self innerhalb der ()

#Ein neues Objekt (Instantz) der Klasse "Car" erstellen
first_car = Car()
first_car.car_brand = 'Volkswagen' #Propertys festlegen
first_car.car_color = 'Blau'
first_car.car_horse_power = 150

print(first_car.car_brand)
print(first_car.car_color)
print(first_car.car_horse_power)
print(first_car)
