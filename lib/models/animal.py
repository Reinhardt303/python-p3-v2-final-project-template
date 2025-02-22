from models.__init__ import CURSOR, CONN
from models.habitat import Habitat

class Animal:

    all = {}

    def __init__(self, name, color, predator, habitat_id, id=None):
        self.name = name
        self.color = color
        self.predator = predator
        self.habitat_id = habitat_id
        self.id = id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 1:
            self._name = name
        else:
            raise Exception('Invalid name')
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if isinstance(color, str) and len(color) > 2:
            self._color = color
        else:
            raise Exception('Invalid color')
        
    @property
    def predator(self):
        return self._predator
    
    @predator.setter
    def predator(self, predator):
        if isinstance(predator, bool):
            self._predator = predator
        else:
            raise Exception('Must be boolean value')
        
    @property
    def habitat_id(self):
        return self._habitat_id
    
    @habitat_id.setter
    def habitat_id(self, habitat_id):
        if type(habitat_id) is int and Habitat.find_by_id(habitat_id): # consider removing if statement
            self._habitat_id = habitat_id
        else:
            raise Exception('Habitat ID must referance a habitat in the database')
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS animals (
            id INTEGER PRIMARY KEY,
            name TEXT,
            color TEXT,
            predator BOOLEAN,
            habitat_id INTEGER,
            FOREIGN KEY (habitat_id) REFERENCES habitats(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS animals;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO animals (name, color, predator, habitat_id)
                VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.color, self.predator, self.habitat_id))
        CONN.commit()

        self.id = CURSOR.lastrowid

    def update(self):
        sql = """
            UPDATE animals
            SET name = ?, color = ?, predator = ?, habitat_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.color, self.predator, self.habitat_id, self.id))
        CONN.commit()

    def delete(self):

        sql = """
            DELETE FROM animals
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, color, predator, habitat_id):
        animal = cls(name, color, predator, habitat_id)
        animal.save()
        return animal
    
    @classmethod
    def instance_from_db(cls, row):
        animal = cls.all.get(row[0])
        if animal:
            animal.name = row[1]
            animal.color = row[2]
            animal.predator = bool(row[3])
            animal.habitat_id = row[4]
        else:
            animal = cls(row[1], row[2], bool(row[3]), row[4])
            animal.id = row[0]
            cls.all[animal.id] = animal
        return animal
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM animals
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM animals
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM animals
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_color(cls, color):
        sql = """
            SELECT *
            FROM animals
            WHERE color is ?
        """

        row = CURSOR.execute(sql, (color,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_predator(cls, predator):
        sql = """
            SELECT *
            FROM animals
            WHERE predator is ?
        """

        row = CURSOR.execute(sql, (predator,)).fetchone()
        return cls.instance_from_db(row) if row else None