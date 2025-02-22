from models.__init__ import CURSOR, CONN


class Habitat:

    all = {}

    def __init__(self, name, id=None):
        self.name = name
        self.id = id
        #Habitat.all.append(self)

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self,name):
        if isinstance(name, str) and len(name) > 2:
            self._name = name
        else:
            raise Exception('Invalid name')
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS habitats (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS habitats;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO habitats (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    

    @classmethod
    def create(cls, name):
        habitat = cls(name)
        habitat.save()
        return habitat
    
    def update(self):
        sql = """
            UPDATE habitats
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM habitats
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
        
    @classmethod
    def instance_from_db(cls, row):
        habitat = cls.all.get(row[0])
        if habitat:
            habitat.name = row[1]
        else:
            habitat = cls(row[1])
            habitat.id = row[0]
            cls.all[habitat.id] = habitat
        return habitat

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM habitats
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM habitats
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM habitats
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def animals(self):
        from models.animal import Animal
        sql = """
            SELECT * FROM animals
            WHERE habitat_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Animal.instance_from_db(row) for row in rows
        ]