class InsertQueryBuilder:
    def __init__(self, table_name):
        self.table_name = table_name
        self.columns = []
        self.values = []

    def insert(self, **kwargs):
        for column, value in kwargs.items():
            self.columns.append(column)
            self.values.append(value)
        return self

    def build(self):
        if not self.columns or not self.values:
            raise ValueError("No columns or values to insert")

        columns_str = ", ".join(self.columns)
        values_placeholder = ", ".join([f":{column}" for column in self.columns])

        query = f"INSERT INTO {self.table_name} ({columns_str}) VALUES ({values_placeholder})"
        return query
