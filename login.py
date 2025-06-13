from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser 


co0 = "#000000"
co1 = "#FFFFFF"
co2 = "#FFFFFF"
co3 = "#8A4040"
co4 = "#000000"
co5 = "#000000"


caminho_fundo = r"C:\login\c5e6a4cdeec2ef36e7690f3278ac41a8.jpg"


janela = Tk()
janela.title("Duduferoz")
janela.geometry("310x350")  
janela.configure(bg=co1)
janela.resizable(False, False)


imagem_fundo_pil = Image.open(caminho_fundo).resize((600, 1000))
imagem_fundo = ImageTk.PhotoImage(imagem_fundo_pil)  


frame_cima = Frame(janela, width=310, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=300, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


label_fundo = Label(frame_baixo, image=imagem_fundo)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)


l_nome = Label(frame_cima, text="LOGIN XBOX", height=1, anchor=NE, font=('Ivy', 25), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, width=275, text="", height=1, anchor=NW, font=('Ivy', 1), bg=co5)
l_linha.place(x=10, y=45)

credenciais = ['davi', 'xbox']

def verificar_senha():
    nome = e_nome.get()
    senha = str(e_pass.get())

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin ao xbox!')
        nova_janela(nome)
        webbrowser.open("https://www.xbox.com")  

    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta '+credenciais[0])

        for widget in frame_baixo.winfo_children():
            widget.destroy()

        for widget in frame_cima.winfo_children():
            widget.destroy()

        nova_janela(nome)
        webbrowser.open("https://www.xbox.com")  

    else:
        messagebox.showwarning('Error', 'Verifique o nome de usuario ou a palavra passe')

def nova_janela(usuario):
    l_nome = Label(frame_cima, text="Usuario: " + usuario, height=1, anchor=NE, font=('Ivy', 20), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, width=275, text="", height=1, anchor=NW, font=("Ivy", 1), bg=co2)
    l_linha.place(x=10, y=45)

    l_nome = Label(frame_baixo, text="Seja bem vindo ao xbox" + usuario, height=1, anchor=NE, font=('Ivy', 20), bg=co1, fg=co4)
    l_nome.place(x=5, y=105)


l_nome = Label(frame_baixo, text="Nome *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_nome.place(x=14, y=50)

l_pass = Label(frame_baixo, text="pass *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_pass.place(x=10, y=90)
e_pass = Entry(frame_baixo, show='*', width=25, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_pass.place(x=14, y=120)

botao_confirmar = Button(frame_baixo, text="Entra", width=39, height=2, bg=co2, fg=co5, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=verificar_senha)
botao_confirmar.place(x=15, y=180)


janela.imagem_fundo = imagem_fundo

janela.mainloop()
