import tkinter as tk

from bin.instalment import Instalment
from bin.good import Good
from bin.invoice import Invoice


class StorageList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)

        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insert(self, instalments, index=tk.END):
        elements = [
            f"{instalment.id}.) {instalment.good.name}, {instalment.count} {instalment.good.unit}" 
            for instalment in instalments
        ]
        self.lb.insert(index, *elements)

    def delete(self, index):
        self.lb.delete(index, index)

    def update(self, instalments, index):
        self.delete(index)
        self.insert(instalments, index)

    def bind_double_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)


class Form(tk.LabelFrame):
    title: str
    disabled: bool = False
    model: type
    fields: list | tuple

    def __init__(self, master, **kwargs):
        super().__init__(master, text=self.title, padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.create_field, enumerate(self.fields)))
        self.frame.pack()

    def create_field(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25, state='readonly' if self.disabled else 'normal')
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry
    
    def load_data(self, obj):
        values = obj.serialize()
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def get_data(self):
        values = [e.get() for e in self.entries]
        return self.model.deserialize_new(values)
    
    def clear(self):
        for entry in self.entries:
            entry.delete(0, tk.END)


class NewGoodForm(Form):
    title = "Товар"
    model = Good
    fields = ("Назва", "Категорія", "Од. вим.")


class NewInstalmentForm(Form):
    title = "Партія"
    model = Instalment
    fields = ("Кількість", "Склад", "Відділ", "Полиця")


class InstalmentForm(NewInstalmentForm):
    fields = ("Назва Товару", "Категорія", "Од. вим.", "Кількість", "Склад", "Відділ", "Полиця")

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btn_move_out = tk.Button(self, text="Відпустити")
        self.btn_delete = tk.Button(self, text="Списати")
        self.btn_move_out.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)

    def bind_move_out(self, callback):
        self.btn_move_out.config(command=callback)

    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)


class InvoiceForm(Form):
    title = "Накладна"
    model = Invoice
    fields = ("Відправник", "Отримувач")


class CreateWindow(tk.Toplevel):
    form_class: type

    def __init__(self, parent):
        super().__init__(parent)
        self.obj = None
        self.form: Form = self.form_class(self)
        self.btn_add = tk.Button(self, text="Підтвердити", command=self.confirm)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirm(self):
        self.obj = self.form.get_data()
        if self.obj:
            self.destroy()

    def get_data(self):
        self.grab_set()
        self.wait_window()
        return self.obj


class NewGood(CreateWindow):
    form_class = NewGoodForm


class NewInstalment(CreateWindow):
    form_class = NewInstalmentForm


class MoveOut(CreateWindow):
    form_class = InvoiceForm


class MoveIn(tk.Toplevel):
    form_class: type

    def __init__(self, parent):
        super().__init__(parent)
        self.good: Good = None
        self.instalment: Instalment = None
        self.invoice: Invoice = None

        self.good_form = NewGoodForm(self)
        self.instalment_form = NewInstalmentForm(self)
        self.invoice_form = InvoiceForm(self)
        self.btn_add = tk.Button(self, text="Підтвердити", command=self.confirm)

        self.good_form.pack(padx=10, pady=10)
        self.instalment_form.pack(padx=10, pady=10)
        self.invoice_form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirm(self):
        self.good = self.good_form.get_data()
        self.instalment = self.instalment_form.get_data()
        self.invoice = self.invoice_form.get_data()

        if self.good and self.instalment and self.invoice:
            self.destroy()

    def get_data(self):
        self.grab_set()
        self.wait_window()
        return (self.good, self.instalment, self.invoice)
