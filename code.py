# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections
#Path of the file is stored in the variable path
data = pd.read_csv(path)
data.rename(columns = {"Total":"Total_Medals"}, inplace =True)
print(data.head(10))

#Code starts here
data["Better_Event"] = np.where(data["Total_Summer"] == data["Total_Winter"],"Both",(np.where(data["Total_Summer"] > data["Total_Winter"],"Summer","Winter")))
better_event = data["Better_Event"].value_counts().idxmax()
print(better_event)
# Data Loading 
top_countries = data[["Country_Name","Total_Summer","Total_Winter","Total_Medals"]]

top_countries.drop(index = 146 ,axis = 0,inplace = True)
# Top 10
def top_ten(df,col_):
    country_list  = []
    country_list = country_list+ list(df.nlargest(10,col_)["Country_Name"])
    return country_list

top_10_summer = top_ten(top_countries,"Total_Summer")
top_10_winter = top_ten(top_countries,"Total_Winter")
top_10 = top_ten(top_countries,"Total_Medals")
print(top_10_summer)
print(top_10_winter)
print(top_10)
common = [x for x in collections.Counter(top_10_summer+top_10_winter+top_10) if collections.Counter(top_10_summer+top_10_winter+top_10)[x] == 3]
print(common)
# Plotting top 10
summer_df = data[data["Country_Name"].isin(top_10_summer)]
plt.xticks(rotation = 90)
plt.title("Summer Olympics Performance")
plt.bar(summer_df["Country_Name"],summer_df["Total_Summer"] )
plt.show()
winter_df = data[data["Country_Name"].isin(top_10_winter)]
plt.xticks(rotation = 90)
plt.title("Winter Olympics Performance")
plt.bar(winter_df["Country_Name"],winter_df["Total_Winter"])
plt.show()
top_df = data[data["Country_Name"].isin(top_10)]
plt.xticks(rotation = 90)
plt.title("Overall Performance")
plt.bar(top_df["Country_Name"],top_df["Total_Medals"])
plt.show()
# Top Performing Countries

summer_df["Golden_Ratio"] = summer_df["Gold_Summer"]/summer_df["Total_Summer"]
summer_max_ratio = summer_df["Golden_Ratio"].max()
summer_country_gold = summer_df[summer_df["Golden_Ratio"]==summer_max_ratio]["Country_Name"]
winter_df["Golden_Ratio"] = winter_df["Gold_Winter"]/winter_df["Total_Winter"]
winter_max_ratio = winter_df["Golden_Ratio"].max()
winter_country_gold = winter_df[winter_df["Golden_Ratio"]==winter_max_ratio]["Country_Name"]
top_df["Golden_Ratio"] = top_df["Gold_Total"]/top_df["Total_Medals"]
top_max_ratio = top_df["Golden_Ratio"].max()
#top_country_gold = top_df[top_df["Golden_Ratio"] == top_max_ratio]["Country_Name"].astype(str)
top_country_gold = data.iloc[top_df["Golden_Ratio"].idxmax()]["Country_Name"]
# Best in the world 
data_1 = data.drop(index = 146 , axis = 0)
data_1["Total_Points"] = data_1["Gold_Total"]*3 + data_1["Silver_Total"]*2 + data_1["Bronze_Total"]
most_points = data_1["Total_Points"].max()
best_country = data_1.iloc[data_1["Total_Points"].idxmax()]["Country_Name"]

# Plotting the best
best = data[data["Country_Name"] == best_country]
best = best[["Gold_Total","Silver_Total","Bronze_Total"]]
best.plot.bar(stacked = True)
plt.xlabel(best_country)
plt.ylabel("Medals Tally")
plt.xticks(rotation= 45)
plt.show()


print(top_max_ratio)
print(top_country_gold)




