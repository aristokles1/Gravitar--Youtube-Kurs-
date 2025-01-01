# Importiere notwendige Bibliotheken
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Öffne und lese die Textdatei
with open('05_Alice_in_wonderland.txt', 'r') as f:
    text = f.read()

# Erstelle ein WordCloud-Objekt mit angegebener Breite und Höhe
wordcloud = WordCloud(width=1920, height=1080)

# Füge benutzerdefinierte Stopwörter zum STOPWORDS-Set hinzu
STOPWORDS.add('said')
STOPWORDS.add('illustration')

# Generiere die Wortwolke aus dem Text
wordcloud.generate(text)

# Zeige die generierte Wortwolke mit matplotlib an
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Achsen ausblenden

# Zeige das Plot an
plt.show()

'''
Detaillierte Erläuterung:
1. Die Bibliotheken `wordcloud` und `matplotlib.pyplot` werden importiert,
   um die Wortwolke zu erstellen und anzuzeigen.
2. Die Textdatei '05_Alice_in_wonderland.txt' wird geöffnet und ihr Inhalt
   wird in die Variable `text` gelesen.
3. Ein `WordCloud`-Objekt wird mit einer Breite von 1920 und einer Höhe von
   1080 Pixeln erstellt.
4. Zwei benutzerdefinierte Stopwörter ('said' und 'illustration') werden zum
   `STOPWORDS`-Set hinzugefügt, um diese Wörter aus der Wortwolke
   auszuschließen.
5. Die Methode `generate` des `WordCloud`-Objekts wird aufgerufen, um die
   Wortwolke basierend auf dem Text zu generieren.
6. Die generierte Wortwolke wird mit `imshow` von `matplotlib` angezeigt,
   wobei die Achsen mit `axis('off')` ausgeblendet werden.
7. Schließlich wird das Plot mit `show` angezeigt.
'''