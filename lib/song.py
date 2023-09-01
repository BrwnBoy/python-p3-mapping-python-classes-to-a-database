from config import CONN, CURSOR

class Song:
    
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
              id INTEGER PRIMARY KEY,
              name TEXT,
              album TEXT
            )
        """
        
        CUSOR.execute(sql)
        
    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        
        CUSOR.execute(sql, (self.name, self.album))
    pass