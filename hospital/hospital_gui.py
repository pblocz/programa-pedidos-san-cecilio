
'''
programa_pedidos_san_cecilio v1.0 | (c) 2014 Pablo Cabeza
license: modified BSD
'''
from Tkinter import *
from ttk import *

import sys
import os

from .lista_compra_frame import ListaCompraFrame
from .programa_pedidos_frame import PedidosPendientesFrame
from .hospital_gui_common import *

from pkgutil import get_data
from PIL import Image as PILImage, ImageTk
from StringIO import StringIO


def main():

    # define root window and its properties
    v = Tk()
    v.title("Programa de cruces")
    v.resizable(0, 0)

    icon = PILImage.open(StringIO(get_data("hospital", "data/icon.ico")))
    icontk = ImageTk.PhotoImage(icon)
    v.tk.call("wm", "iconphoto", v._w, icontk)

    # logging text area
    logframe = Frame(v, bd=1, relief=GROOVE)

    logtext = ReadOnlyText(logframe, height=10, width=10, bd=0)
    logtext.pack(side=TOP, fill=BOTH, expand=1)

    def logging(*args, **kwargs):
        textwidgetlog(*args, text=logtext, **kwargs)

    # create notebook widget
    note = Notebook(v)

    # Create and add both frames
    listacompratab = ListaCompraFrame(note, log=logging)
    pedidospendtab = PedidosPendientesFrame(note, log=logging)

    note.add(listacompratab, text="Lista de compra", sticky="E")
    note.add(pedidospendtab, text="Pedidos pendientes", sticky="E")

    note.grid(row=0, padx=8, pady=(8, 0), sticky="WE")  # the the notebook widget

    print listacompratab.winfo_reqwidth(),
    logframe.grid(row=1, padx=8, pady=(0, 8), sticky="WE")


    # Actual loop and center widgets
    centrar(v)
    v.mainloop()


if __name__ == '__main__': main()
