from sqlmodel import create_engine


class Connections():
    def __init__(self) -> None:
        self.engine = ''
        self.db = ''
    
    def localMysql(self, schema):
        self.db = f"mysql+pymysql://web:#Colim42024@192.168.1.10/{schema}"
        self.engine = create_engine(self.db, echo=True)
    def localSQLServer(self, schema):
        self.db = f"mssql+pyodbc://web:#Colim42024@DESKTOP-OB0SKR8/{schema}?driver=ODBC+Driver+17+for+SQL+Server"
        self.engine = create_engine(self.db, echo=True)
