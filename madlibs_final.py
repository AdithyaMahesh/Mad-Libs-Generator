

from tkinter import *

# Initialize window
w = Tk()
w.geometry('500x500')
w.title('Mad Libs Generator Python')
Label(w, text= 'Mad Libs Generator Python!' , font = 'arial 22 bold').pack()
Label(w, text = 'Choose a story :', font = 'arial 17 bold').place(x=40, y=80)


#Story functions 

# Photographer
def madlib1():

    #Close previous current window and open new one
    w.destroy()
    
    root=Tk()
    root.geometry('300x300')
    root.title("madlib1")

    #Inputs for the mad lib
    
    animals_label=Label(root, text="Enter animal", font='calibre 10 bold')
    animals_entry=Entry(root,font='calibre 10 normal')
    
    profession_label=Label(root,text="Enter Profession", font='calibre 10 bold')
    profession_entry=Entry(root,font='calibre 10 normal')

    cloth_label=Label(root,text="Enter cloth", font='calibre 10 bold')
    cloth_entry=Entry(root,font='calibre 10 normal')

    things_label=Label(root,text='Enter things',font='calibre 10 bold')
    things_entry=Entry(root,font='calibre 10 normal')

    name_label=Label(root,text="Enter name",font='calibre 10 bold')
    name_entry=Entry(root,font='calibre 10 normal')

    place_label=Label(root,text="Enter place",font='calibre 10 bold')
    place_entry=Entry(root,font='calibre 10 bold')

    verb_label=Label(root,text="Enter verb ending with ing",font='calibre 10 bold')
    verb_entry=Entry(root,font='calibre 10 normal')

    food_label=Label(root,text="Enter food",font='calibre 10 bold')
    food_entry=Entry(root,font='calibre 10 normal')

    #Submit button leads to story with given inputs
    
    def submit():
        animals_name=animals_entry.get()
        profession_name=profession_entry.get()
        cloth_name=cloth_entry.get()
        things_name=things_entry.get()
        name_name=name_entry.get()
        place_name=place_entry.get()
        verb_name=verb_entry.get()
        food_name=food_entry.get()

        root.destroy()
        
        m=Tk()
        m.geometry('1200x200')
        m.title("The photographer")
        final=Label(m, text='Say, ' +food_name+ '! The photographer said as the camera flashed! ' + name_name + ' and I had gone to ' + place_name +' to get our photos taken today',font='calibre 10 bold',fg='red')
        final2=Label(m,text='The first photo we really wanted was a picture of us dressed as ' + animals_name + ' pretending to be a ' + profession_name+'.',font='calibre 10 bold',fg='red')
        final3=Label(m,text='When we saw the second photo, it was exactly what I wanted. We both looked like ' + things_name + ' wearing ' + cloth_name + ' and ' + verb_name + ' --exactly what I had in mind!',font='calibre 10 bold',fg='red')

        final.grid()
        final2.grid()
        final3.grid()

        m.mainloop()
        

    sub_btn=Button(root, text="Submit",font ='arial 15', command = submit, bg = 'blue').place(x=90, y=240)

    #Geonetric placement of entry labels

    animals_label.grid(row=0,column=0)
    animals_entry.grid(row=0,column=1)
    profession_label.grid(row=1,column=0)
    profession_entry.grid(row=1,column=1)
    cloth_label.grid(row=2,column=0)
    cloth_entry.grid(row=2,column=1)
    things_label.grid(row=3,column=0)
    things_entry.grid(row=3,column=1)
    name_label.grid(row=4,column=0)
    name_entry.grid(row=4,column=1)
    place_label.grid(row=5,column=0)
    place_entry.grid(row=5,column=1)
    verb_label.grid(row=6,column=0)
    verb_entry.grid(row=6,column=1)
    food_label.grid(row=7,column=0)
    food_entry.grid(row=7,column=1)
    
    root.mainloop()

# Unicorns 
def madlib2():

    #Close previous current window and open new one

    w.destroy()
    
    root=Tk()
    root.geometry('300x300')
    root.title("madlib2")

    #Inputs for the mad lib
    
    noun1_label=Label(root, text="Enter noun in plural", font='calibre 10 bold')
    noun1_entry=Entry(root,font='calibre 10 normal')
    
    adj1_label=Label(root,text="Enter an adjective", font='calibre 10 bold')
    adj1_entry=Entry(root,font='calibre 10 normal')

    animal_label=Label(root,text="Enter an animal in plural", font='calibre 10 bold')
    animal_entry=Entry(root,font='calibre 10 normal')

    noun2_label=Label(root,text='Enter a noun',font='calibre 10 bold')
    noun2_entry=Entry(root,font='calibre 10 normal')

    adj2_label=Label(root,text="Enter an adjective",font='calibre 10 bold')
    adj2_entry=Entry(root,font='calibre 10 normal')

    color_label=Label(root,text="Enter a color",font='calibre 10 bold')
    color_entry=Entry(root,font='calibre 10 bold')

    adj3_label=Label(root,text="Enter an adjective",font='calibre 10 bold')
    adj3_entry=Entry(root,font='calibre 10 normal')

    noun3_label=Label(root,text="Enter a noun",font='calibre 10 bold')
    noun3_entry=Entry(root,font='calibre 10 normal')

    noun4_label=Label(root,text="Enter a plural noun",font='calibre 10 bold')
    noun4_entry=Entry(root,font='calibre 10 normal')

    adj4_label=Label(root,text="Enter an adjective",font='calibre 10 bold')
    adj4_entry=Entry(root,font='calibre 10 normal')

    place_label=Label(root,text="Enter a place",font='calibre 10 bold')
    place_entry=Entry(root,font='calibre 10 bold')

    #Submit button leads to story with given inputs
    
    def submit():
        noun1=noun1_entry.get()
        adj1=adj1_entry.get()
        animal=animal_entry.get()
        noun2=noun2_entry.get()
        adj2=adj2_entry.get()
        color=color_entry.get()
        adj3=adj3_entry.get()
        noun3=noun3_entry.get()
        noun4=noun4_entry.get()
        adj4=adj4_entry.get()
        place=place_entry.get()


        root.destroy()
        
        m=Tk()
        m.geometry('1200x200')
        m.title("The photographer")
        final=Label(m, text="Unicorns aren't like other "+noun1+";they're "+adj1+".\nThey look like "+animal+", with "+noun2+" for feet and a "+adj2+" mane of hair.",font='calibre 10 bold',fg='red')
        final2=Label(m,text="But unicorns are "+color+" and have a "+adj3+" "+noun3+" on their heads."+"Some "+noun4+" don't believe unicorns are "+adj4+", but I believe in them!",font='calibre 10 bold',fg='red')
        final3=Label(m,text="I would love to take my unicorn to "+place,font='calibre 10 bold',fg='red')

        final.grid()
        final2.grid()
        final3.grid()

        m.mainloop()
        

    sub_btn=Button(root, text="Submit",font ='arial 15', command = submit, bg = 'blue').place(x=90, y=240)
    
    #Geonetric placement of entry labels

    noun1_label.grid(row=0,column=0)
    noun1_entry.grid(row=0,column=1)
    adj1_label.grid(row=1,column=0)
    adj1_entry.grid(row=1,column=1)
    animal_label.grid(row=2,column=0)
    animal_entry.grid(row=2,column=1)
    noun2_label.grid(row=3,column=0)
    noun2_entry.grid(row=3,column=1)
    adj2_label.grid(row=4,column=0)
    adj2_entry.grid(row=4,column=1)
    color_label.grid(row=5,column=0)
    color_entry.grid(row=5,column=1)
    adj3_label.grid(row=6,column=0)
    adj3_entry.grid(row=6,column=1)
    noun3_label.grid(row=7,column=0)
    noun3_entry.grid(row=7,column=1)
    noun4_label.grid(row=8,column=0)
    noun4_entry.grid(row=8,column=1)
    adj4_label.grid(row=9,column=0)
    adj4_entry.grid(row=9,column=1)
    place_label.grid(row=10,column=0)
    place_entry.grid(row=10,column=1)
    
    root.mainloop()

# School Lunch 
def madlib3():

    #Close previous current window and open new one

    w.destroy()
    
    root=Tk()
    root.geometry('300x300')
    root.title("madlib3")

    #Inputs for the mad lib
    
    food_label=Label(root, text="Enter a type of food", font='calibre 10 bold')
    food_entry=Entry(root,font='calibre 10 normal')
    
    girl_label=Label(root,text="Enter a girl's name", font='calibre 10 bold')
    girl_entry=Entry(root,font='calibre 10 normal')

    adj1_label=Label(root,text="Enter an adjective", font='calibre 10 bold')
    adj1_entry=Entry(root,font='calibre 10 normal')

    bird_label=Label(root,text='Enter a noun',font='calibre 10 bold')
    bird_entry=Entry(root,font='calibre 10 normal')

    verb1_label=Label(root,text="Enter a verb in the past tense",font='calibre 10 bold')
    verb1_entry=Entry(root,font='calibre 10 normal')

    verb2_label=Label(root,text="Enter another verb in the past tense",font='calibre 10 bold')
    verb2_entry=Entry(root,font='calibre 10 bold')

    verb3_label=Label(root,text="Enter a third verb in the past tense",font='calibre 10 bold')
    verb3_entry=Entry(root,font='calibre 10 normal')

    noun1_label=Label(root,text="Enter a noun",font='calibre 10 bold')
    noun1_entry=Entry(root,font='calibre 10 normal')

    #Submit button leads to story with given inputs
    
    def submit():
        food=food_entry.get()
        girl=girl_entry.get()
        adj1=adj1_entry.get()
        bird=bird_entry.get()
        verb1=verb1_entry.get()
        verb2=verb2_entry.get()
        verb3=verb3_entry.get()
        noun1=noun1_entry.get()

        root.destroy()
        
        m=Tk()
        m.geometry('1200x200')
        m.title("School Lunch")
        final=Label(m, text="It was " + food + " day at school, and " + girl + " was super " + adj1 + " for lunch. But when she went outside to eat, a " + bird + " stole her " + food + "! " + girl + " chased the " + bird + " all over school.",font='calibre 10 bold',fg='red')
        final2=Label(m,text="She " + verb1 + ", " + verb2 + ", and " + verb3 + " through the playground. Then she tripped on her " + noun1 + " and the " + bird + " escaped! Luckily, " + girl + "'s friends were willing to share their " + food + " with her.",font='calibre 10 bold',fg='red')

        final.grid()
        final2.grid()

        m.mainloop()
        

    sub_btn=Button(root, text="Submit",font ='arial 15', command = submit, bg = 'blue').place(x=90, y=240)

    #Geonetric placement of entry labels

    food_label.grid(row=0,column=0)
    food_entry.grid(row=0,column=1)
    girl_label.grid(row=1,column=0)
    girl_entry.grid(row=1,column=1)
    adj1_label.grid(row=2,column=0)
    adj1_entry.grid(row=2,column=1)
    bird_label.grid(row=3,column=0)
    bird_entry.grid(row=3,column=1)
    verb1_label.grid(row=4,column=0)
    verb1_entry.grid(row=4,column=1)
    verb2_label.grid(row=5,column=0)
    verb2_entry.grid(row=5,column=1)
    verb3_label.grid(row=6,column=0)
    verb3_entry.grid(row=6,column=1)
    noun1_label.grid(row=7,column=0)
    noun1_entry.grid(row=7,column=1)
    
    root.mainloop()
   
#Buttons to select story
Button(w, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'blue').place(x=60, y=120)
Button(w, text= 'Unicorns', font ='arial 15', command = madlib2, bg = 'blue').place(x=90, y=240)
Button(w, text= 'School Lunch', font ='arial 15', command = madlib3, bg = 'blue').place(x=80, y=360)

#Execute window
w.mainloop()


