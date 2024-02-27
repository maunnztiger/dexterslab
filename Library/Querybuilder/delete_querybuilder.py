class DeleteQueryBuilder:
    def __init__(self, table_name):
        self.table_name = table_name
        self.conditions = []

    def where(self, condition):
        self.conditions.append(condition)
        return self

    def build(self):
        if not self.conditions:
            raise ValueError("No conditions specified for delete query")

        query = f"DELETE FROM {self.table_name}"

        if self.conditions:
            query += " WHERE " + " AND ".join(self.conditions)

        return query
