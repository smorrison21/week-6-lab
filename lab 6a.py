#NAMES

import matplotlib.pyplot as plt
import pandas as pd
import datetime
import os
# Load the file UNRATE.csv, which shows the seasonally-adjusted US unemployment
# rate, monthly, from 2000 to present.  Create a line plot, with vertical
# lines to mark recessions:
#   March 2001 - November 2001
#   December 2007 - June 2009
#   February 2020 - April 2020
# Next continue to clean up the figure, adding a title, axis labels, shading the area
# that designates recessions, and any other changes that come to mind. If you manually
# copy-pasted the code for each recession line, try instead to put them in containers
# and use a for-loop.
os.chdir(r'/Users/sarahmorrison/Downloads/GitHub/')
base_path = r'/Users/sarahmorrison/Downloads/GitHub/'
og_data_path = os.path.join(base_path, 'week-6-lab/unrate.csv')
unrate = pd.read_csv(og_data_path, parse_dates=['DATE'])

fig, ax = plt.subplots()
for m in unrate:
    m.plot(x='DATE', y='UNRATE',
               ax=ax,
               kind='line')

x=unrate['DATE']
y=unrate['UNRATE']             

ax = unrate.plot(x='DATE', y='UNRATE', linestyle='solid', color='black', legend=False, linewidth=.7)

ax.axvline('2001-03-01', color='r', linestyle=':')
ax.axvline('2001-11-01', color='r', linestyle=':', label='March 2001 – November 2001 Recession')

ax.axvline('2007-12-01', color='b', linestyle=':')
ax.axvline('2009-06-01', color='b', linestyle=':')

ax.axvline('2020-02-01', color='g', linestyle=':')
ax.axvline('2020-04-01', color='g', linestyle=':')

ax.set_ylabel('Unemployment Rate')
ax.set_xlabel('Date')
ax.set_title('Monthly US Unemployment Rate 2000-2022')
