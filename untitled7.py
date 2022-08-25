from tkinter import*
import random

root=Tk()
root.title("Sales Application")
root.geometry("500x500")

month=("January","February","March","April","May","June","July","August",
       "September","October","November","December")
profit= (10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000)
def max_profit():
max_profit= max(profit)
max_profit_index= profit.index(max_profit)
max_profit_month= month[max_profit_index]

def min_profit
min_profit= min(profit)
min_profit_index= profit.index(min_profit)
min_profit_month= month[min_profit_index]

btn= Button(root, text= "Show Max Profiable Month", command= max_profit)
btn= Button(root, text= "Show Min Profiable Month", command= min_profit)

place.button(max_profit)
place.button(min_profit)