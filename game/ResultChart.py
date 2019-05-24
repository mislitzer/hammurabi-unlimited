import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ResultChart():
    def __init__(self, data):
        width = .35

        years = []
        pop = []
        acres = []
        bushels = []

        for d in data:
            years.append(d.year)
            pop.append(d.population)
            acres.append(d.acres)
            bushels.append(d.bushels)

        print("YEARS----")
        print(years)

        print("POP----")
        print(pop)

        print("ACRES----")
        print(acres)

        print("BUSHELS----")
        print(bushels)

        m1_t = pd.DataFrame({
            'year': years,
            'pop': pop,
            'acres': acres,
            'bushels': bushels
        })

        m1_t[['acres','bushels']].plot(kind='bar', width = width)
        m1_t['pop'].plot(secondary_y=True, label='population', legend=True)

        ax = plt.gca()
        plt.xlim([-width, len(m1_t['bushels'])-width])
        ax.set_xticklabels(m1_t['year'])

        plt.show()
