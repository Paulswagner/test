import matplotlib.pyplot as plt

class Kreis():

    def __init__(self, radius, farbe):
        if (isinstance(radius, float) or isinstance(radius, int)) and radius > 0: 
            self.radius = radius
        else:
            raise ValueError("Bitte gib eine positive Zahl für den Radius ein.")
        self.farbe = farbe
        print(f'Du hast ein objekt der Klasse Kreis erzeugt mit Radius: {self.radius} und farbe {self.farbe}')


    def plot(self):
        self.fig, self.ax = plt.subplots()
        kreis = plt.Circle((0, 0), self.radius, color = self.farbe)   # kreis ist halt ein patch und kein linienobjekt. das wird einer axe hinzugefügt
        self.ax.add_patch(kreis)
        self.ax.set_xlim(-3, 3)
        self.ax.set_ylim(-3, 3)
        self.ax.set_aspect(1) # Verhältnis x zu y achse
        plt.show()   # das hier plt.show() showed es und löscht den speichert wieder. globale funktion die allee matplotlib figuren anzeigt
                            #fig → Figure-Objekt (matplotlib.figure.Figure)
                            #ax → Achsen-Objekt (matplotlib.axes._subplots.AxesSubplot)

    def plot_save(self):
        self.fig.savefig(f'kreis_r_{self.radius}_farbe_{self.farbe}.pdf')  # hier macht es ja keinen sinn das nochmal zu plotten. wäre schon sinnvoll, dass einfch oben iregdnwie zu specciehrn und hier nur aufzurufen? mit self.kreis?
                # und dieser aufruf speichert das aktuelle figure objekt. # das der befehl von matplotlib.figure um es zu speichern
        print('Ich habe die figure gespeichert!')



k1 = Kreis(2.2, 'green')
k1.plot()
k1.plot_save()

# Titel hinzufügen noch. sollte halt auch nur iene zeile sien oder doch funktion machen um den benuzer tippen zu lassen?
# noch herausfinden wie fig, ax zusammenhängen also warum immer zwei sachen ausgegeben werden bei plt.subplots()
# ich habe es verbunden man sieht es aber nicht bei git?


