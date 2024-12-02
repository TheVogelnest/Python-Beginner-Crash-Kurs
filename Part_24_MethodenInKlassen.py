class People:
    def __init__(self):
        self.age = None
        self.firstname = None
        self.lastname = None
        self.heigt = None
        self.weight = None
        self.x_position = 5
        self.y_position = 5 # jedes Objekt der Klasse People startet an der x,y koordinate 5

    def walk(self, x, y):     #da dies eine Funktion in einer Klasse ist, also eine Methode wird der sef Parameter übergeben
        self.x_position += x    #dadurch weiß Python genau welches Objekt der Klasse People diese Methode aufruft
        self.y_position += y

first_person = People()
print(f"x={first_person.x_position} // y={first_person.y_position}")

first_person.walk(5, 10)
print(f"x={first_person.x_position} // y={first_person.y_position}")
