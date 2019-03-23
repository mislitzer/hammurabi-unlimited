from random import random

class City:

    def __init__(self):
        self.__population = 0
        self.__acres = 0
        self.__trade_value = 0
        self.__bushels_per_acre = 0
        self.__store = 0
        self.__year = 0

        # start initial round
        self.process()

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

    def process(self):
        """
            Wird aufgerufen wenn die Eingabe bestätigt wird
        """
        self.ask_to_buy_or_sell_land()

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



    def rats(self):
        """
            Wird in der process() aufgerufen und berechnet die Menge an Scheffeln,
            welche die Ratten pro Jahr fressen
        """

    def immigration(self):
        """
            Wird aufgerufen in der process() und berechnet den Bevölkerungszuwachs
        :return:
        """

    def ask_to_buy_or_sell_land(self):
        print("asdfsdf")
        """ Ask user how many bushels to spend buying land. """
        value = input("> How many acres will you buy or sell? ")
        return value

