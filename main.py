### BMI CALCULATOR 

import tkinter
root = tkinter.Tk()
root.title("BMI calculator")

#Create function(s)
def calculate_bmi():
    kg=float(entry_kg.get())
    height=float(entry_height.get())
    bmi=round(kg/height**2,2)
    label_result['text']=f"BMI:{bmi}"


##Create GUI
label_kg=tkinter.Label(root, text="KG:")
label_kg.pack()


label_height=tkinter.Label(root, text="HEIGHT:")
label_height.pack()


label_result=tkinter.Label(root, text="RESULT:")
label_result.pack()

entry_kg=tkinter.Entry(root)
entry_kg.pack()

entry_height=tkinter.Entry(root)
entry_height.pack()

button_calculate=tkinter.Button(root,text="Calculate",command = calculate_bmi)
button_calculate.pack()

root.mainloop()