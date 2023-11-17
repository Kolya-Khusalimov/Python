from .good import Good

class Instalment:
    def __init__(self, id: int = None,
                 good: int | str | Good = None, count: str | int = None,
                 building: str | int = None, section: str | int = None, shelf: str | int = None,
                 deleted: bool = False):
        try:
            self.id = id
            self.good = good
            self.count = int(count)
            self.building = int(building)
            self.section = int(section)
            self.shelf = int(shelf)
            self._deleted = deleted

        except:
            raise Exception
        
    @classmethod
    def deserialize(cls, data):
        good = Good.deserialize(data[1:6])
        return cls(
            id=data[0],
            good=good,
            count=data[5],
            building=data[6],
            section=data[7],
            shelf=data[8],
            deleted=data[9]
        )
    
    @classmethod
    def deserialize_new(cls, data):
        return cls(
            count=data[0],
            building=data[1],
            section=data[2],
            shelf=data[3],
        )
    
    def serialize(self) -> tuple:
        return (
            self.good.name,
            self.good.category,
            self.good.unit,
            self.count,
            self.building,
            self.section,
            self.shelf,
        )
    
    @staticmethod
    def list(conn, name: str = None, category: str = None) -> list:
        cursor = conn.cursor()

        query = []
        query_data = []

        if name:
            query.append(f"goods.name like ?")
            query_data.append(f"%{name}%")

        if category:
            query.append(f"categories.name like ?")
            query_data.append(f"%{category}%")

        query = """
        SELECT inventory.id, goods.id, goods.name, categories.name, goods.unit, inventory.count, inventory.building, inventory.section, inventory.shelf, inventory.deleted
        FROM goods
        INNER JOIN inventory
        ON inventory.good = goods.id
        INNER JOIN categories
        ON categories.id = goods.category
        """ + "WHERE " * bool(query) + " AND ".join(query) + """
        LIMIT 100
        """

        res = cursor.execute(query, query_data)
        
        res = res.fetchall()

        if not res:
            return []

        goods = []

        for item in res:
            goods.append(Instalment.deserialize(item))

        return goods
    
    def create(self, conn):
        cursor = conn.cursor()

        res = cursor.execute(
            "SELECT id FROM inventory WHERE building = ? AND section = ? AND shelf = ? AND deleted = FALSE",
            (self.building, self.section, self.shelf))
        res = res.fetchone()
        if res:
            raise Exception

        good_id = self._get_good_id(cursor)
        
        cursor.execute(
            "INSERT INTO inventory (good, count, building, section, shelf) VALUES (?,?,?,?,?)",
            (good_id, self.count, self.building, self.section, self.shelf))

        conn.commit()

        self.id = cursor.lastrowid
        self.good = Good.find(conn, good_id)



    def delete(self, conn):
        if not self.id:
            raise Exception
        
        if self._deleted:
            raise Exception
        
        cursor = conn.cursor()
        
        res = cursor.execute("SELECT deleted FROM inventory WHERE id = ?", (self.id,))
        res = res.fetchone()
        if not res:
            raise Exception

        if res[0]: 
            raise Exception
        
        cursor.execute(
            "UPDATE inventory SET deleted = ? WHERE id = ?",
            (True, self.id))

        conn.commit()

        self._deleted = True


    def print(self, docx, save_as:str):
        document = docx.Document()

        document.add_heading(f"Товар №{self.id}", 0)

        document.add_paragraph("-----------------------------------------")

        document.add_paragraph(f"Назва: {self.name}")
        document.add_paragraph(f"Кількість: {self.count}")
        document.add_paragraph(f"Категорія: {self.category}")
        document.add_paragraph(f"Склад: {self.building}")
        document.add_paragraph(f"Відділ: {self.section}")
        document.add_paragraph(f"Полиця: {self.shelf}")
        
        document.add_paragraph("-----------------------------------------")
        
        document.save(save_as)

    def _get_good_id(self, cursor) -> int:
        res = cursor.execute(
            "SELECT id FROM goods WHERE name like ?",
            (f"%{self.good}%",))

        res = res.fetchone()

        if not res:
            raise Exception

        return res[0]
