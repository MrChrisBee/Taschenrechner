# Taschenrechner
Simple Calculator Test with Tkinter
Using tkinter i try to make a calculator with as less typing as good.
Instead of pack i use grid.
Defining a Function which creates the Buttons
I use too Tupels, one with the text and one with the command in it,
looping over this a call the predefined function and create a butten with every thing i need

status jet: not uploaded 
            one can see the buttons with the text on it 
            i can press them and got a individual predifined text on the console
            
try to implement 
  
Main think to do is evaluate (eval()) the String i got from input.
Calculating 5+7= leads to a string containing 5+7 and the evaluation because = was pressend.
The order in which calculation takes place should ensure by Python eval() (* / before -+ and so on)
Worklfow should be type a number, recognizing that it's done when a operation is pressed. If this is = ?
7+          calcstr = "7+"
5*          calcstr = calcstr + "5*"

3=          calcstr = calcstr + "3" (7+5*3)   

print(eval("7+5*3")) works as Expected

This is limited to +-*/=. 