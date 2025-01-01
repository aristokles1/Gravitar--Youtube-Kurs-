import locale

locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

summe = 0

for feld in range(64):
    reiskoerner = 2**feld
    summe += reiskoerner
    print(f'Auf dem {feld+1}. Feld liegen {locale.format_string("%d", reiskoerner, grouping=True):>30} Reiskörner')

print()    
print(f'Insgesamt sind es {locale.format_string("%d", summe, grouping=True)} Reiskörner')
print()

gesamt_gewicht = round(summe * 0.00002 / 1000) # in Tonnen
print(f'Die Reiskörner wiegen zusammen {locale.format_string("%.0f", gesamt_gewicht, grouping=True)} Tonnen')
print()
