from tkinter import *

# Nouvelle Fenêtre
window = Tk()
# Couleur d'arrière plan de la fenêtre
window["bg"] = "#dbf0fc"
# Titre de la fenêtre
window.title("Calculatrice")
# Dimensions de la fenêtre
window.geometry("1080x720")

# Calc touches
## Ligne 1
btn_C = Button(window, text="C").grid(row=1,column=1)
btn_lpar = Button(window, text="(").grid(row=1,column=2)
btn_rpar = Button(window, text=")").grid(row=1,column=3)
btn_divide = Button(window, text="/").grid(row=1,column=4)
## Ligne 2
btn_9 = Button(window, text="9").grid(row=2,column=1)
btn_8 = Button(window, text="8").grid(row=2,column=2)
btn_7 = Button(window, text="7").grid(row=2,column=3)
btn_multiply = Button(window, text="*").grid(row=2,column=4)
## Ligne 3
btn_6 = Button(window, text="6").grid(row=3,column=1)
btn_5 = Button(window, text="5").grid(row=3,column=2)
btn_4 = Button(window, text="4").grid(row=3,column=3)
btn_sub = Button(window, text="-").grid(row=3,column=4)
## Ligne 4
btn_3 = Button(window, text="3").grid(row=4,column=1)
btn_2 = Button(window, text="2").grid(row=4,column=2)
btn_1 = Button(window, text="1").grid(row=4,column=3)
btn_add = Button(window, text="+").grid(row=4,column=4)
## Ligne 5
btn_0 = Button(window, text="0").grid(row=5,column=1)
btn_point = Button(window, text=".").grid(row=5,column=2)
btn_equal = Button(window, text="=").grid(row=5,column=3)

# Lancement de la boucle du script
window.mainloop()