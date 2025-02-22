CREATE TABLE animals (
    id INTEGER PRIMARY KEY,
    name TEXT,
    color TEXT,
    predator BOOLEAN
    habitat_id INTEGER
    FOREIGN KEY (habitat_id) REFERENCES habitats(id)
)

CREATE TABLE habitats (
    id INTEGER PRIMARY KEY,
    name TEXT,
)