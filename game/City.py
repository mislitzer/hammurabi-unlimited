import random

class City:

    def __init__(self):
        self.__population = 100
        self.__acres = 1000
        self.__trade_value = 0
        self.__bushels_per_acre = 0
        self.__store = 2800
        self.__year = 1
        self.__output = []

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        self.__population = value

    @property
    def acres(self):
        return self.__acres

    @acres.setter
    def acres(self, value):
        self.__acres = value

    @property
    def trade_value(self):
        return self.__trade_value

    @trade_value.setter
    def trade_value(self, value):
        self.__trade_value = value

    @property
    def bushels_per_acre(self):
        return self.__bushels_per_acre

    @bushels_per_acre.setter
    def bushels_per_acre(self, value):
        self.__bushels_per_acre = value

    @property
    def store(self):
        return self.__store

    @store.setter
    def store(self, value):
        self.__store = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, value):
        self.__output = value

    def inkrementOutput(self, value):
        self.output.append(value)

    def start(self):
        # start initial round
        self.process()

    def printOutput(self):
        for i in self.output:
            print(i)

    def printValues(self):
        print("population: " + str(self.population))
        print("acres: " + str(self.acres))
        print("store: " + str(self.store))

    def process(self):
        """
            Wird aufgerufen wenn die Eingabe bestätigt wird
        """


        buyOrSell = self.ask_to_buy_or_sell_land()
        self.calculateAcres(int(buyOrSell))
        self.rats()
        self.disease()

        self.printOutput()

        self.printValues()


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

    def calculateAcres(self, value):
        """
            Berechnet die Anzahl der Acker
        """
        self.acres += value

    def tradeValue(self):
        """
            Ermittelt den zufälligen tradeValue
        """
        self.trade_value = random.randint(17, 26)

    def disease(self):
        """
            Wird aufgerufen in der process() und berechnet Wahrscheinlichkeit einer
            Plage oder Seuche
        """
        disease = random.randint(1, 10)
        deaths = 0
        if(disease == 10):
            deaths = random.randint(1,(self.population/2))
            self.calculatePopulation(-deaths)
            self.inkrementOutput(str(deaths) + " have died because of a horrible disease!")

        return deaths



    def rats(self):
        """
            Wird in der process() aufgerufen und berechnet die Menge an Scheffeln,
            welche die Ratten pro Jahr fressen
        """
        eaten = random.randint(0, 200)
        self.calculateStore(-eaten)
        self.inkrementOutput("Rats have eaten " + str(eaten) + " bushels")
        return eaten

    def immigration(self):
        """
            Wird aufgerufen in der process() und berechnet den Bevölkerungszuwachs
        """


    def ask_to_buy_or_sell_land(self):
        """ Ask user how many bushels to spend buying land. """
        value = input("> How many acres will you buy or sell? ")
        return value

