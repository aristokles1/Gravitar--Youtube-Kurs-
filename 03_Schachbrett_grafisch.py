import matplotlib.pyplot as plt
import locale

# Setze die Locale auf Deutsch (Deutschland), um Punkt als Tausender-Trennzeichen zu verwenden
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

# Initialisiere die Summe der Reiskörner
summe = 0

# Liste zur Speicherung der Anzahl der Reiskörner auf jedem Feld
koerner_auf_feld_liste = []

# Berechne die Anzahl der Reiskörner auf jedem Feld des Schachbretts
for feld in range(64):
    reiskoerner = 2**feld
    koerner_auf_feld_liste.append(reiskoerner)
    summe += reiskoerner
    print(f'Auf dem {feld+1}. Feld liegen {locale.format_string("%d", reiskoerner, grouping=True):>30} Reiskörner')

print()    
print(f'Insgesamt sind es {locale.format_string("%d", summe, grouping=True)} Reiskörner')
print()

# Berechne das Gesamtgewicht der Reiskörner in Tonnen (angenommenes Gewicht pro Korn: 0.00002 kg)
gesamt_gewicht = round(summe * 0.00002 / 1000) # in Tonnen
print(f'Die Reiskörner wiegen zusammen {locale.format_string("%.0f", gesamt_gewicht, grouping=True)} Tonnen')
print()

# Erstelle ein Diagramm der Anzahl der Reiskörner auf jedem Feld
plt.plot(koerner_auf_feld_liste)
plt.xlabel('Feldnummer')
plt.ylabel('Anzahl der Reiskörner')
plt.title('Anzahl der Reiskörner auf jedem Feld des Schachbretts')
plt.show()


# Dokumentation:
# 1. Importe:
#    - matplotlib.pyplot: Zum Erstellen von Diagrammen.
#    - locale: Zum Setzen der Lokalisierung für die Formatierung von Zahlen.
#
# 2. Locale-Einstellung:
#    - Setzt die Locale auf Deutsch (Deutschland), um Punkt als Tausender-Trennzeichen zu verwenden.
#
# 3. Initialisierung:
#    - summe: Variable zur Speicherung der Gesamtsumme der Reiskörner.
#    - koerner_auf_feld_liste: Liste zur Speicherung der Anzahl der Reiskörner auf jedem Feld des Schachbretts.
#
# 4. Berechnung der Reiskörner:
#    - Schleife über 64 Felder des Schachbretts.
#    - Berechnung der Anzahl der Reiskörner auf jedem Feld (2^feld).
#    - Hinzufügen der Anzahl der Reiskörner zur Liste und zur Gesamtsumme.
#    - Ausgabe der Anzahl der Reiskörner auf jedem Feld mit Tausender-Trennzeichen.
#
# 5. Gesamtsumme und Gewicht:
#    - Ausgabe der Gesamtsumme der Reiskörner mit Tausender-Trennzeichen.
#    - Berechnung des Gesamtgewichts der Reiskörner in Tonnen (angenommenes Gewicht pro Korn: 0.00002 kg).
#    - Ausgabe des Gesamtgewichts der Reiskörner in Tonnen mit Tausender-Trennzeichen.
#
# 6. Diagramm:
#    - Erstellung eines Diagramms der Anzahl der Reiskörner auf jedem Feld.
#    - Beschriftung der Achsen und des Titels.
#    - Anzeige des Diagramms.
