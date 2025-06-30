import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


nfl_data = pd.read_csv('NFL_Distance.csv')

nfl_data_by_dist = nfl_data.sort_values(by='total_dist', ascending=True)

qbr_data = pd.read_csv('NFL_QBR_EPA.csv')



sns.regplot(x='total_dist', y='tot_winp', data=nfl_data_by_dist, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
plt.xlabel('Total Yearly Distance Traveled (in Miles)')
plt.ylabel('Winning Percentage')
plt.title('Total Distance Traveled vs Yearly Winning Percentages')
plt.show()

sns.regplot(x='div_dist', y='div_winp', data=nfl_data_by_dist, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
plt.xlabel('Total Yearly Distance Traveled within the Division (one way, in miles)')
plt.ylabel('Divisional Winning Percentage')
plt.title('Total Divisional Distance Traveled vs Yearly Divisional Winning Percentages')
plt.show()

qbr_data['Long_Diff'] = qbr_data['long_qbr'] - qbr_data['avg_qbr']
qbr_data['Short_Diff'] = qbr_data['short_qbr'] - qbr_data['avg_qbr']

# Positions for grouped bars
x = np.arange(len(qbr_data))  # number of QBs
width = 0.35  # width of the bars

fig, ax = plt.subplots(figsize=(14, 6))

bars1 = ax.bar(x - width/2, qbr_data['Long_Diff'], width, label='Longest Travel')
bars2 = ax.bar(x + width/2, qbr_data['Short_Diff'], width, label='Shortest Travel')

# X-axis labels
ax.set_xticks(x)
ax.set_xticklabels(qbr_data['player_name'], rotation=45, ha='right')

# Labels and legend
ax.set_ylabel('QBR Difference from Season Avg')
ax.set_title('QB Performance in Longest vs Shortest Travel Games (vs Season Avg)')
ax.axhline(0, color='gray', linewidth=1, linestyle='--')
ax.legend()

plt.tight_layout()
plt.show()

# Melt into long format if needed
long_data = pd.DataFrame({
    'QB': qbr_data['player_name'],
    'Distance': qbr_data['long_dist'],
    'QBR_Change': qbr_data['Long_Diff'],
    'Travel_Type': 'Longest'
})

short_data = pd.DataFrame({
    'QB': qbr_data['player_name'],
    'Distance': qbr_data['short_dist'],
    'QBR_Change': qbr_data['Short_Diff'],
    'Travel_Type': 'Shortest'
})

combined = pd.concat([long_data, short_data])

sns.scatterplot(data=combined, x='Distance', y='QBR_Change', hue='Travel_Type')
plt.axhline(0, color='gray', linestyle='--')
plt.title('QBR Change vs Travel Distance')
plt.xlabel('Distance Traveled (miles)')
plt.ylabel('QBR Difference from Season Avg')
plt.show()
