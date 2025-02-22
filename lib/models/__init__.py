import sqlite3

CONN = sqlite3.connect('AnimalsByHabitat.db')
CURSOR = CONN.cursor()
