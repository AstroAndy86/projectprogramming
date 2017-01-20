#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''This small program computes the weight and the age in other planets.
Also, it gives some cool details about each one. Working on receiving the date of birth and computing
not only the age but also the ephemerids on that day in any planet.
Created by: Andrea Guzman Mesa
As part of the Course: Programming Skills for Astrophysics
21/01/2017

This is actually my 4th trial! But I'm improving!
'''

import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
import ephem
import wx

class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetForegroundColour((0,225,0)) #Changes the Font Color
        self.quote = wx.StaticText(self, label="CALCULATOR WEIGHT AND AGE ON OTHER PLANETS :", pos=(20, 30))
        self.font= wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.quote.SetFont(self.font)  
        self.SetBackgroundColour(wx.BLACK) #Changes the color of the Panel
        
        

        #Initialize the Variables and define the arrays containing the factor of weight and years,
        
        self.pfactors=[0.4155,0.8975,1.0,0.166,0.3507,2.5374,1.0677,0.8947,0.0899 ] #Gravity Factors
        self.pdays=[88.0, 225.0, 365.0,687.0,4307.0,10731.0,30660.0,59860.0,90520.0] #Days per year planet
        self.pcomments=["Mercury is a really hot planet!","Venus is beautiful but dangerous","Earth is home!","Mars looks amazing","Jupiter is the biggest planet","Saturn has lovely rings!","Uranus is great","Neptune is a gaseous planet","Pluto is no loger a planet xD "]
        self.kilos=0.0
        self.age=0.0 

        self.planet_id = 0

        # Text output
        self.textout = wx.TextCtrl(self, pos=(400,20), size=(200,300), 
                                  style=wx.TE_MULTILINE | wx.TE_READONLY)
       
        # Submit Button
        self.button =wx.Button(self, label="Submit", pos=(200, 325))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        
        # Show the label and the receives the input for the weight
        self.lblkilos = wx.StaticText(self, label="Your Weight In kilos:",pos=(20,60))
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
        myoutput3= self.examplefunction3()
        myoutput4= self.examplefunction4()
        self.textout.AppendText("Your weight:"+myoutput+"\n"+"Your Age:"+myoutput2+"\n "+"\n "+myoutput3+"\n "+"\n"+myoutput4)
        self.font= wx.Font(15, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.textout.SetFont(self.font)

    #Calculates the weight and uses the astronomy library to give the right units
    def examplefunction(self): # kilos * times * planet_id 
        x = (self.getkilos()*self.pfactors[self.planet_id])*u.kg
        return str(x)+"\n"
    
    
    #Calculates the Age and uses the astronomy library to give the right units
    def examplefunction1(self): #Age*365/planet_id
        y = (self.getage()*365.0/self.pdays[self.planet_id])
        #m=y.to(u.yr)
        print y
        return str(y)
    
    #Here, i would like to compute the RA and DEC of the choosen planet in the Birth's date.. working on that
    def examplefunction4(self):
        mars = ephem.Mars()
        mars.compute('2008/1/1')
        a=mars.ra
        b=mars.dec
        print a, b
        return str(a)+"RA \n"+str(b)+"DEC \n"

        
    
    def examplefunction3(self): #comments about the planets
        z= self.pcomments[self.planet_id]
        return str(z)
        
    


app = wx.App(False)
frame = wx.Frame(None,size=(700,400))
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()

    
