from tkinter import Tk,CENTER
from tkinter.filedialog import askopenfilename as ask
import customtkinter as ct
import convert_sped_panilha as csp
from os import getcwd

arquivo=''

def formatar(arq):
	for i in range(0,int(len(arq)/25)):
		arq=arq[i:25*(i+1)]+'\n'+arq[25*(i+1):]
	return arq

def selecionar() :
	global arquivo
	file = ask()
	arquivo = file
	arq=formatar(arquivo)
	lab1.configure(text='Selecionado : \n'+arq)

def gerar():
	global arquivo
	novo = str(inputtxt.get())
	novo = getcwd()+'\\'+novo
	arq = csp.main(arquivo,novo )
	arq = formatar(arq)
	lab2.configure(text =' Resultado : \n'+arq)
	
root = ct.CTk()	
root.title('SPED->TABLE')
root.geometry("300x400")

ct.set_appearance_mode('dark')
ct.set_default_color_theme('blue')

lab1=  ct.CTkLabel(master=root, text='')
lab1.place(relx=0.5,rely=0.2,anchor=CENTER)

button =  ct.CTkButton(master=root, text='Selecionar arquivo',command=selecionar)
button.place(relx=0.5,rely=0.4,anchor='n')

button =  ct.CTkButton(master=root, text='Gerar Planilha Sped',command=gerar)
button.place(relx=0.5,rely=0.5,anchor='n')

inputtxt = ct.CTkEntry(root,placeholder_text='sped',    height = 10,width = 80)
inputtxt.place(relx=0.5,rely=0.6,anchor='n')

lab2=  ct.CTkLabel(master=root, text='')
lab2.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()

