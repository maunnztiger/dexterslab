class UpdateQueryBuilder:
    def __init__(self, table_name):
        self.table_name = table_name
        self.set_values = {}
        self.conditions = []

    def set(self, **kwargs):
        self.set_values.update(kwargs)
        return self

    def where(self, condition):
        self.conditions.append(condition)
        return self

    def build(self):
        if not self.set_values:
            raise ValueError("No columns to update")

        query = f"UPDATE {self.table_name} SET "

        set_clauses = [f"{column} = '{value}'" for column, value in self.set_values.items()]
        query += ", ".join(set_clauses)

        if self.conditions:
            query += " WHERE " + " AND ".join(self.conditions)

        return query
