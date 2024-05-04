#Sarah Morrison

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = sns.load_dataset('iris')
sns.scatterplot(x='sepal_length', y='petal_length',
                data=df, hue='species')
plt.show()

#Recreate this plot in Matplotlib, without using Seaborn!
#Then try adding some of your own customizations to the 
#plot using MatPlotLib methods
os.chdir(r'/Users/sarahmorrison/Downloads/GitHub/')
base_path = r'/Users/sarahmorrison/Downloads/GitHub/'
og_data_path = os.path.join(base_path, 'week-4-lab/iris.csv')
iris = pd.read_csv(og_data_path)

fig, ax = plt.subplots()
grouped = iris.groupby('species')
colors = {'setosa': 'red', 'versicolor': 'blue', 'virginica': 'green'}

for key, group in grouped:
    group.plot(x='sepal_length', y='petal_length',
               ax=ax,
               kind='scatter',
               color=colors[key],
               label=key.capitalize())
leg = ax.legend()
leg.set_title('species')
plt.show()

fig = ax.get_figure()
fig, ax = plt.subplots()

ax.set_ylabel('petal_length')
ax.set_xlabel('sepal_length')
