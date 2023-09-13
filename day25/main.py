import pandas

data = pandas.read_csv('./centralpark.csv')



my_hash = {'color':['Cinnamon','Gray','Black'],
           'count':[0,0,0]
           }

newData = data['Primary Fur Color'].tolist()

# this is not efficient because it creates an additional n usage of memory

for item in newData:
    if item == 'Gray':
        my_hash['count'][1]+=1
    if item == 'Cinnamon':
        my_hash['count'][0]+=1
    if item == 'Black':
        my_hash['count'][2]+=1

# this step however is essentially cycling thru all the data and doing the same thing data['Primary Fur Color']=='Gray
# would have done. so this would've been o(3n) if i had used angela's method

# however, my way makes it o(n).. does this really matter?

# i think the bigger problem is the amount of space i used in memory


finalDF = pandas.DataFrame.from_dict(my_hash)


print(finalDF)