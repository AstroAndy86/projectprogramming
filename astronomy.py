#!/usr/bin/python

'''This small program computes the weight and the age in other planets
Created by: Andrea Guzman Mesa
As part of the Course: Programming Skills for Astrophysics
21/01/2017

This is actually my 4th trial! But I'm improving!
'''

import numpy as np
import matplotlib.pyplot as plt
import wx

class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="CALCULATOR WEIGHT AND AGE ON OTHER PLANETS :", pos=(20, 30))
        
        self.pfactors=[0.4155,0.8975,1.0,0.166,0.3507,2.5374,1.0677,0.8947,0.0899 ] #Gravity Factors
        self.pdays=[88.0, 225.0, 365.0,687.0,4307.0,10731.0,30660.0,59860.0,90520.0] #Days per year planet
        self.kilos=0.0
        self.age=0.0 

        self.planet_id = 0

        # text output
        self.textout = wx.TextCtrl(self, pos=(400,20), size=(200,300), 
                                  style=wx.TE_MULTILINE | wx.TE_READONLY)
       
        # Submit Button
        self.button =wx.Button(self, label="Submit", pos=(200, 325))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)

        # Show the label and the receives the input for the weight
        self.lblkilos = wx.StaticText(self, label="Your Weight on kilos:",pos=(20,60))
        self.editkilos = wx.TextCtrl(self, value="Enter Weight",pos=(160, 60), size=(100,-1))
      
        # Show the label and the receives the input for the Age
        self.lblage = wx.StaticText(self, label="Your Age in Years:",pos=(20,100))
        self.editage = wx.TextCtrl(self, value="Enter your age",pos=(160, 100), size=(100,-1))

        # Radio Boxes to choose in which planet you would like to know the weight and age
        radioList = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter',
                     'Saturn', 'Uranus', 'Neptune', 'Pluto']
        rb = wx.RadioBox(self, label="On which Planet ?",pos=(20, 160), choices=radioList, majorDimension=3, style=wx.RA_SPECIFY_COLS)

        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)


    #Gets from pfactors the value corresponding to the planet in radioList
    def EvtRadioBox(self, event):
        self.planet_id = event.GetInt()
        print self.pfactors[self.planet_id]
    
    #Stores the value for weight
    def getkilos(self):
        self.kilos=float(self.editkilos.GetValue())
        return self.kilos
    
    #Stores the value for age  
    def getage(self):
        self.age=float(self.editage.GetValue())
        return self.age
    
    #when you submit it makes the fucntions work and output the corresponding value and print the value
    def OnClick(self,event):
        self.textout.Clear()
        self.kilos = self.getkilos()
        self.age = self.getage()
        myoutput = self.examplefunction()
        myoutput2= self.examplefunction1()  
        self.textout.AppendText("Your weight:"+myoutput+"\n"+"Your Age(days):"+myoutput2)

    #Calculates the weight
    def examplefunction(self): # kilos * times * planet_id 
        x = self.getkilos()*self.pfactors[self.planet_id]
        return str(x)+"\n"
    
    #Calculates the Age
    def examplefunction1(self): #Age*365/planet_id
        y = self.getage()*365.0/self.pdays[self.planet_id]
        return str(y)


app = wx.App(False)
frame = wx.Frame(None,size=(700,400))
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()
    