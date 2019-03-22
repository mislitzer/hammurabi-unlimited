class City:

    population =  0
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
        :return:
        """

    def calculatePopulation(self, value):
        """
            Wird aufgerufen, wenn die Population verändert wird
        :return:
        """

    def calculateStore(self, value):
        """
            Wird aufgerufen, wenn die Scheffelmenge verändert wird
        :return:
        """

    def disease(self):
        """
            Wird aufgerufen in der process() und berechnet Wahrscheinlichkeit einer
            Plage oder Seuche
        :return:
        """

    def rats(self):
        """
            Wird in der process() aufgerufen und berechnet die Menge an Scheffeln,
            welche die Ratten pro Jahr fressen
        :return:
        """

    def immigration(self):
        """
            Wird aufgerufen in der process() und berechnet den Bevölkerungszuwachs
        :return:
        """