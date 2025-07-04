import sqlite3




class Database:
    def __init__(self,db):
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
    
    def execute_script(self,script):
        self.cursor.execute(script)
        self.conn.commit()
    def close_script(self):
        self.cursor.close()
        self.conn.close()




class Sqlscripts():
    def __init__(self,table_name,dictionary):
        self.table_name = table_name
        self.dictionary = dictionary
    def save_personal(self):
        key_list = [key for key in self.dictionary.keys()]
        values_list = [self._escape_sql_value(v) for v in self.dictionary.values()] 
        
        columns = ', '.join(key_list)
        values = ', '.join(values_list)
        
        return f"""
        INSERT INTO {self.table_name} ({columns}) 
        VALUES ({values})
        """


    def _escape_sql_value(self, value):
        if value is None:
            return 'NULL'
        elif isinstance(value, str):
            escaped_value = value.replace("'", "''")
            return f"'{escaped_value}'"
        elif isinstance(value, (int, float)):
            return str(value)
        elif isinstance(value, bool):
            return '1' if value else '0'
        elif isinstance(value, list):
            import json
            json_str = json.dumps(value)
            escaped_json = json_str.replace("'", "''")
            return f"'{escaped_json}'"
        else:
            return 'NULL'