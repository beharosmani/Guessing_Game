from tkinter import *
from tkinter import messagebox
import random

class GuessNumber:
    random_number=0 
    number_of_guesses=0 
    bc='SystemButtonFace'

    def __init__(self,root,title,geometry):
        
        self.root=root
        self.root.title(title)
        self.root.geometry(geometry)


        self.label_enter_number=Label(self.root,text="Pick a number grater than zero")
        self.label_enter_number.pack(pady=5)

        self.input_top_range_number=Entry(self.root,width=20)
        self.input_top_range_number.pack(pady=2)

        btnTopRange=Button(self.root,text="Enter top range",command=self.topRangeFunc,width=12)
        btnTopRange.pack(pady=5)



        self.label_guess_number=Label(self.root,text="Enter the guessing number")
        self.label_guess_number.pack(pady=5)

        self.input_guess_number=Entry(self.root,width=20)
        self.input_guess_number.pack(pady=2)

        self.btnGuess=Button(self.root,text="Guess",command=self.mainFunction,width=12)
        self.btnGuess.pack(pady=5)


        self.label_nr_guesses=Label(self.root,text="Number of guesses")
        self.label_nr_guesses.pack(pady=8)

        # self.var=StringVar()
        # self.label_value=Label(self.root,textvariable=self.var,relief=RAISED,width=15)
        # self.label_value.pack(pady=3)

        # self.info=StringVar()
        # self.label_info=Label(self.root,textvariable=self.info,text="Guess the number Game",relief=RAISED,font=('Helvetica',14)).pack(pady=20)

        self.label_info=Label(self.root,text="Guess the number Game",font=("Helvetica",16))
        self.label_info.pack(pady=20)
        
        self.root.resizable(True,True)
        self.root.mainloop()

    # @classmethod
    # def setVar(cls):
    #     cls.var.set(cls.number_of_guesses)

    def topRangeFunc(self):
       
        try:
            top_range_number=int(self.input_top_range_number.get()) 
            self.number_of_guesses=0
           
            self.label_nr_guesses.config(text="Number of guesses:"+str(self.number_of_guesses))

            if(top_range_number<=0):
                messagebox.showerror("Error",'Number should be higher than zero')
            else:
                self.random_number=random.randint(0,top_range_number)
        except:
             messagebox.showerror("Error","The value must be a number")
            
        finally:
            root.config(background=self.bc)

    
    def mainFunction(self):
        

        try:
            
            guess_number=int(self.input_guess_number.get())
            self.number_of_guesses+=1
            self.label_nr_guesses.config(text="Number of guesses:"+str(self.number_of_guesses))
            
       

            dif=abs(guess_number-self.random_number)

            if(self.random_number==guess_number): 
                
                self.label_info.config(text="You got it!",font=('Brush Script MT',18))
        
            elif(guess_number<self.random_number): 
                
                 self.label_info.config(text="Your guess is below the number",font=('Brush Script MT',18))

            else:
               
                self.label_info.config(text="Your guess is above the number",font=('Brush Script MT',18))
            
        except:
            messagebox.showerror("Error","The value must be a number")
        finally:
            self.input_guess_number.delete(0,END)
            if(dif<10):
                bc=f'#ff{dif}{dif}{dif}{dif}'
            elif(dif>10):
                bc=f'#{1}{1}{1}{1}ff'
            
            root.config(background=bc)
            self.label_info.config(background=bc)
            


root=Tk()
g=GuessNumber(root,'Guess Number','350x350')