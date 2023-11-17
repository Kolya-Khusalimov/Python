import sqlite3
import docx

from bin.instalment import Instalment
from widgets import *


MOVE_IN_TRANSACTION = 'Приймання'
MOVE_OUT_TRANSACTION = 'Відпуск'
DESTROY_TRANSACTION = 'Списання'


class App(tk.Tk):
    def __init__(self, conn):
        super().__init__()

        self.title("Товари")

        self.conn = conn
        self.selection = None

        self.list = StorageList(self, height=15)
        self.category = tk.Label(self, text="Категорія")
        self.categoryEntry = tk.Entry(self, width=25)
        self.name = tk.Label(self, text="Назва")
        self.nameEntry = tk.Entry(self, width=25)
        self.form = InstalmentForm(self)
        self.btn_move_in = tk.Button(self, text="Отримати партію",
                                 command=self.move_in)
        self.btn_search = tk.Button(self, text="Пошук",
                                    command=self.search, width=25)

        self.instalments: list[Instalment] = []
        self.search()
        
        self.category.pack(side=tk.TOP, padx=5, pady=5)
        self.categoryEntry.pack(side=tk.TOP, padx=5, pady=5)
        self.name.pack(side=tk.TOP, padx=5, pady=5)
        self.nameEntry.pack(side=tk.TOP, padx=5, pady=5)
        self.btn_search.pack(side=tk.TOP, padx=5, pady=5)
        self.list.pack(side=tk.LEFT, padx=10, pady=10)

        self.form.pack(padx=10, pady=10)
        # self.btn_new.pack(side=tk.LEFT,padx=5, pady=5)
        self.btn_move_in.pack(side=tk.LEFT, padx=5, pady=5)

        self.list.bind_double_click(self.retrieve)
        self.form.bind_move_out(self.move_out)
        self.form.bind_delete(self.delete)

    def search(self):
        self.list.lb.delete(0, len(self.instalments))
        name = self.nameEntry.get()
        category = self.categoryEntry.get()
        self.instalments = Instalment.list(self.conn, name=name, category=category)
        self.list.insert(self.instalments)

    def create(self):
        interface = NewGood(self)
        good: Good = interface.get_data()
        if not good:
            return
        good.create(self.conn)
    
    def retrieve(self, index):
        self.selection = index
        instalment: Instalment = self.instalments[index]
        self.form.load_data(instalment)

    def move_in(self):
        interface = MoveIn(self)
        good: Good
        instalment: Instalment
        invoice: Invoice
        good, instalment, invoice = interface.get_data()
        if not good or not instalment or not invoice:
            return
        try:
            good.create(self.conn)
        except Exception:
            pass

        instalment.good = good.name
        instalment.create(self.conn)
        invoice.operation = MOVE_IN_TRANSACTION
        invoice.instalment = instalment.id
        invoice.create(self.conn)
        invoice.print(docx, instalment)
        self.instalments.append(instalment)
        self.list.insert([instalment])

    def move_out(self):
        if self.selection == None:
            return
        interface = MoveOut(self)
        invoice: Invoice = interface.get_data()
        if not invoice:
            return
        instalment: Instalment = self.instalments[self.selection]
        invoice.operation = MOVE_OUT_TRANSACTION
        invoice.instalment = instalment.id
        instalment.delete(self.conn)
        invoice.create(self.conn)
        invoice.print(docx, instalment)
        self.form.clear()
        self.list.delete(self.selection)
        self.selection = None

    def delete(self):
        if self.selection == None:
            return
        instalment: Instalment = self.instalments[self.selection]
        invoice = Invoice(
            operation=DESTROY_TRANSACTION,
            instalment=instalment.id)
        instalment.delete(self.conn)
        invoice.create(self.conn)
        invoice.print(docx, instalment)
        self.form.clear()
        self.list.delete(self.selection)
        self.selection = None


def main():
    with sqlite3.connect("db.sqlite3") as conn:
        app = App(conn)
        app.mainloop()


if __name__ == "__main__":
    main()
