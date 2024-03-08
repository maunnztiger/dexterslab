import inspect

SQL_COMMAND_SELECT = 'SELECT'
SQL_COMMAND_COUNT = 'COUNT'
SQL_COMMAND_DISTINCT = 'DISTINCT'
SQL_COMMAND_FROM = 'FROM'
SQL_COMMAND_UPDATE = 'UPDATE'
SQL_COMMAND_DELETE = 'DELETE'
SQL_COMMAND_INSERT = 'INSERT INTO'
SQL_COMMAND_VALUES = 'VALUES'
SQL_COMMAND_SET = 'SET'

SQL_CLAUSE_JOIN = 'JOIN'
SQL_CLAUSE_ON = 'ON'
SQL_CLAUSE_INNER = 'INNER'
SQL_CLAUSE_LIMIT = 'LIMIT'

JOIN_LEFT = 'LEFT'
JOIN_RIGHT = 'RIGHT'
JOIN_INNER = 'INNER'

SQL_STATEMENT_WHERE = 'WHERE'
SQL_STATEMENT_AND = 'AND'
SQL_STATEMENT_OR = 'OR'
SQL_STATEMENT_GROUP_BY = 'GROUP BY'
SQL_STATEMENT_ORDER_BY = 'ORDER BY'

OPERATOR_EQUAL = '='
OPERATOR_NOT_EQUAL = '!='
OPERATOR_GT = '>'
OPERATOR_GT_OR_EQUAL = '>='
OPERATOR_LT = '<'
OPERATOR_LT_OR_EQUAL = '<='
OPERATOR_BETWEEN = 'BETWEEN'
OPERATOR_LIKE = 'LIKE'
OPERATOR_IN = 'IN'

class Querybuilder:

    def __init__(self):
        self.table_names = []
        self.table_primary_keys = {}
        self.table_properties = {}
        self.join = []
        self.on = []
        self.insert = None
        self.set = None
        self.update = None
        self.delete = None
        self.query = None
        self.db = None
        self.result = None
        self.from_cache = False

        self.id = None
        self.data = {}
        self.select = None
        self.insert = None
        self.delete = None
        self.count = None
        self.set = {}
        self.operator = None
        self.distinct = False
        self.from_table = None
        self.query = None
        self.where = []
        self.order_by = None
        self.group_by = None
        self.result = None
        self.joins = None
        self.join = []
        self.on = None
        self.limit = None
        self.db = None
        self.stmt = None
        self.spalte = None
        self.value = None
        self.row = []
        self.klass = None

        self.allowed_operators = [
            OPERATOR_EQUAL,
            OPERATOR_NOT_EQUAL,
            OPERATOR_GT,
            OPERATOR_GT_OR_EQUAL,
            OPERATOR_LT,
            OPERATOR_LT_OR_EQUAL,
            OPERATOR_BETWEEN,
            OPERATOR_LIKE,
            OPERATOR_IN
        ]

def backticks(self, value):
        return f"`{value}`"

def formatiereValue(self, value):
        if isinstance(value, (int, float)):
            return value
        return str(value)

def formatiereOperator(self, value):
        return f'({value})'
    
def count(self, spalte=None):
        if not spalte:
            self.count = f'{SQL_COMMAND_COUNT} {self.formatiere_operator("*")}'
        elif isinstance(spalte, str):
            self.count = f'{SQL_COMMAND_COUNT} {self.formatiere_operator(spalte)}'
        return self

def select(self, spalte=None):
        if isinstance(spalte, str):
            if spalte == SQL_COMMAND_COUNT:
                self.count()
                self.select += self.count
            else:
                self.select += spalte
        elif spalte is None:
            spalte += '*'
            self.select += spalte
        elif isinstance(spalte, list):
            spalten = len(spalte)
            count = 1
            for value in spalte:
                if spalten == 1:
                    self.select += self.backticks(value)
                else:
                    if spalten > count:
                        self.select += self.backticks(value) + ','
                    else:
                        self.select += self.backticks(value)
                count += 1
        return self

def table(self):
        klassen_name = self.klass.__name__.lower()
        try:
            if not isinstance(self.table_names, list):
                raise ValueError(f'Querybuilder {klassen_name} has no Table property!')
            else:
                table_name = self.table_names[0]
        except ValueError as e:
            print(e)
        return table_name

def order_by(self, spalte, richtung='DESC'):
        self.order_by = f' {SQL_STATEMENT_ORDER_BY} {self.backticks(spalte)} {richtung}'
        return self

def from_table_(self, table_name=None):
        if not table_name:
            self.from_table_name = f' {SQL_COMMAND_FROM} {self.backticks(self.table())}'
        else:
            if isinstance(table_name, list):
                tables = len(table_name)
                count = 1
            for value in table_name:
                if tables == 1:
                    self.from_table_name += self.backticks(value)
                else:
                    if tables > count:
                        self.from_table_name += self.backticks(value) + ','
                    else:
                        self.from_table_name += self.backticks(value)
                count += 1
            else:
                self.from_table_name += table_name
        return self

def where(self, spalte, operator=None, value=None):
        if operator is None:
            value = operator
            operator = '='

        bedingung = self.formatiereValue(value)

        if operator == OPERATOR_IN:
            bedingung = self.formatiereOperator(value)
        elif operator == OPERATOR_LIKE:
            bedingung = self.formatiereOperator(value)
        elif operator == OPERATOR_NOT_EQUAL:
            bedingung = self.formatiereOperator(value)

        if not self.where:
            self.where.append(f'{SQL_STATEMENT_WHERE} {self.backticks(spalte)} {operator} {bedingung}')
        else:
            self.where.append(f'{SQL_STATEMENT_AND} {self.backticks(spalte)} {operator} {bedingung}')

        return self
    
def primary_key(self):
        if self.klass is None:
            self.klass = type(self).__name__

        try:
            if self.klass not in self.table_primary_keys:
                if hasattr(self.klass, 'primary_keys'):
                    self.table_primary_keys[self.klass] = self.table_primary_keys
                else:
                    raise Exception()
                    

        except Exception as e:
            print(e)

        return self.table_primary_keys[self.klass]

def properties(self):
    if self.klass is None:
        self.klass = type(self).__name__

        try:
            if self.klass not in self.table_properties:
                if hasattr(self.klass, 'primary_keys'):
                    self.table_properties[self.klass] = self.table_properties
                else:
raise Exception()

        except Exception as e:
            print(e)
            

        return self.table_properties[self.klass]

def join(self, table, richtung='LEFT'):
        if table:
            self.join.append(f'{richtung} JOIN {self.backticks(table)}')
        return self

def on(self, spalte1='', spalte2=''):
        try:
            if not spalte1 or not spalte2:
                raise Exception as e 

            spalten_array1 = spalte1.split('.')
            spalten_array2 = spalte2.split('.')

            if len(spalten_array1) == 1:
                raise Exception(self.klass + '::' + inspect.currentframe().f_code.co_name + '(): Wert für Spalte 1"' + spalte1 + '" muss im Format "table_name.row" angegeben werden.')
            else:
                spalte1 = f'{self.backticks(spalten_array1[0])}.{self.backticks(spalten_array1[1])}'

            if len(spalten_array2) == 1:
                raise Exception(self.klass + '::' + inspect.currentframe().f_code.co_name + '(): Wert für Spalte 2"' + spalte2 + '" muss im Format "table_name.row" angegeben werden.')
            else:
                spalte2 = f'{self.backticks(spalten_array2[0])}.{self.backticks(spalten_array2[1])}'

            self.on.append(f'ON {spalte1} = {spalte2}')

        except Exception as e:
            print(e)

        return self

def insert_into(self, spalte=''):
    if not spalte:
        spalte = self.table()
    self.insert = f'INSERT INTO {spalte}'
    return self

def set(self, spalte=[], value=[]):
        operator = '='
        if spalte is not None and value is not None:
            self.set = f'SET {self.prepare_data(spalte, operator, value)}'
        return self

def prepare_data(self, spalte=[], operator=None, value=[]):
        operator = '='
        inhalt = ""
        if spalte:
            total_spalten = len(spalte)
            for i in range(total_spalten):
                if total_spalten == 0:
                    inhalt += f'{spalte[i]} {operator} {value[i]}'
                else:
                    if i < total_spalten - 1:
                        inhalt += f'{spalte[i]} {operator} {value[i]}, '
                    else:
                        inhalt += f'{spalte[i]} {operator} {value[i]}'
        return inhalt

def update(self, spalte):
        if not spalte:
            spalte = self.table()
        self.update = f'UPDATE {spalte}'
        return self

def delete(self):
        self.delete = 'DELETE'
        return self

def build(self):
        if self.query is None:
            self.query = ''
            if self.select is not None:
                self.query += 'SELECT '
                if self.distinct:
                    self.query += 'DISTINCT '
                if self.from_ is None:
                    self.from_()
                self.query += f'{self.select} {self.from_} '
                if self.join and self.on:
                    for i in range(len(self.join)):
                        self.query += f'{self.join[i]} {self.on[i]} '
                if self.where:
                    for value in self.where:
                        self.query += value
                if self.order_by:
                    self.query += self.order_by
                if self.limit:
                    self.query += self.limit
                if self.group_by:
                    self.query += self.group_by
            elif self.insert:
                if self.set:
                    self.query += f'{self.insert} {self.set}'
            elif self.update:
                if self.set:
                    self.query += f'{self.update} {self.set} '
                    if self.where:
                        for value in self.where:
                            self.query += value
            elif self.delete:
                self.query += f'{self.delete} {self.from_} '
                if not self.from_:
                    self.from_()
                if self.where:
                    for value in self.where:
                        self.query += value
        return self.query



def as_array(self):
        if not self.result:
            return False
        if not isinstance(self.result, list):
            return [self.result]
        return self.result

def as_object(self):
        if not self.result:
            return False
        if not isinstance(self.result, dict):
            return {i: v for i, v in enumerate(self.result)}
        return self.result

