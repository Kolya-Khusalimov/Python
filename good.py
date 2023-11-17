class Good:
    def __init__(self, id: int = None,
                 name: str = None, category: str = None, unit: str = None):
        try:
            self.id = id
            self.name = str(name)
            self.category = str(category)
            self.unit = str(unit)

        except:
            raise Exception
        
    @classmethod
    def deserialize(cls, data):
        return cls(
            id=data[0],
            name=data[1],
            category=data[2],
            unit=data[3],
        )
    
    @classmethod
    def deserialize_new(cls, data):
        return cls(
            name=data[0],
            category=data[1],
            unit=data[2],
        )
    
    def serialize(self) -> tuple:
        return (
            self.name,
            self.category,
            self.unit,
        )
    
    @classmethod
    def find(cls, conn, id):
        res = conn.execute("SELECT * FROM goods WHERE id = ?", (id,))
        res = res.fetchone()
        if not res:
            raise Exception
        return cls.deserialize(res)
    
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
        SELECT goods.id, goods.name, categories.name, goods.unit
        FROM goods
        INNER JOIN categories
        ON categories.id = goods.category
        """ + "WHERE " * bool(query) + " AND ".join(query) +  """
        GROUP BY goods.id
        LIMIT 100
        """

        res = cursor.execute(query, query_data)
        
        res = res.fetchall()

        if not res:
            return []

        goods = []

        for item in res:
            goods.append(Good.deserialize(item))

        return goods
    
    def create(self, conn):
        cursor = conn.cursor()

        category_id = self._get_category_id(cursor)

        cursor.execute(
            "INSERT INTO goods (name, category, unit) VALUES (?,?,?)", 
            (self.name, category_id, self.unit))

        conn.commit()

        self.id = cursor.lastrowid

    def _get_category_id(self, cursor) -> int:
        res = cursor.execute(
            "SELECT id FROM categories WHERE name like ?", 
            (f"%{self.category}%",))
        
        res = res.fetchone()

        if not res:
            raise Exception

        return res[0]
