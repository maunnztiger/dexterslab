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

    # Build Query
    def build(self):
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

