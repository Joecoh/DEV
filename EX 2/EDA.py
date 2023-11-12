# Load the required libraries 
import pandas as pd 
import numpy as np 
import seaborn as sns

# Load the data 
df = pd.read_csv('titanic.csv')

# View the data 
df.head()

# Find the duplicates 
df.duplicated().sum()

# Unique values 
df['Pclass'].unique()
df['Survived'].unique()
df['Sex'].unique()

# Plot the unique values 
sns.countplot(df['Pclass']).unique()

# Replace null values 
df.replace(np.nan, 'O', inplace=True)

# Check the changes now 
df.isnull().sum()

# Find null values 
df.isnull().sum()

# Filter data 
df[df['Pclass']==1].head()

# Boxplot 
df[['Fare']].boxplot()
