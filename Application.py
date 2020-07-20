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
####################################
#CODE FOR GUI
####################################
def select(click,root):
    if (click == 0):
        root.destroy()
        root=Tk()
        root.title("Upto Date with Covid-19")
        root.geometry("300x160")
        root.configure(background='black')
        var = StringVar()
        var.set("Countries")
        drop =OptionMenu(root,var,*country)
        drop.pack()
        mybutton=Button(root,text="Show graph",command=lambda:makegraphcountry(var.get(),root)).pack()

    else:
        root.destroy()
        root=Tk()
        root.title("Upto Date with Covid-19")
        root.geometry("300x160")
        root.configure(background='black')
        canvas.pack()
        var = StringVar()
        var.set("Countries")
        drop =OptionMenu(root,var,*continent)
        drop.pack()
        mybutton=Button(root,text="Show graph",command=lambda:makegraphcontinent(var.get(),root)).pack()

def main_func():
    root=Tk()
    root.title("Upto Date with Covid-19")
    
    canvas=Canvas(root,width=300,height=160)

    image=ImageTk.PhotoImage(Image.open("pic.jpg"))

    canvas.create_image(0,0,anchor=NW,image=image)
    canvas.pack()
    var=IntVar()
    var.set("3")
    mylabel=Label(root,text="SELECT").pack()
    Radiobutton(root,text="Countries",variable=var,value=0,command=lambda :select(var.get(),root)).pack()
    Radiobutton(root,text="Continents",variable=var,value=1,command=lambda :select(var.get(),root)).pack()

    root.mainloop()
main_func()