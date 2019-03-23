import unittest
import City as c
import random
class CityTest(unittest.TestCase):

    def setUp(self):
        self.city = c.City()

    def test_calculate_Store(self):

        store = self.city.store
        deltaStore = -5

        self.city.calculateStore(deltaStore)
        self.assertEqual(self.city.store, store+deltaStore)

    def test_calculate_Population(self):

        population = self.city.population
        deltaPopulation = 5

        self.city.calculatePopulation(deltaPopulation)
        self.assertEqual(self.city.population, population+deltaPopulation)

    def test_disease_happens(self):
        random.seed(10)
        self.assertGreater(self.city.disease(), 0)

    def test_disease_not_happens(self):
        random.seed(123)
        self.assertEquals(self.city.disease(), 0)

    def test_rats_eat(self):
        random.seed(1)
        self.assertGreaterEqual(self.city.rats(), 0)


if __name__ == '__main__':
    unittest.main()