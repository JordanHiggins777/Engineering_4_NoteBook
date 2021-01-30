# CAD
<details>
  <summary>Onshape Assignments</summary>
<details>
<summary>CASTER</summary>
<details>
<summary>Part 1 - Base</summary>

  <p align="center">
  <img width="300" src="https://github.com/JordanHiggins777/Onshape/blob/main/Base.jpg">
</p>
</details>
  <details>
<summary>Part 2 - Mount</summary>
      <p align="center">
  <img width="300" src="https://github.com/JordanHiggins777/Onshape/blob/main/Mount.jpg">
</p>
</details>
  <details>
<summary>Part 3 - Fork</summary>

          
  <img width="300" src="https://github.com/JordanHiggins777/Onshape/blob/main/Fork.jpg">
</p>
</details>
  <details>
<summary>Part 4 - Tire</summary>
          <p align="center">
  <img width="300" src="https://github.com/JordanHiggins777/Onshape/blob/main/Wheel.jpg">
</p>
</details>
  <details>
<summary>Part 5 - Wheel</summary>
          <p align="center">
  <img width="300" src="https://github.com/JordanHiggins777/Onshape/blob/main/Wheel2.jpg">
</p>
</details>
    <details>
<summary>Parts 6-9 Axle, Collar, Bearings</summary>
          <p align="center">
  <img width="300" src="https://github.com/JordanHiggins777/Onshape/blob/main/Axle.jpg">
</p>         
      <p align="center">
  <img width="200" src="https://github.com/JordanHiggins777/Onshape/blob/main/Bearing.jpg">
</p>
</details>
    <details>
<summary>Sub-Assembly</summary>
          <p align="center">
  <img width="300" src="https://github.com/JordanHiggins777/Onshape/blob/main/Sub_Assem.jpg">
</p>
</details>
   <details>
<summary>Final Caster Assembly</summary>
          <p align="center">
  <img width="300" src="https://github.com/JordanHiggins777/Onshape/blob/main/Final_Assem.jpg">
</p>
</details>
</details>
   <details>
<summary>Onshape Challenge</summary>
This is a dropdown with text!
</details>
   <details>
<summary>Dorothy's Dowel Pins</summary>
          <p align="center">
  <img width="300" src="https://github.com/JordanHiggins777/Onshape/blob/main/Frame.jpg">
</p>
</details>
</p>
</details>


# Python Assignments
<details>
<summary>Python Assignments</summary>
<details>
<summary>Hello PI</summary>

## Objective: 
Power up my Rasperry PI then wrtie a program that spits out "Hello World!" 10 times.
## Prossess:
Given this was the first assignment of the year, the actual prossess of writing the code and powering on my Pi were very simple given Dr.Sheilds had given a step by step tutorial(LINK: https://youtu.be/FFUm7omFLUE) on how to do the assignment. Just follow this step by step and youll be done assuming no technecal errors.
## Code Explanation: 
All this assignment is, is 2 lines of code
```
for i in range(0,10):          ## this sets the amount of times the loop runs for in this case it's 10 times.
	print("Hello, World!")      ##this prints any statment in the quotations.
```
## Problems and Solutions:
#### Problem 1: 
Your PI does not turn on
#### Solution 1:
Turn it off and on again. If that does not work you may have a fualty pi especially if your PI starts to heat up.
#### Problem 2:
The 2 lines of code simply do not work
#### Solution 2:
Check to make sure its a ".py" file, check that your pi led is on, and check for any misspellings in the code.
## Diagram/Picture:

  <p align="center">
  <img width="300" src= "https://github.com/JordanHiggins777/Engineering_4_NoteBook/blob/main/hello.png">
	
## Reflection: 
While this assignment is by far the simplest it may have taken the most time out of any. With the transition to at home engineering and the fact Ive never used a raspberry PI didnt help. 
## Resources:
Dr.Sheilds Step by Step https://youtu.be/FFUm7omFLUE

</p>
</details>
  <details>
<summary>Get the Pi online</summary>
            
## Objective: 
Make a Engineering 4 notebook in GitHub.
## Prossess:
This was another assignment that was provided a youtube video as a resorce(LINK:https://www.youtube.com/watch?v=9IpcrxeftwE&feature=emb_title).Getting the PI online was a bit difficult for me personaly because of my pi disintegrating the SD cards it came in contact with, thus I had to get a new PI in person, and that was a prossess in itself because this is 2020 and getting sheadules to match up is a nightmare. Regardless I eventually got the new PI online and a engineering 4 notebook up. The hardest part of the actual assignment was this one glitch where it didnt reconize my account, I just shoutdown the pi and tried again. My guess is this just came down to a typo error. Other then that I had no problems.
## Code Explanation:
N/A whoops no code.
## Problems and Solutions:
#### Problem 1:
My pi is getting hot and the green light wont turn on
#### Solution 1: 
Get a new PI

#### Problem 2:
The .conf command does not reconize your account
#### Solution 2: 
Restart from the begining it might be a typing error(It was for me)

## Reflection:
Given you are reading this I did eventually get this assignment done. This was a easy assignment that wouldve taken ~ one day to complete in different senario, hopefully in the near future 2020 quarantine will be over.    
## Resources: 
The step by step https://www.youtube.com/watch?v=9IpcrxeftwE&feature=emb_title

</p>
</details>
  <details>
<summary>Python Assignment 0: Hello Python/Dice Roller  </summary>
            
## Objective:
write code that functions as a six sided die.
## Prossess:
First things first, google "python dice roller" youll find various snipbits of code that work but you might have to make some changes for sake of simplicity. 
## Code Explanation:
```
import random
```
this allows for randomness to exist when we use it for the dice roller
```

question = input('Would you like to roll the dice [y/n]?\n')
```
Input is a piece of code that asks for a user input. The way I like to think about it is "Input" replaces what would be a "Print". For example if one replaced Input with print the code would be - print('Would you like to roll the dice [y/n]?\n') -  all this would do is spit out the statment in quotations. Input asks for a users INPUT or just to type something following the statment. When you call input something in this case "question" you can then call upon it later.
```
while question != 'n':
    if question == 'y': #questions are prints requireing a input after 
        die = random.randint(1, 6) #sets range from 1-6
        print(die)  #print a number 1-6
        question = input('Would you like to roll the dice [y/n]?\n')
    else:
        print('Invalid response. Please type "y" or "n".') #prints a statement
        question = input('Would you like to roll the dice [y/n]?\n')        

print('Good-bye!')
```
The rest of the code involves making a while loop then setting a variable equal to a number from 1-6 then just asking for the user to type y or n to continue spitting out numbers.
## Diagram:
  <p align="center">
  <img width="300" src= "https://github.com/JordanHiggins777/Engineering_4_NoteBook/blob/main/dice.png">
	
## Reflection:
This was the first coding assignment of the year,in that you code a simple dice roller. This assignment will introduce to you basic inputs, and randomizers. Looking back this assignment wasnt too hard and its a good way to dip your toes into coding at the begining of the year.
## Resources:
https://www.pythonforbeginners.com/code-snippets-source-code/game-rolling-the-dice

</p>
</details>
<details>
<summary>Python Assignment 1: Calculator  </summary>
              
## Objective: 
Program a basic calculator that calculates, sum, difference, quotient, and modulo of two numbers.
## Prossess: 
Just like dice, calculators are very common and thus code for calculators are also very common. A quick google search will give you all the resorces you need its pretty surface level. 
## Code Explanation:
```
def doMath(a,b):
	print("Sum:", a+b)
	print("Difference:", a-b)
	print("Product", a*b)
	print("Quotient", round(a/b, 2))
	print("Modulo", a%b)
```
This is a function that runs a and b through all these expressions then prints out the result.
```
number_1 = float(input("Enter the first number:"))
number_2 = float(input("Enter the second number"))


(doMath(number_1,number_2))
```
The remaining code sets a and b as terms in this case I just used number 1 and 2. Then just print the numbers and there you have your calculator.

## Problems and Solutions:
Problem 1: My code is far too long

Solution 1: Make sure you make a function that any 2 terms could run through not hardcode.

## Diagram:

## Reflection: 
This was a simple fun assignment by this point code is finally getting into my system as a skill.

</p>
</details>
  <details>
<summary>Python Assignment 2: Quadratic Solver  </summary>
 
## Objective: 
Write code that solves basic algebraic quadratic equation
## Prossess:
This assignment started out with a simmilar prosses to the calculator, where I have a fuction that uses the variables I put in as a user. I imagined the code as the calculator code, but rather than a/b it would be the quadratic equation.
## Code Explanation:
## Problems and Solutions:
## Diagram:
  <p align="center">
  <img width="300" src= "https://github.com/JordanHiggins777/Engineering_4_NoteBook/blob/main/quad.png">
## Reflection:
</p>
</details>
  <details>
<summary>Python Assignment 3: Strings and Loops- Vertical Sentence  </summary>
            
## Objective:
Write code that turns a horizontial sentence into a vertical one.
## Prossess:
## Code Explanation:
## Problems and Solutions:
## Diagram:
  <p align="center">
  <img width="300" src= "https://github.com/JordanHiggins777/Engineering_4_NoteBook/blob/main/strandloops.png">
## Reflection: 
</p>
</details>
  <details>
<summary>Python Pseudo Project: Hangman Game   </summary>
            
# WIP
</p>
</details>
  <details>
<summary>GPIO Pins:Bash  </summary>
            
## Objective:
Make a blinking led
## Prossess: 
Just wire up a led/leds then write some bash code, bash sucks but the main issue was figuring out this bit of code

```
while [ $count -lt 10 ];
# when the counter ($ - a variable) is less than 10:
do
```
at this point I've forgotten how I got this code but here it is, all this assignment is is alternateing Led blinks much like many other engineering assignments. The only difference is the bash part but it's diferences in formatting and things like gpio pin out vs output. 
## Diagram:
## Reflection: 
Its mainly a lot of learning what bash is and figuring out how to not to think in "python". It's just a bit of change in look, however I still prefer python overall maybe I'm just set in my ways.  
</p>
</details>
  <details>
<summary>GPIO Pins:Python   </summary>
            
## Objective:
Do the same thing as the previous assignment but in python.
## Prossess: 
This assignment is pretty simple the biggest challenge is not think about the code in a "bash" mindset. At this point I was thinking of how to convert bash code to python code when the best way to go about it is just to make new code thats a python led blink.
## Code Explanation:
```
from gpiozero import LED
from time import sleep

led1 = LED(17)

while True:
	led1.on()
	sleep(0.5)
	led1.off()
	sleep(0.5)
```
This code is VERY simple just set the led to a pin turn it on boom.
## Diagram: 
I could take a picture in real life of my wiring or you could look at this fritzing diagram made by a fellow student kudos to him
https://github.com/rmckee75/Engineering_4_Notebook/blob/main/images/GPIOBashWiring.png

## Reflection: 
Looking back this is one of the easier assignments 
</p>
</details>
  <details>
<summary>GPIO Pins:SSH </summary>
            
## Objective:
Make your pi wireless.
## Prossess: 
So a lot of the diffucultly in this assignment was in that my Pi kinda just died for no reason, but apart from that just follow the directions and youll be mostly there. The only thing that relates to code in this assignment is a simple blink code
## Code :

## Reflection: 
Make sure everything is as simple as possible, if you have any wiring from previous assignments get rid of it. On the topic of I would reccomend doing ssh before any other GPIO assignment.   
</p>
</details>
  <details>
<summary>GPIO Pins - I2C</summary>
            
## Objective:
## Prossess:
## Code Explanation:
## Problems and Solutions:
## Diagram:
## Reflection: 
</p>
</details>
  <details>
<summary>Difficulty Chart  </summary>

| Assignments        | Difficulty rating out of 10 | How you should budget time  |
| ------------- |:-------------:| -----:|
| Hello PI    | 1 | ~2 Days |
| Get the Pi online   | 3      |  ~ 1 week |
| Python Assignment 0: Hello Python/Dice Roller | 4    |  ~1 week   |
| Python Assignment 1: Calculator | 4      |    ~2 days |
| Python Assignment 2: Quadratic Solver | 5      |   ~ 3 days|
| Python Assignment 3: Strings and Loops- Vertical Sentence | 6      |    ~ 1 week |
| Python Pseudo Project: Hangman Game | 10    |  ~1.5 Weeks   |
| GPIO Pins:Bash |  3     |    ~1 day |
|  GPIO Pins:Python    | 5      |   ~ 1.5 days |
| Assignment 7 Hello VS code |  2     |    ~1 day |
| Assignment 8 Fancy LED     | 6      |   ~1 week |
| Assignment 7 Hello VS code |  2     |    ~1 day |
| Assignment 8 Fancy LED     | 6      |   ~1 week |
</p>
</details>

</p>
</details>
