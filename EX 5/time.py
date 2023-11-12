import pandas as pd
from matplotlib import pyplot

# reading the dataset using read_csv
df = pd.read_csv("stock_data.csv", parse_dates=True, index_col="Date")

# displaying the first five rows of the dataset
print(df.head())

# Plot the time series data
series = pd.read_csv('daily-minimum-temperatures.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
series.plot()
pyplot.show()

# Plot the time series data with black dots
series.plot(style='k.')
pyplot.show()

# Plot a histogram of the time series data
series.hist()
pyplot.show()

# Boxplot by year
groups = series.groupby(pd.Grouper(freq='A'))
years = pd.DataFrame()

for name, group in groups:
    years[name.year] = group.values

years.boxplot()
pyplot.show()
