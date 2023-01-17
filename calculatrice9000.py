from tkinter import *

formule = ""
def click(num): 
    global formule 
    formule += str(num) 
    equation.set(formule)

def equalclick():
    global formule
    result = str(eval(formule))
    equation.set(result)
    formule = result

def sqrt():
    global formule
    if formule != "":
        i = 1
        while (i * i) < float(formule):
            i+= 1
        if i * i == float(formule):
            result = i
            equation.set(str(result))
            formule = result
        else:
            result = "Racine pas entière"
            equation.set(str(result))
            formule = result
    else:
        result = "Entrez d'abord la valeur"
        equation.set(result)
        formule = result

def effacer():
    global formule
    equation.set("")
    formule=""

def square():
    global formule
    if formule != "":
        result = float(formule) * float(formule)
        equation.set(result)
        formule = result
    else:
        result = "Entrez d'abord la valeur"
        equation.set(result)
        formule = result



print("Il faut effacer le champ d'écriture après chaque calcul \nPour les élévations au carés et les racines le calcul se fait directement et il faut bien effacer avant de recalculer \nPour les racines carrées la calculette ne prends en charge que les racines avec un résultat entier\n")


fenetre=Tk()
fenetre.geometry("235x300")
fenetre.configure(bg='#2b2d2f')
fenetre.title("calculatrice9000")
equation = StringVar()
formule_field = Entry(textvariable=equation)
formule_field.grid(columnspan=4, ipadx = 20 , ipady = 2)
#bouttons chiffres
btn_1 = Button(fenetre, text=' 1 ', command=lambda: click(1), height=2, width=2, bg='#5f6062')
btn_1.grid(row=2, column=0)
btn_2 = Button(fenetre, text=' 2 ', command=lambda: click(2), height=2, width=2, bg='#5f6062') 
btn_2.grid(row=2, column=1) 
btn_3 = Button(fenetre, text=' 3 ', command=lambda: click(3), height=2, width=2, bg='#5f6062') 
btn_3.grid(row=2, column=2) 
btn_4 = Button(fenetre, text=' 4 ', command=lambda: click(4), height=2, width=2, bg='#5f6062') 
btn_4.grid(row=3, column=0)  
btn_5 = Button(fenetre, text=' 5 ', command=lambda: click(5), height=2, width=2, bg='#5f6062') 
btn_5.grid(row=3, column=1)  
btn_6 = Button(fenetre, text=' 6 ', command=lambda: click(6), height=2, width=2, bg='#5f6062') 
btn_6.grid(row=3, column=2)  
btn_7 = Button(fenetre, text=' 7 ', command=lambda: click(7), height=2, width=2, bg='#5f6062') 
btn_7.grid(row=4, column=0)  
btn_8 = Button(fenetre, text=' 8 ', command=lambda: click(8), height=2, width=2, bg='#5f6062') 
btn_8.grid(row=4, column=1)  
btn_9 = Button(fenetre, text=' 9 ', command=lambda: click(9), height=2, width=2, bg='#5f6062') 
btn_9.grid(row=4, column=2)  
btn_0 = Button(fenetre, text=' 0 ', command=lambda: click(0), height=2, width=2, bg='#5f6062') 
btn_0.grid(row=5, column=1)
#bouttons chiffres
# boutons opérations
divide = Button(fenetre,text=' / ', command=lambda: click("/"), height=2, width=2, bg='#ff9800') 
divide.grid(row=2, column=3)

multiply = Button(fenetre,text=' * ', command=lambda: click("*"), height=2, width=2, bg='#ff9800') 
multiply.grid(row=3, column=3)

minus = Button(fenetre,text=' - ', command=lambda: click("-"), height=2, width=2, bg='#ff9800') 
minus.grid(row=4, column=3)

plus = Button( fenetre,text=' + ', command=lambda: click("+"), height=2, width=2, bg='#ff9800') 
plus.grid(row=5, column=3) 
 
sqrt = Button(fenetre, text=' √ ', command = sqrt, height = 2, width = 2)
sqrt.grid(row = 5, column=0)

pourcent = Button(fenetre, text=' % ', command = lambda: click("%"), height = 2, width = 2)
pourcent.grid(row = 5, column=2)

square = Button(fenetre, text = ' ² ', command = square, height = 2, width = 2)
square.grid(row=6, column=0)
#bouttons opérations
#egalité
equal = Button(fenetre,text=' = ', command=lambda: equalclick(), height=2, width=2, bg='#ff9800') 
equal.grid(row=6, column=3)
#egalité

# boutton decimal
Decimal= Button(fenetre,text='.', command=lambda: click('.'), height=2, width=2) 
Decimal.grid(row=6, column=2)
# boutton decimal

# boutton effacer
effacer = Button(fenetre,text='effacer', command=effacer, height=2, width=2) 
effacer.grid(row=6, column=1) 
#boutton effacer

fenetre.mainloop()