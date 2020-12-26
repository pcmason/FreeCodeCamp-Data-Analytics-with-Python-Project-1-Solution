import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 'date')

# Clean data
#mask to filter out the views that are below the 2.5th percentile
lvMask = df['value'] >= df['value'].quantile(0.025)
#mask to filter out the views that are above the 97.5th percentile
hvMask = df['value'] <= df['value'].quantile(0.975)
#filter these values out of df
df = df.loc[lvMask & hvMask]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure()
    plt.plot(df)
    #set the set the title 
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    #set the x and y axis labels
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = ['date'])

    #clean the data 
    #mask to filter out the views that are below the 2.5th percentile
    lvMask2 = df_bar['value'] >= df_bar['value'].quantile(0.025)
    #mask to filter out the views that are above the 97.5th percentile
    hvMask2 = df_bar['value'] <= df_bar['value'].quantile(0.975)
    df_bar = df_bar.loc[lvMask2 & hvMask2]

    #get the values from date
    df_bar['Years'] = df_bar['date'].dt.year 
    df_bar['month'] = df_bar['date'].dt.month
    #change the type of month to string
    df_bar['month'] = df_bar['month'].astype('str')
    #replace the numerical values with the month values
    df_bar['month'].replace({"1": "January", "2":"February",      "3":"March",
                         "4":"April", "5":"May", "6": "June",
                         "7": "July", "8":"August", "9": "September",
                         "10":"October", "11": "November",
                         "12": "December"}, inplace = True)
    #set the order for the hue
    order = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']

    fig, ax = plt.subplots(figsize = (14, 6))
    # Draw bar plot
    sns.barplot(x = 'Years', y = 'value', hue = 'month',hue_order =             order, estimator = np.mean,
            palette = 'bright', data = df_bar, ci = None, ax = ax)
    ax.set_ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    #set date to datetime
    df_box['date'] = pd.to_datetime(df_box['date'])
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2,  figsize = (14, 6))
    #plot the first boxplot
    sns.boxplot(x = 'year', y = 'value', data = df_box, ax = ax1)
    #set the labels
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')  
    ax1.set_ylabel('Page Views')
    #get the new order for the months
    order2 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
         'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    #plot the second boxplot
    sns.boxplot(x = 'month', y = 'value', data = df_box, ax = ax2, order = order2)
    #set the labels 
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
