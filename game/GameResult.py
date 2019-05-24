import City as city

class GameResult:
    def __init__(self, year, population, acres, bushels):
        self.__year = year
        self.__population = population
        self.__acres = acres
        self.__bushels = bushels

    @property
    def year(self):
        return self.__year

    @property
    def population(self):
        return self.__population

    @property
    def acres(self):
        return self.__acres

    @property
    def bushels(self):
        return self.__bushels