#Part 17 // Die For Schleife als Zähler Schleife

variable_one = "Ich bin einfach Text"

for number in range(10): #Die For Schleife erzeugt für uns so ein Itterierbares Objekt im Bereich 0-10
    print(number)        #also die Zahlen 0,1,2,3,4,5,6,7,8,9

start = 5
end = 10

for number in range(start, end): #Jetzt wird auch ein Itterierbares Objekt erzeugt mit dem Startwert 5 und dem Endwert
    print(number)                #10 //Startwert = inkludiert // Endwert = exkludiert also werden die Zahlen bis 9
                                 #ausgegeben


for number in range(start, end, 2): #die 2 gibt die schrittweite an also z.b. von 5 auf 7 dann auf 9 und dann wäre die
    print(number)                   #schleife beendet

#kann man z.B. auch für schleifen Benutzen
list_names = ['Fritz', 'Inessa', 'Susi', 'Simon']

for count in range(0, 5, 1):
    print(list_names[count])
    #start mit 0 endet mit 4 und gibt jedes mal den entsprechenden Listen Index in der Konsole aus

