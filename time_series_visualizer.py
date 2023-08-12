# link to replit code: https://replit.com/@MauricioFiorent/boilerplate-page-view-time-series-visualizer

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
df.index = pd.to_datetime(df.index)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
  fig = plt.figure()
  plt.plot(df.index, df['value'],  color='red')
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page Views')

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar['year'] = df_bar.index.year
  df_bar['month'] = df_bar.index.month
  df_bar = df_bar.groupby([df_bar['year'], df_bar['month']]).mean()
  df_bar = pd.pivot_table(df_bar, values='value', index='year', columns='month')

  # Draw bar plot
  df_bar = df_bar.plot(kind='bar')
  fig = df_bar.get_figure()
  df_bar.set_xlabel('Years')
  df_bar.set_ylabel('Average Page Views')
  plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], title='Months')

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)
  fig, subplot = plt.subplots(1, 2)
  sns.boxplot(df_box, x='year', y='value', ax=subplot[0]).set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')
  sns.boxplot(df_box, x='month', y='value', ax=subplot[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']).set(xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (Seasonality)')

  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
