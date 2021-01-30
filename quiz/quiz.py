# Python program to create a simple GUI 
# Simple Quiz using Tkinter 

#import everything from tkinter
from tkinter import *
# and import messagebox as mb from tkinter
from tkinter import messagebox as mb
#import json to use json file for data
import json

#class to define the components of the GUI
class Quiz:
    #initialize the methods and attributes
    def __init__(self):
        # set question number to 0
        self.q_no=0
        # passing the first question to the ques
        self.ques=self.display_question(self.q_no)
        # opt_selected holds an integer value
        self.opt_selected=IntVar()
        # displaying radio button
        self.opts=self.radio_buttons()
        # display options
        self.display_options(self.q_no)
        # showing buttons
        self.buttons()
        # no of questions
        self.data_size=len(question)
        # keep a counter of correct answers
        self.correct=0

   #This method is used to display the result
    def display_result(self):
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        # Shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}") 

    # This method checks the Answer after we click on Next.
    def check_ans(self, q_no):
        # checks for if the selected option is correct
        if self.opt_selected.get() == answer[q_no]:
            # if the option is correct it return true
            return True 

    # This is a method to increment the correct answer and move to
    # the next Question.
    def next_btn(self):
        # Check if the answer is correct
        if self.check_ans(self.q_no):
            # if the answer is correct it increments the correct by 1
            self.correct += 1
        # Moves to next Question by incrementing the q_no counter
        self.q_no += 1
        # checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:
            # if it is correct then it displays the score
            self.display_result()
            # destroys the GUI
            gui.destroy()
        # if it is not then
        else:
            # shows the next question
            self.display_options(self.q_no) 
    
    # This method shows the two buttons on the screen
    def buttons(self):
        # The first button is the Next button to move to the
        # next Question
        next_button = Button(gui, text="Next",command=self.next_btn,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        # palcing the button  on the screen
        next_button.place(x=350,y=380)
        # This is the second button which is used to Quit the GUI
        quit_button = Button(gui, text="Quit", command=gui.destroy,
        width=5,bg="black", fg="white",font=("ariel",16," bold"))
        # placing the Quit button on the screen
        quit_button.place(x=700,y=50) 
    
    # This method shows the text of the options
    def display_options(self,q_no):
        val=0
        # selecting the option button
        self.opt_selected.set(0)
        # shows the question options
        self.ques['text']=question[q_no]
        # looping over the question to be displayed
        for option in options[q_no]:
            self.opts[val]['text']=option
            val+=1
            
    # This method shows the title and the Question on the screen
    def display_question(self, q_no):
        # The title to be shown
        title = Label(gui, text="GeeksforGeeks QUIZ", 
        width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
        # place of the title
        title.place(x=0, y=2)
        # setting the Quetion properties
        q_no = Label(gui, text=question[q_no], width=60, 
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        #placing the option on the screen
        q_no.place(x=70, y=100)
        # returns the question and title
        return q_no
    
    # This method shows the radio buttons to select the Question
    def radio_buttons(self):
        # initialize the list with an empty list of options
        q_list = []
        # position of the first option
        y_pos = 150
        # adding the options to the list
        while len(q_list) < 4:
            # setting the radio button properties
            radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",14))
            # adding the button to the list
            q_list.append(radio_btn)
            # placing the button
            radio_btn.place(x = 100, y = y_pos)
            # incrementing the y-axis position by 40
            y_pos += 40
        # return the radio buttons
        return q_list

# Create a GUI Window
gui = Tk()

# set the size of the GUI Window
gui.geometry("800x450")
# set the title of the Window
gui.title("GeeksforGeeks Quiz")

# get the data from the json file
with open('data.json') as f:
    data = json.load(f)

# set the question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])

# create an object of the Quiz Class.
quiz = Quiz()

# Start the GUI
gui.mainloop()

# END OF THE PROGRAM