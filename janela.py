# coding: utf-8

import tkinter as tk
from os import system


class Janela(object):
    u"""Implementaçao da janela principal."""

    def __init__(self, janela):
        """Construtor da Classe."""
        self.janela = janela
        self.fonte = ("Capture it", 12)
        self.janela.configure(bg="black")

        self.username_frame = tk.Frame(self.janela, bd=10)
        self.username_label = tk.Label(self.username_frame,
                                       text="Nome de Usuário:", width=15)
        self.username_entry = tk.Entry(self.username_frame, justify=tk.CENTER)
        self.username_frame.configure(bg="black")
        self.username_label.configure(bg="black", fg="white", font=self.fonte)
        # self.username_entry.configure(bg="black", fg="white")
        self.username_frame.pack()
        self.username_label.pack(side=tk.TOP)
        self.username_entry.pack(side=tk.BOTTOM)

        self.password_frame = tk.Frame(self.janela, bd=10)
        self.password_label = tk.Label(self.password_frame,
                                       text="Senha:", width=15)
        self.password_entry = tk.Entry(self.password_frame,
                                       show='*', justify=tk.CENTER)
        self.password_frame.configure(bg="black")
        self.password_label.configure(bg="black", fg="white", font=self.fonte)
        # self.password_entry.configure(bg="black", fg="white")
        self.password_frame.pack()
        self.password_label.pack(side=tk.TOP)
        self.password_entry.pack(side=tk.BOTTOM)

        self.link_frame = tk.Frame(self.janela, bd=10)
        self.link_label = tk.Label(self.link_frame, text="Link do Curso:",
                                   width=15, font=self.fonte)
        self.link_entry = tk.Entry(self.link_frame, justify=tk.CENTER)
        self.link_frame.configure(bg="black")
        self.link_label.configure(bg="black", fg="white")
        # self.link_entry.configure(bg="black", fg="white")
        self.link_frame.pack()
        self.link_label.pack(side=tk.TOP)
        self.link_entry.pack(side=tk.BOTTOM)

        self.buttom_frame = tk.Frame(self.janela, bd=10, bg="black")
        self.download = tk.Button(self.buttom_frame, text="Baixar",
                                  command=self.baixar)
        self.download.configure(bg="black", fg="white", font=self.fonte)
        self.buttom_frame.pack()
        self.download.pack(side=tk.BOTTOM)

    def baixar(self):
        u"""Realiza a operação de Download."""
        print("Baixando...")
        system("youtube-dl -u {0} -p {1} {2}".format(self.username_entry.get(),
                                                     self.password_entry.get(),
                                                     self.link_entry.get()))
        print("Download completo.")
