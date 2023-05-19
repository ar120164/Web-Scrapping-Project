# Loads the Pandas library 
import pandas as pd 

# Reads data from local file 
path = "C:/Users/user/Documents/Web scrapping/dataset.csv" # Path contains the location of the spyder's output dataset
data = pd.read_csv(path) 
data = data.drop(columns=['id'])
data = data.dropna() #Drops rows that contain at least one Na
data['cause'] = data['cause'].str.replace('Cause: ', '') #Removes 'Cause: ' prefix

#Separates state and police department in two columns
data['state']= data['policeDepartment'].str[-2:] 
data['policeDepartment'] =  data['policeDepartment'].str[:-3]

#Removes police dogs (K9)
dataK9Officer = data[data.name.str.contains("K9 Officer")]
dataSinK9 = data[~data.name.str.contains("K9")]
data = dataSinK9.append(dataK9Officer)
data = data.reset_index().drop(columns=["index"])

#Separates date of End of Watch in Week-day, Month, Day and Year
split2= data['date'].str.split(',',expand=True)
data['EOW week-Day'], data['EOW month-day'], data['EOW year'] = split2[0],split2[1],split2[2]
data['EOW week-Day'] = data['EOW week-Day'].str.replace('EOW: ', '')
data = data.drop(columns=['date'])
split3= data['EOW month-day'].str.split(' ',expand=True)
data['EOW month'], data['EOW day'] = split3[1],split3[2]
data = data.drop(columns=['EOW month-day'])

#Allows to display all columns
pd.set_option('display.max_columns', None)

#Checks for empty values
print(data.isnull().values.any())

#Exports the dataframe to a csv file located in the same path where the script is stored
data.to_csv("Fallen Officers Dataset.csv") 

