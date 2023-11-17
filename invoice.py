from datetime import datetime

INVOICES_DIR = 'Накладні'

class Invoice:
    def __init__(self, id: int = None,
                 operation: str = None, date: str = None,
                 sender: str = "", recipient: str = "",
                 instalment: int = None):
        try:
            self.id = id
            self.operation = operation
            self.date = date if date else datetime.today().strftime('%Y-%m-%d')
            self.sender = sender
            self.recipient = recipient
            self.instalment = instalment
        except:
            raise Exception
    
        
    @property
    def document_number(self):
        return f"Накладна №{self.id}"
        
    @classmethod
    def deserialize(cls, data):
        return cls(
            id=data[0],
            operation=data[1],
            date=data[2],
            instalment=data[3],
            sender=data[4],
            recipient=data[5],
        )
    
    @classmethod
    def deserialize_new(cls, data):
        return cls(
            sender=data[0],
            recipient=data[1],
        )
    
    def serialize(self) -> tuple:
        return (
            self.id,
            self.operation,
            self.date,
            self.sender,
            self.recipient,
            self.instalment,
        )

    def create(self, conn):
        cursor = conn.cursor()

        operation_id = self._get_operation_id(cursor)

        cursor.execute(
            "INSERT INTO invoices (operation, date, instalment, sender, recipient) VALUES (?,?,?,?,?)", 
            (operation_id, self.date, self.instalment, self.sender, self.recipient))

        conn.commit()

        self.id = cursor.lastrowid

    def print(self, docx, instalment):
        document = docx.Document()

        document.add_heading(self.document_number, 0)

        document.add_paragraph(f"Дата: {self.date}")
        document.add_paragraph(f"Процедура: {self.operation}")
        
        table = document.add_table(rows=1, cols=8)

        header = ('№', 'Назва товару', 'Категорія', 'Од. вим.', 'Кількість', 'Будівля', 'Відділ', 'Полиця')
        data = (
            instalment.id,
            instalment.good.name,
            instalment.good.category,
            instalment.good.unit,
            instalment.count,
            instalment.building,
            instalment.section,
            instalment.shelf,
        )
        
        row = table.rows[0].cells
        for i, title in enumerate(header):
            row[i].text = title
        
        row = table.add_row().cells
        for i, value in enumerate(data):
            row[i].text = str(value)

        table.style = 'Table Grid'

        document.add_paragraph("")

        if self.sender:
            document.add_paragraph(f"Відправив: {self.sender}")
        if self.recipient:
            document.add_paragraph(f"Отримав: {self.recipient}")

        document.add_paragraph("\n")
        document.add_paragraph("Підпис: _____________________")
        
        document.save(f"{INVOICES_DIR}/{self.document_number}.docx")

    def _get_operation_id(self, cursor) -> int:
        res = cursor.execute(
            "SELECT id FROM operations WHERE name = ?", (self.operation,))
        
        res = res.fetchone()

        if not res:
            raise Exception

        return res[0]
