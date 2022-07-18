import numpy as np
import pandas as pd
file = pd.read_csv("C:/Users/aruni/PycharmProjects/script/Bitcoin.csv")
file = file.set_index(pd.DatetimeIndex(file['Date'].values))

# User Invested amount
#Amount

Amount = int(input("Enter the Amount you invested:$"))

#Date(yyyy-mm-dd)

Date = input("Enter the Date on investment(yyyy-mm-dd)(2022-05-09):")
print('\t', Amount,"\n",Date)

#Low price & High price of the day to store and return

#low_1 = data.get('Low')
#High_1 = data.get('High')
Low_1 = 'Low'
High_1 = 'High'
Value_1 = file[Low_1][Date]
Value_2 = file[High_1][Date]

#Quantity of crypto assest

invest_1 = int(Amount)/ Value_1
invest_2 = int(Amount)/ Value_2
print(invest_1)

#profit of crypto

print(file[Low_1][-1])
profit_1 = (round(invest_1,4) * file[Low_1][-1]) - int(Amount)
profit_2 = (round(invest_2,4) * file[High_1][-1]) - int(Amount)
print(profit_1)

#Amount made as profit or loss

print('the profit and loss price between $',profit_1, 'and also $',profit_2, 'on',file["Date"][-1])

#return of investment

rot1 =  profit_1/ int(Amount) * 100
rot2 =  profit_2/ int(Amount) * 100
print("The return of investment will be between",round(rot1,2),"% and",round(rot2,2),"%")