Month = ("January","Febuary","March","April","May","June","July","August","September","October","November","December")
Profit = (120,140,190,150,200,110,100,160,220,240,290,400) 

max_profit = max(Profit)
max_profit_index = Profit.index(max_profit)
print(max_profit_index)
max_profit_month = Month[max_profit_index]
print("The Maximum Profit of "+str(max_profit) +" was Recorded in the Month of "+str(max_profit_month))

min_profit = min(Profit)
min_profit_index = Profit.index(min_profit)
print(min_profit_index)
min_profit_month = Month[min_profit_index]
print("The Minimum Profit of "+str(min_profit) +" was Recorded in the Month of "+str(min_profit_month))

