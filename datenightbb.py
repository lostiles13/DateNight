# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 17:22:40 2021

@author: lastiles
"""

import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd 
import random
import webbrowser


class Test(tk.Tk): 
    def __init__(self):
        super().__init__()
        sto = ttk.Style()
        #sto.configure('W.TButton', font= ('Times new roman', 15),
                      #foreground='black')
        self.geometry('1200x800')
        self.title("It's date night baby!")
        self.configure(bg = 'plum1')
        #self.resizable(0,0)
        
        self.columnconfigure(1, weight = 3)
        
        # labels
        self.label_border = tk.Frame(self, highlightbackground = 'black',
                                highlightthickness = 2, bd = 0)
        self.label1 = tk.Label(self.label_border, text = "Hey baby! It's date night!\nWould you like a virtual, active, or TOTALLY random date?",
                          bg = 'lemon chiffon', font = ('Kerning',20))
        self.label_border.grid(column = 1, row = 2)
        self.label1.grid(column = 1, row = 2)

        # Radio buttons 
        self.theme = tk.IntVar()
        self.virtual_frame = tk.Frame(self, highlightbackground = 'black',
                                highlightthickness = 1, bd = 0)
        self.virtual = tk.Radiobutton(self.virtual_frame, text = 'Virtual', 
                                 variable = self.theme, font = ('Times new roman',18),
                                 activebackground = 'pink', bg = 'sky blue',
                                 value = 1)
        self.virtual_frame.grid(column = 1, row = 9)
        self.virtual.grid(column = 1, row = 9)
        self.active_frame = tk.Frame(self, highlightbackground = 'black',
                                highlightthickness = 1, bd = 0)
        self.active = tk.Radiobutton(self.active_frame, text = 'Active',
                                     font = ('Times new roman',18),
                                 activebackground = 'pink', bg = 'sky blue',
                                variable = self.theme, 
                                value = 2)
        self.active_frame.grid(column =1, row = 10)
        self.active.grid(column = 1, row = 10)
        self.random_frame = tk.Frame(self, highlightbackground = 'black',
                                highlightthickness = 1, bd = 0)
        self.random = tk.Radiobutton(self.random_frame, text = 'Random', 
                                    font = ('Times new roman',18),
                                 activebackground = 'pink', bg = 'sky blue',
                                variable = self.theme, 
                                value = 3)
        self.random_frame.grid(column = 1, row = 11)
        self.random.grid(column = 1, row = 11)
        
        # button frames and buttons
        
        self.buttonA = tk.Button(self, text = 'Give me my date', 
                                 font = ('Times new roman',18),
                                 activebackground = 'pink', bg = 'aquamarine2',
                                  command = self.changeText)
        self.buttonB = tk.Button(self, text = '', 
                                 font = ('Times new roman',18),
                                 activebackground = 'pink', bg = 'aquamarine2',
                                 command = self.play_game)
        self.buttonC = tk.Button(self, text = 'I want another option', 
                                font = ('Times new roman',18),
                                 activebackground = 'pink', bg = 'aquamarine2',
                                 command = self.changeText)
        
        self.buttonA.grid(column = 1, row = 13)
        self.buttonB.grid(column = 1, row = 14)
        self.buttonC.grid(column = 1, row = 15)
        
        self.mainloop()
        
    
    def changeText(self): 
        self.df = pd.read_csv('master.csv')
        idea = []
        indices = []
        self.index = tk.IntVar()
        # to get active date 
        if self.theme.get() == 1: 
            for i in range(0, len(self.df)):
                if self.df['Theme'][i] == 'Virtual':
                    idea.append(self.df['Date idea'][i])
                    indices.append(i)
            self.date_index = random.randint(0,len(idea)-1)
            self.index.set(indices[self.date_index])
            self.date_night = idea[self.date_index]
        
        if self.theme.get() == 2: 
            for i in range(0, len(self.df)):
                if self.df['Theme'][i] == 'Active':
                    idea.append(self.df['Date idea'][i])
                    indices.append(i)
            self.date_index = random.randint(0,len(idea)-1)
            self.index.set(indices[self.date_index])
            self.date_night = idea[self.date_index]
            
        if self.theme.get() == 3: 
            for i in range(0, len(self.df)):
                idea.append(self.df['Date idea'][i])
                indices.append(i)
            self.date_index = random.randint(0,len(idea)-1)
            self.date_night = idea[self.date_index]
            self.index.set(indices[self.date_index])
        
        #print(self.index.get())
        # to get virtual date
            
        # to get random date
        self.buttonB['text'] = f'Play {self.date_night}'
        #self.index = self.date_index
    def play_game(self): 
        
        if self.index.get() == 8: 
            self.card_button2 = tk.Button(self, text = '       ',
                                          font = ('Times new roman',18),
                                 activebackground = 'pink', bg = 'medium orchid',
                                          command = self.card_url)
            self.card_button2.grid(column = 1, row = 24)
            self.card_button = tk.Button(self, text = 'Gimme a card game', 
                                         font = ('Times new roman',18),
                                 activebackground = 'medium orchid', bg = 'medium orchid',
                                    command = self.play_cards)
            self.card_button.grid(column = 1, row = 20)
            
        url = self.df['Url'][int(self.index.get())]
        if url != 'none':
            webbrowser.open(url)
    def play_cards(self): 
        self.df2 = pd.read_csv('card.csv')
        self.card_index = random.randint(0,len(self.df2)-1)
        self.card_game = self.df2['Date idea'][self.card_index]
        
        self.card_button2['text'] = f'Play {self.card_game}'
    
    def card_url(self): 
        
        if len(self.card_game.split(" ")) == 2:
            
            url_string = self.card_game.lower().replace(" ", "-")
        else: 
            url_string = self.card_game.lower().replace(" ", "-")

        
        url_start = f'https://playingcards.io/game/{url_string}'
        
        webbrowser.open(url_start)
        
app = Test()
app.mainloop()