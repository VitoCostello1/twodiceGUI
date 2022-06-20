"""
Program: twodiceGUI.py 
Author: Vito 6/10/2022

GUI-based version of the Two Dice game from the Java class 
"""

from breezypythongui import EasyFrame
from tkinter.font import Font 
import random
# other imports

class twodiceGUI(EasyFrame):
	# "ApplicationName" will change from project to project 

	# definition of the __init__() method which is our class constructor
	def __init__(self):
		# call the EasyFrame version of the __init__

		EasyFrame.__init__(self, title = "Two Dice Game", resizable = False, background = "#663399",width = 320, height = 280 )
		self.titleFont = Font(weight = "bold", size = 24)
		self.title = self.addLabel(text = "Two Dice Game",row = 0, column = 0, font = self.titleFont, background = "#663399", sticky = "NSEW", columnspan = 2 )
		self.addLabel(text = "Player's Roll",row = 1, column = 0)
		self.addLabel(text = "Computer's Roll", row = 2, column = 0)
		self.playerRoll = self.addIntegerField(value =  0, row = 1, column = 1, state = "readonly")
		self.computerRoll = self.addIntegerField(value = 0, row = 2, column = 1, state = "readonly")
		self.button = self.addButton(text = "ROLL!", row = 3, column = 0, columnspan = 2,command = self.roll)
		self.resultArea = self.addLabel(text = "result will display here after rolling of dice of who won!", row = 4, column = 0, sticky = "NSEW", rowspan = 2, columnspan = 2)
		
	def roll(self):
		self.playerRoll.setValue(random.randint(1,6))
		self.computerRoll.setValue(random.randint(1,6))

		if self.playerRoll.getValue() > self.computerRoll.getValue():
			self.resultArea["text"] = "You are winner!"
		elif self.playerRoll.getValue() < self.computerRoll.getValue():
			self.resultArea["text"] = "You lose? roll again to test your luck!"
		else:
			self.resultArea["text"] = "Tie? roll again test your luck!"


# definition of the main() method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	twodiceGUI().mainloop()

# global call to the main() method 
main()