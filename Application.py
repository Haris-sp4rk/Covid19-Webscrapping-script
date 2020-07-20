from tkinter import *
from PIL import ImageTk,Image
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import collections
###################################
#CODE FOE WEB SCRAPPING
###################################
website='https://www.worldometers.info/coronavirus/#countries'
website_url=requests.get(website).text
soup = BeautifulSoup(website_url,'html.parser')
my_table = soup.find('tbody')
country= []
continent= []
table_data2= []
table_data = []
I=0
for row in my_table.findAll('tr'):
    I=I+1
    row_data = []
    for cell in row.findAll('td'):
        row_data.append(cell.text)
    if (I > 7):
         if(len(row_data) > 0):
            country.append(row_data[1])
            data_item = {"Country": row_data[1],
                        "TotalCases": row_data[2],
                        "NewCases": row_data[3],
                        "TotalDeaths": row_data[4],
                        "NewDeaths": row_data[5],
                        "TotalRecovered": row_data[6],
                        "ActiveCases": row_data[7],
                        "CriticalCases": row_data[8],
                        "Totcase1M": row_data[9],
                        "Totdeath1M": row_data[10],
                        "TotalTests": row_data[11],
                        "Tottest1M": row_data[12],
            }
            table_data.append(data_item)
    else:
         if(len(row_data) > 0):
           continent.append(row_data[1])
           data_item = {"Continent": row_data[1],
                        "TotalCases": row_data[2],
                        "NewCases": row_data[3],
                        "TotalDeaths": row_data[4],
                        "NewDeaths": row_data[5],
                        "TotalRecovered": row_data[6],
                        "ActiveCases": row_data[7],
                        "CriticalCases": row_data[8],
                        "Totcase1M": row_data[9],
                        "Totdeath1M": row_data[10],
                        "TotalTests": row_data[11],
                        "Tottest1M": row_data[12],
            }
         table_data2.append(data_item)
     
df = pd.DataFrame(table_data2) 
df.to_excel('Covid19_datacontinent.xlsx', index=True)
df = pd.DataFrame(table_data)
df.to_excel('Covid19_data.xlsx', index=True)
###############################
#METHODS TO PLOT GRAPHS
###############################
def makegraphcountry(var,lol):
            lol.destroy()
            for cont in table_data:
                for i in cont:
                    if(cont[i]==var):
                        newdict=cont
                        a = sorted(newdict.items(), key=lambda x: x[1])
                        sort_orders=collections.OrderedDict(a)
                        sort_orders.pop("Country")
                        x=list(sort_orders.keys())
                        x.reverse()
                        y=list(sort_orders.values())
                        y.reverse()
                        plt.title(var)
                        plt.xlabel('Categories')
                        plt.ylabel('Numbers')

                        plt.bar(x,y,color=['r','b','g'])
                        plt.show()
                        break
            main_func()   
           

def makegraphcontinent(var,lol):
            lol.destroy()
            for cont in table_data2:
                for i in cont:
                   if(cont[i]==var): 
                        newdict=cont
                        a = sorted(newdict.items(), key=lambda x: x[1])
                        sort_orders=collections.OrderedDict(a)
                        sort_orders.pop("Continent")
                        x=list(sort_orders.keys())
                        x.reverse()
                        y=list(sort_orders.values())
                        y.reverse()
                        plt.title(var)
                        plt.xlabel('Categories')
                        plt.ylabel('Numbers')
                        plt.bar(x,y,color=['r','b','g'])
                        plt.show()
                        break
            main_func()          
