class QueryBuilder:
    def __init__(self, table_name):
        self.table_name = table_name
        self.columns = []
        self.conditions = []
        self.order_by = None

    def select(self, *columns):
        self.columns.extend(columns)
        return self

    def where(self, condition):
        self.conditions.append(condition)
        return self

    def order_by_column(self, column, ascending=True):
        self.order_by = (column, ascending)
        return self

    def build(self):
        query = "SELECT "

        if not self.columns:
            query += "*"
        else:
            query += ", ".join(self.columns)

        query += f" FROM {self.table_name}"

        if self.conditions:
            query += " WHERE " + " AND ".join(self.conditions)

        if self.order_by:
            column, ascending = self.order_by
            query += f" ORDER BY {column} {'ASC' if ascending else 'DESC'}"

        return query


