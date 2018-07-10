
# ## Pandas is responsible to handle dataframes
import pandas as pd
# ## Reading the csv file using pandas 
df = pd.read_csv('tab.csv')
# ## Importing library to handle date and time
import datetime
today = datetime.date.today()
# ## Assigning them in seperate variables to use further
yearry = today.year
monthy = today.month
daye = today.day
# ### convert the existing EXP DATE to  pandas readable format using to_datetime
df['newExp'] = pd.to_datetime(df['EXP DATE'])

# ## Below is the logic that filter out expiring tablets today
# From our newExp column just checking every column that matches with this year using a.year == yearry , similarly date and month and assign that information to a new variable chronos
chronos = df[df['newExp'].map(lambda a:a.year == yearry and a.month == monthy and a.day == daye)]

# ## Export the data frame into csv using pandas to_csv command
chronos.to_csv('Tablets That Expire After {}.csv'.format(today),index=False)
print('Process Completed!')
