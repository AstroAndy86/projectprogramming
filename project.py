
'''This program computes helpful things for Physics/Astronomy
Created by: Andrea Guzman Mesa '''

import numpy as np
import matplotlib.pyplot as plt
import wx
from wx.lib.masked import NumCtrl #Textboxes only accepts numbers

import wx
class ExampleFrame(wx.Frame):
    def __init__(self, parent):
        
        wx.Frame.__init__(self, parent,size=(700,600))
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        #Title
        self.quote = wx.StaticText(self, label="This Program Calculates Helpful Things for Physics: ")
        grid.Add(self.quote, pos=(0,0))
        
        self.semi=0.1
        self.mass=0.1
        self.ecc=0.1
    
        
        # Labels for theInputs and Outputs
        self.mass_label=wx.StaticText(self, label="Mass:")
        grid.Add(self.mass_label, pos=(2,0))
        
        self.semi_label=wx.StaticText(self, label="Semimajor Axis:")
        grid.Add(self.semi_label, pos=(4,0))
        
        self.ecc_label=wx.StaticText(self, label="Eccentricity:")
        grid.Add(self.ecc_label, pos=(6,0))
        
        self.vel_label=wx.StaticText(self, label="Velocity:")
        grid.Add(self.vel_label, pos=(2,4))
        
        self.newton_label=wx.StaticText(self, label="Newton's First Law:")
        grid.Add(self.newton_label, pos=(4,4))
        
        self.kepler_label=wx.StaticText(self, label="Kepler's Law:")
        grid.Add(self.kepler_label, pos=(6,4))
        
        
        #Input Boxes
        self.mass_input=wx.TextCtrl(self, size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.getmass, self.mass_input)
        grid.Add(self.mass_input, pos=(2,2))
        
        self.semi_input=wx.TextCtrl(self, size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.getsemi, self.semi_input)
        grid.Add(self.semi_input, pos=(4,2))
        
        self.ecc_input=wx.TextCtrl(self, size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.getmass, self.ecc_input)
        grid.Add(self.ecc_input, pos=(6,2))  
        
        #submit button 
        self.submit_button= wx.Button(self, label="SUBMIT", size=(140,-1))
        grid.Add(self.submit_button, pos=(8,2))
        
        
        #OutputBoxes
        
        self.force_output=wx.TextCtrl(self, size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.getforce, self.force_output)
        grid.Add(self.force_output,pos=(2,6))
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.submit_button)
        
        self.kepler_output=wx.TextCtrl(self, size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.getkepler, self.kepler_output)
        grid.Add(self.kepler_output,pos=(4,6))
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.submit_button)
        
        self.vel_output=wx.TextCtrl(self, size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.getvel, self.vel_output)
        grid.Add(self.vel_output, pos=(6,6))
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.submit_button)
        
      
               
        
        hSizer.Add(grid, 0, wx.ALL, 6)
        mainSizer.Add(hSizer, 0, wx.ALL, 6)
        self.SetSizerAndFit(mainSizer)
        self.Show(True)
        
        
    def getmass(self,event):
        self.mass=float(self.mass_input.GetValue())
        
    def getsemi(self,event):
        self.semi=float(self.semi_input.GetValue())
    
    def getecc(self,event):
        self.ecc=float(self.ecc_input.GetValue())
        
    def getforce(self):
        self.force_output.SetValue(str(self.force))
    
    def getkepler(self):
        self.kepler_output.SetValue(str(self.kepler))
        
    def getvel(self):
        self.vel_output.SetValue(str(self.vel))
        
            
    def OnClick(self,event):
        self.kepler=np.sqrt((4.0*np.pi)*(self.semi)**3.0/(2.0*self.mass))
        self.vel=np.sqrt(3.0*self.mass/2.0)  
        self.force=self.mass*self.vel
        
        print self.kepler
        self.getkepler()
        self.getforce()
        self.getvel()
   
    def OnExit(self, e):
        self.Close(True)        
        

app = wx.App(False)
ExampleFrame(None)
app.MainLoop()