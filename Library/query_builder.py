from sqlalchemy import text

class QueryBuilder:
    def __init__(self, table_name):
        self.table_name = table_name
        self.columns = []
        self.values = []
        self.set_values = {}
        self.where_conditions = []
        self.order_by_columns = []
        self.limit_value = None
        self.kind_of_query = ""
        self.data = {}  # Parameter-Werte für sichere Bindung

    # --- SELECT ---
    def select(self, *columns):
        self.kind_of_query = 'SELECT'
        self.columns = columns if columns else ["*"]
        return self

    # --- WHERE ---
    def where(self, **kwargs):
        for column, value in kwargs.items():
            self.where_conditions.append(f"{column} = :{column}")
            self.data[column] = value
        return self

    # --- ORDER BY ---
    def order_by(self, *columns):
        self.order_by_columns = columns
        return self

    # --- LIMIT ---
    def limit(self, value):
        self.limit_value = value
        return self

    # --- INSERT ---
    def insert(self, **kwargs):
        self.kind_of_query = 'INSERT'
        for column, value in kwargs.items():
            self.columns.append(column)
            self.data[column] = value
        return self

    # --- UPDATE ---
    def set(self, **kwargs):
        self.kind_of_query = 'UPDATE'
        self.set_values.update(kwargs)
        for column, value in kwargs.items():
            self.data[column] = value
        return self

    def set_where(self, **kwargs):
        for column, value in kwargs.items():
            self.where_conditions.append(f"{column} = :{column}")
            self.data[column] = value
        return self

    # --- DELETE ---
    def delete_where(self, **conditions):
        clause = " AND ".join([f"{k} = '{v}'" for k, v in conditions.items()])
        self._query = f"DELETE FROM {self.table_name} WHERE {clause}"
        return self

    # --- Build SQL ---
    def build(self):
        if self.kind_of_query == 'SELECT':
            cols = ", ".join(self.columns)
            query = f"SELECT {cols} FROM {self.table_name}"
        elif self.kind_of_query == 'INSERT':
            cols = ", ".join(self.columns)
            vals = ", ".join([f":{c}" for c in self.columns])
            query = f"INSERT INTO {self.table_name} ({cols}) VALUES ({vals})"
        elif self.kind_of_query == 'UPDATE':
            sets = ", ".join([f"{c} = :{c}" for c in self.set_values.keys()])
            query = f"UPDATE {self.table_name} SET {sets}"
        elif self.kind_of_query == 'DELETE FROM':
            query = f"DELETE FROM {self.table_name}"
        else:
            raise ValueError("Unknown query type")

        if self.where_conditions:
            where_str = " AND ".join(self.where_conditions)
            query += f" WHERE {where_str}"
        if self.order_by_columns:
            query += " ORDER BY " + ", ".join(self.order_by_columns)
        if self.limit_value is not None:
            query += f" LIMIT {self.limit_value}"

        return query

    # --- Execute ---
    def execute(self, session):
        query = self.build()
        print("Executing Query:", query)
        print("With Parameters:", self.data)
        result = session.execute(text(query), self.data)
        session.commit()
        if self.kind_of_query == "SELECT":
            rows = result.fetchall()
            return [row._asdict() for row in rows]
        else:
            return {"affected_rows": result.rowcount}
