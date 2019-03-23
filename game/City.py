from random import random
class City:

    population = 0
    acres = 0
    tradeValue = 0
    bushelsPerAcre = 0
    store = 0
    year = 0

    def __init__(self) -> None:
        super().__init__()

    def process(self):
        """
            Wird aufgerufen wenn die Eingabe bestätigt wird
        """

    def calculatePopulation(self, value):
        """
            Wird aufgerufen, wenn die Population verändert wird
        """
        self.population += value

    def calculateStore(self, value):
        """
            Wird aufgerufen, wenn die Scheffelmenge verändert wird
        """
        self.store += value

    def disease(self):
        """
            Wird aufgerufen in der process() und berechnet Wahrscheinlichkeit einer
            Plage oder Seuche
        """
        disease = random.randint(1, 10)
        if(disease == 10):
            deaths = random.randint(-1,-(self.population/2))
            self.calculatePopulation(deaths)



    def rats(self):
        """
            Wird in der process() aufgerufen und berechnet die Menge an Scheffeln,
            welche die Ratten pro Jahr fressen
        """

    def immigration(self):
        """
            Wird aufgerufen in der process() und berechnet den Bevölkerungszuwachs
        """