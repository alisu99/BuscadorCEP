import json.decoder
from tkinter import *
from tkinter import messagebox
from requests import get


def limpar():
    texto_logradouro['text'] = ''
    texto_bairro['text'] = ''
    texto_cidade['text'] = ''
    texto_estado['text'] = ''
    texto_complemento['text'] = ''
    texto_ddd['text'] = ''
    input_cep.delete(first=0, last=len(input_cep.get()))


def get_cep():
    try:
        if input_cep.get() == 'criador':
            messagebox.showinfo('Olá!', '''Me chamo Alisson e esse é meu primeiro projeto! 
É construído totalmente com Python e estou sempre em  busca de melhorá-lo, obrigado!''')

        else:
            url = get(f'http://viacep.com.br/ws/{input_cep.get()}/json/'.lower())
            resultado = url.json()
            texto_logradouro['text'] = resultado['logradouro']
            texto_bairro['text'] = resultado['bairro']
            texto_cidade['text'] = resultado['localidade']
            texto_estado['text'] = resultado['uf']
            texto_complemento['text'] = resultado['complemento'] if len(resultado['complemento']) > 0 else '--'
            texto_ddd['text'] = resultado['ddd']

    except json.decoder.JSONDecodeError:
        messagebox.showerror('Erro!', f'CEP "{input_cep.get()}" não encontrado!')
        input_cep.delete(first=0, last=len(input_cep.get()))

    except KeyError:
        messagebox.showerror('Erro!', f'CEP "{input_cep.get()}" não encontrado!')
        input_cep.delete(first=0, last=len(input_cep.get()))


# criação e configuração da janela
janela = Tk()
janela.config(bg='#87888c')
janela.title('Consulta CEP')
janela.geometry('486x280')
janela.resizable(width=False, height=False)
janela.iconphoto(False, PhotoImage(file='lupa.png'))

# -------------------------------

# input para digitar o cep e botão de buscar
cep = Label(janela, text='CEP', width=5, height=0, font='Calibre 10', fg='black', borderwidth=2)
cep.place(x=123, y=12)

input_cep = Entry(janela, width=15, font='Calibre', borderwidth=2)
input_cep.place(x=170, y=10)
botao_cep = Button(janela, command=get_cep, width=10, height=0, font='Calibre 8', text='Buscar', borderwidth=1,
                   relief=GROOVE)
botao_cep.place(x=311, y=11)

# rótulos onde irão aparecer as informações do cep digitado
label_logradouro = Label(janela, text='Endereço/Logradouro', font='Calibre 10')
label_logradouro.place(x=15, y=70)
texto_logradouro = Label(janela, width=24, height=1, text='', font='Calibre', bg='white')
texto_logradouro.place(x=15, y=95)

label_bairro = Label(janela, text='Bairro', font='Calibre 10')
label_bairro.place(x=15, y=125)
texto_bairro = Label(janela, width=24, height=1, text='', font='Calibre', bg='white')
texto_bairro.place(x=15, y=150)

# ---------------------------------

label_complemento = Label(janela, text='Complemento', font='Calibre 10')
label_complemento.place(x=250, y=70)
texto_complemento = Label(janela, width=24, height=1, text='', font='Calibre', bg='white')
texto_complemento.place(x=250, y=95)

label_cidade = Label(janela, text='Cidade', font='Calibre 10')
label_cidade.place(x=250, y=125)
texto_cidade = Label(janela, width=24, height=1, text='', font='Calibre', bg='white')
texto_cidade.place(x=250, y=150)

# ---------------------------------

label_estado = Label(janela, text='Estado', font='Calibre 10')
label_estado.place(x=15, y=180)
texto_estado = Label(janela, width=24, height=1, text='', font='Calibre', bg='white')
texto_estado.place(x=15, y=205)

label_ddd = Label(janela, text='DDD', font='Calibre 10')
label_ddd.place(x=250, y=180)
texto_ddd = Label(janela, width=24, height=1, text='', font='Calibre', bg='white')
texto_ddd.place(x=250, y=205)


# Botão de limpar
botao_limpar = Button(janela, command=limpar, width=10, height=0, font='Calibre 8', text='Limpar', borderwidth=1,
                      relief=GROOVE)
botao_limpar.place(x=404, y=240)

# ---------------------------------

janela.mainloop()
