import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

#get the BMI by dividing weight by height divided by 100 and squared
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)

# Add 'overweight' column
#if BMI is > 25, overweight = 1, else = 0
df['overweight'] = np.where(df['BMI'] > 25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    #group the data based on cardio
    df_cat = df_cat.groupby(['cardio','variable', 'value'], as_index = False).size().rename(columns={'size':'total'})

    # Draw the catplot with 'sns.catplot()'
    #fig, ax = plt.subplots(figsize = (12, 6))
    #fig = plt.figure()
    fig = sns.catplot(x = 'variable',y = 'total', hue = 'value', col = 'cardio', kind = 'bar', data = df_cat).fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    #make the masks to clean the data 
    #mask for ap_lo greater than ap_hi
    apMask = df['ap_lo'] <= df['ap_hi']
    #mask for height < 2.5th percentile
    shrtMask = df['height'] >= df['height'].quantile(0.025)
    #mask for height > 97.5th percentile
    tallMask = df['height'] <= df['height'].quantile(0.975)
    #mask for weight < 2.5th percentile
    skinMask = df['weight'] >= df['weight'].quantile(0.025)
    #mask for weight > 97.5th percentile
    hugeMask = df['weight'] <= df['weight'].quantile(0.975)
    #use the masks created to easily clean the df
    df_heat = df.loc[apMask & shrtMask & tallMask & skinMask & hugeMask]

    df_heat = df_heat.drop(columns = ['BMI'])

    # Calculate the correlation matrix
    corr = round(df_heat.corr(), 1)

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones(corr.shape)).astype(np.bool)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (12, 6))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot = True, fmt = ".1f", mask = mask)
    #plt.show()

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
