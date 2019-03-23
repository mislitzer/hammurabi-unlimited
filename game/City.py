import random
from config import GameConstants as GAMECONST
class City:

    def __init__(self):
        self.__population = 100
        self.__acres = 1000
        self.__trade_value = GAMECONST.TRADEVALUE_RAND
        self.__bushels_per_acre = 1
        self.__store = 2800
        self.__year = 1
        self.__starve = 0
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
    def starve(self):
        return self.__starve

    @starve.setter
    def starve(self, value):
        self.__starve = value

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

    def resetOutput(self):
        self.output.clear()

    def printOutput(self):
        for i in self.output:
            print(i)

    def printValues(self):
        print("Year: " + str(self.year))
        print("population: " + str(self.population))
        print("acres: " + str(self.acres))
        print("store: " + str(self.store))
        print("bushels per acre:" + str(self.bushels_per_acre))
        print("tradeValue: " + str(self.trade_value))

    def start(self):
        # start initial round
        self.printValues()
        buyOrSell = self.ask_to_buy_or_sell_land()
        feed = self.ask_to_feed_people()
        plant = self.ask_to_plant_bushel()
        self.peopleFeed(feed)
        self.harvest(plant)
        self.calculateAcres(int(buyOrSell))
        self.rats()
        self.disease()
        self.year += 1

    def process(self):
        """
            Wird aufgerufen wenn die Eingabe bestätigt wird
        """
        self.tradeValue()
        self.printValues()
        self.printOutput()
        buyOrSell = self.ask_to_buy_or_sell_land()
        feed = self.ask_to_feed_people()
        plant = self.ask_to_plant_bushel()
        self.peopleFeed(feed)
        self.harvest(plant)
        self.calculateAcres(int(buyOrSell))
        self.resetOutput()
        self.rats()
        self.disease()
        self.year += 1


    def calculatePopulation(self, value):
        """
            Wird aufgerufen, wenn die Population verändert wird
        """
        self.population += value

    def calculateStore(self, value):
        """
            Wird aufgerufen, wenn die Scheffelmenge verändert wird
        """
        self.store += int(value)

    def calculateAcres(self, value):
        """
            Berechnet die Anzahl der Acker
        """
        self.acres += value

    def tradeValue(self):
        """
            Ermittelt den zufälligen tradeValue
        """
        self.__trade_value = GAMECONST.TRADEVALUE_RAND

    def disease(self):
        """
            Wird aufgerufen in der process() und berechnet Wahrscheinlichkeit einer
            Plage oder Seuche
        """
        disease = GAMECONST.DISEASE_RAND
        deaths = 0
        if(disease >= 10):
            deaths= random.randint(1, int(self.population/2))
            self.calculatePopulation(-deaths)
            self.inkrementOutput(str(deaths) + " have died because of a horrible disease!")

        return deaths

    def rats(self):
        """
            Wird in der process() aufgerufen und berechnet die Menge an Scheffeln,
            welche die Ratten pro Jahr fressen
        """
        eaten = GAMECONST.RATS_RAND
        self.calculateStore(-eaten)
        self.inkrementOutput("Rats have eaten " + str(eaten) + " bushels")
        return eaten

    def immigration(self):
        """
            Wird aufgerufen in der process() und berechnet den Bevölkerungszuwachs
        """
        if(self.__starve == 0):
            immigration = random.randint(1, ((self.population)/5))
            print(immigration)
            self.calculatePopulation(immigration)

    def harvest(self, plant):
        self.calculateStore(plant*self.bushels_per_acre)

    def peopleFeed(self, bushel):
        foodPerPerson = int(bushel)/int(self.population)
        if(foodPerPerson < 20):
            if(int(foodPerPerson) == 19):
                self.starve = random.randint(1, int(self.population)/5)
                self.inkrementOutput("People starved: " + str(self.starve))
                self.calculatePopulation(-int(self.starve))
            elif(int(foodPerPerson) ==18):
                self.starve = random.randint(1, (int(self.population)/10)*3)
                self.inkrementOutput("People starved: " + str(self.starve))
                self.calculatePopulation(-int(self.starve))
            elif(int(foodPerPerson) ==17):
                self.starve = random.randint(1, (int(self.population) / 10)*6)
                self.inkrementOutput("People starved: " + str(self.starve))
                self.calculatePopulation(-int(self.starve))

            elif(int(foodPerPerson) <=16):
                self.starve = self.population
                self.inkrementOutput("People starved: " + str(self.starve))
                self.calculatePopulation(-int(self.starve))

        elif(foodPerPerson > 20):
            return


    def ask_to_buy_or_sell_land(self):
        """ Ask user how many bushels to spend buying land. """
        value = input("> How many acres will you buy or sell? ")
        storeChange = int(value)*int(self.trade_value)
        self.calculateStore(-int(storeChange))
        return value

    def ask_to_feed_people(self):
        """ Ask user how many bushels to feed to people. """
        value = input("> How many bushels do you want to feed the people? (They need 20 per person to not starve)")
        storeChange = int(value)
        self.calculateStore(-storeChange)
        return value

    def ask_to_plant_bushel(self):
        """ Ask user how many bushels to plant on acres """
        value = input("> How many bushels do you want to plant on the acres? (max Value = people * 10)")
        storeChange = int(value)
        self.calculateStore(-storeChange)
        return value
