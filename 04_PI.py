"""
PI-Visualisierung mit Turtle-Grafiken

Dieses Skript visualisiert die Ziffern von Pi mithilfe von Turtle-Grafiken. Jede Ziffer von Pi wird verwendet, um den Drehwinkel der Turtle zu bestimmen, wodurch ein einzigartiges Muster entsteht.

Module:
    turtle: Bietet Funktionen für Turtle-Grafiken.

Verwendung:
    Führen Sie das Skript aus, um eine Visualisierung der ersten 500.000 Ziffern von Pi zu erstellen.

Attribute:
    lines (int): Die Anzahl der zu visualisierenden Ziffern von Pi.
    zoom_factor (float): Der Faktor, um den die Visualisierung gezoomt wird. Werte kleiner als 1 verkleinern die Darstellung.

Funktionen:
    Keine
"""

import turtle as tu

# Anzahl der zu visualisierenden Ziffern von Pi (maximal 1 Million)
lines = 500000

# Lesen der Ziffern von Pi aus einer Datei
with open("04_1_million_digits_of_pi.txt", "r") as f:
    pi = f.read()

# Einrichtung der Turtle-Grafikumgebung
tu.mode("logo")
tu.tracer(False)
tu.screensize(7000, 7000, "black")
tu.colormode(255)

# Setzen der Weltkoordinaten für den Zoom-Modus
zoom_factor = 0.95  # Verkleinerungsfaktor (negativer Zoom)
tu.setworldcoordinates(-5000/zoom_factor, -5000/zoom_factor, 5000/zoom_factor, 5000/zoom_factor)

# Zeichnen der Visualisierung
for n in range(lines):
    color = int(n / (lines / 255))
    tu.pencolor(255, 255 - color, color)
    zahl = int(pi[n])
    rotation = zahl * 36
    tu.setheading(rotation)
    tu.forward(5)
    if n % 20_000 == 0:
        tu.update()

# Speichern der Zeichnung als PostScript-Datei 
# (Zum Anschauen wird ein entsprechendes Grafikprogramm benötigt)
tu.getcanvas().postscript(file="04_PI_picture.ps")
tu.done()


# Erklärung der Hauptabschnitte:

# Modul-Import:
# turtle: Wird verwendet, um Turtle-Grafiken zu erstellen.

# Konstanten:
# lines: Anzahl der zu visualisierenden Ziffern von Pi.
# zoom_factor: Faktor für den Zoom-Modus. Werte kleiner als 1 verkleinern die Darstellung.

# Datei einlesen:
# Liest die ersten 1 Million Ziffern von Pi aus einer Datei.

# Turtle-Grafik einrichten:
# tu.mode("logo"): Setzt den Modus der Turtle-Grafik.
# tu.tracer(False): Deaktiviert das automatische Zeichnen, um die Leistung zu verbessern.
# tu.screensize(10000, 10000, "black"): Setzt die Bildschirmgröße und den Hintergrund.
# tu.colormode(255): Setzt den Farbmodus auf RGB.

# Zoom-Modus einstellen:
# tu.setworldcoordinates(...): Setzt die Weltkoordinaten für den Zoom-Modus.

# Visualisierung zeichnen:
# Iteriert über die Ziffern von Pi und zeichnet die Visualisierung basierend auf den Ziffern.
# tu.pencolor(...): Setzt die Stiftfarbe basierend auf der aktuellen Position.
# tu.setheading(rotation): Setzt die Richtung basierend auf der aktuellen Ziffer.
# tu.forward(5): Bewegt die Turtle vorwärts.
# tu.update(): Aktualisiert die Zeichnung alle 20.000 Schritte.

# Zeichnung speichern:
# tu.getcanvas().postscript(file="PI_picture.ps"): Speichert die Zeichnung als PostScript-Datei.
# tu.done(): Beendet die Turtle-Grafik.