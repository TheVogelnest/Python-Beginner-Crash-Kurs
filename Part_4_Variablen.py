#Part 4 Das Konzept von Variablen // Werte zu speichern

#um diese Später im Programm wieder aufzurufen
#Dies sind quasi Datenspeicher in denen man Daten speichern kann, Variablen müssen wichtige Informationen enthalten wie
#den Bezeichner => Variablen Name und dieser sollte immer sprechend gewählt werden, das man erahnen kann welche Daten
#sich in den Variable befindet
# variable1 // variable2 = nicht gut
# age (für das alter) // weight (für das Gewicht) = gut // sprechend und englisch (optimaler weise in Englisch)

age = 33 #Der wert rechts wird dem linken Bezeichner zugewiesen
#Python erkennt automatisch welche art von Daten in einer Variable gespeichert wird, deswegen muss nicht Manuel deklariert
#werden um welche Art von Variable es sich handelt ( in diesem bsp. ist es ein Int)
print(age) #ansprechen einer Variable im Programm Code

age = 44 #bestehende Variable "age" wurde hier überschrieben und enthält nun den Wert 44
print(age)
name = "Simon"
print("Mein Name ist " + name) #String Addition mit Variablen
print(f"Mein name ist {name}") #Variablen direkt in einen string einbetten durch das f vor den Hochkommatas

#Bei der wahl des Bezeichner ist zu beachten das die Variable mit einem Buchstaben oder einem Unterstrich (_) beginnt
#Der rest darf aus Buchstaben, Zahlen und dem Unterstrich bestehen. Es dürfen keine Sonderzeichen wie z.B. $, !, (, usw.
#für den Bezeichner verwendet werden
