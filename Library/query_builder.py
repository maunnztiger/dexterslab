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
        self.set_values = {}
        self.conditions = []
        self.limit_value = None
        self.kind_of_query= ""

    # READ Operation
    def select(self, *columns):
        self.kind_of_query = 'SELECT'
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

    def insert(self, **kwargs):
        self.kind_of_query = 'INSERT'
        for column, value in kwargs.items():
            self.columns.append(column)
            # Hier verwenden wir den Parameter :value anstelle von {value}
            self.values.append(f"{value}")
        return self
    
    def set(self, **kwargs):
        self.kind_of_query = 'UPDATE'
        self.set_values.update(kwargs)
        return self
    
    def set_where(self, condition):
        self.conditions.append(condition)
        return self
    
    def delete_where(self, condition):
        self.conditions.append(condition)
        return self
    
    # Build Query
    def build(self):
        if self.kind_of_query == 'SELECT':
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
        elif self.kind_of_query == 'INSERT':
            if not self.columns or not self.values:
                raise ValueError("No columns or values to insert")

            columns_str = ", ".join(self.columns)
            values_str = ", ".join(self.values)

            query = f"INSERT INTO {self.table_name} ({columns_str}) VALUES ({values_str})"
        elif self.kind_of_query == 'UPDATE':
            if not self.set_values:
                raise ValueError("No columns to update")

            query = f"UPDATE {self.table_name} SET "

            set_clauses = [f"{column} = '{value}'" for column, value in self.set_values.items()]
            query += ", ".join(set_clauses)

            if self.conditions:
                query += " WHERE " + " AND ".join(self.conditions)
        else:
            if not self.conditions:
                raise ValueError("No conditions specified for delete query")

            query = f"DELETE FROM {self.table_name}"

            if self.conditions:
                query += " WHERE " + " AND ".join(self.conditions)
        return query

    # Execute Query
    def execute(self, session, **params):
        query = self.build()
        print("Executing Query:", query)  # Debug Output
        result = session.execute(text(query), params)
        session.commit()
        return result.fetchall() if "SELECT" in query else result.rowcount

