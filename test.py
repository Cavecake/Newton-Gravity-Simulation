import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv("DataTypes/log.csv")

print("DF loaded")

df.plot.scatter(x = "x0", y = "y0").get_figure().savefig('test2.png')

#plt.show()