from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

class QueryBuilder:
    def __init__(self, table_name):
        self.table_name = table_name
        self.columns = []
        self.values = []
        self.set_statements = []
        self.where_conditions = []
        self.order_by_columns = []
        self.limit_value = None

    # CREATE Operation
    def insert(self, **kwargs):
        self.columns = list(kwargs.keys())
        self.values = [f":{key}" for key in kwargs.keys()]
        self.data = kwargs
        return self

    # READ Operation
    def select(self, *columns):
        self.columns = columns if columns else ["*"]
        return self

    def where(self, **kwargs):
        for column, value in kwargs.items():
            self.where_conditions.append(f"{column} = :{column}")
            self.data[column] = value
        return self

    def order_by(self, *columns):
        self.order_by_columns = columns
        return self

    def limit(self, value):
        self.limit_value = value
        return self

    # UPDATE Operation
    def update(self, **kwargs):
        for column, value in kwargs.items():
            self.set_statements.append(f"{column} = :{column}")
            self.data[column] = value
        return self

    # DELETE Operation
    def delete(self):
        return self

    # Build Query
    def build(self):
        if self.set_statements:  # Update Query
            set_str = ", ".join(self.set_statements)
            where_str = " AND ".join(self.where_conditions) if self.where_conditions else "1=1"
            query = f"UPDATE {self.table_name} SET {set_str} WHERE {where_str}"

        elif self.columns and self.values:  # Insert Query
            columns_str = ", ".join(self.columns)
            values_str = ", ".join(self.values)
            query = f"INSERT INTO {self.table_name} ({columns_str}) VALUES ({values_str})"

        elif self.where_conditions:  # Delete Query
            where_str = " AND ".join(self.where_conditions)
            query = f"DELETE FROM {self.table_name} WHERE {where_str}"

        else:  # Select Query
            columns_str = ", ".join(self.columns)
            query = f"SELECT {columns_str} FROM {self.table_name}"
            if self.where_conditions:
                where_str = " AND ".join(self.where_conditions)
                query += f" WHERE {where_str}"
            if self.order_by_columns:
                order_by_str = ", ".join(self.order_by_columns)
                query += f" ORDER BY {order_by_str}"
            if self.limit_value is not None:
                query += f" LIMIT {self.limit_value}"

        return query

    # Execute Query
    def execute(self, session, **params):
        query = self.build()
        print("Executing Query:", query)  # Debug Output
        result = session.execute(text(query), params)
        session.commit()
        return result.fetchall() if "SELECT" in query else result.rowcount


# Datenbank-Verbindung
def connect_to_database():
    engine = create_engine("sqlite:///example.db")  # SQLite-Datenbank
    Session = sessionmaker(bind=engine)
    return Session()

# Beispiel für die Nutzung des Query Builders
if __name__ == "__main__":
    session = connect_to_database()
    query_builder = QueryBuilder("users")

    # CREATE - Insert Beispiel
    query_builder.insert(id=1, name="Alice", age=30).execute(session)

    # READ - Select Beispiel
    users = query_builder.select("id", "name").where(age=30).order_by("name").execute(session)
    print(users)

    # UPDATE - Update Beispiel
    query_builder.update(name="Bob").where(id=1).execute(session)

    # DELETE - Delete Beispiel
    query_builder.delete().where(id=1).execute(session)
