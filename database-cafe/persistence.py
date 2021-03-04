import sqlite3
import atexit

# DTO



class Employee(object):
    def __init__(self, id, name, salary, coffee_stand):
        self.id = id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand


class Supplier(object):
    def __init__(self, id, name, contact_information):
        self.id = id
        self.name = name
        self.contact_information = contact_information


class Product(object):
    def __init__(self, id, description, price, quantity):
        self.id = id
        self.description = description
        self.price= price
        self.quantity = quantity


class Coffee_stand(object):
    def __init__(self, id, location, number_of_employees):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees


class Activitie(object):
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date


# DAO


class _Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("""
        INSERT INTO employees (id,name,salary,coffee_stand) VALUES (?,?,?,?)
         """, [employee.id, employee.name, employee.salary, employee.coffee_stand])

    def find(self, employee_id):
        c = self._conn.cursor()
        c.execute("""
        SELECT id,name,salary,coffee_stand FROM employees WHERE id = ? 
        """, [employee_id])

        return Employee(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""SELECT id,name,salary,coffee_stand FROM employees""").fetchall()
        return [Employee(*row) for row in all]


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
        INSERT INTO suppliers (id, name, contact_information) VALUES (?,?,?)
        """, [supplier.id, supplier.name, supplier.contact_information])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
        SELECT id, name, contact_information FROM suppliers WHERE id = ?
        """, [supplier_id])

        return Supplier(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""SELECT  id, name, contact_information FROM suppliers""").fetchall()
        return [Supplier(*row) for row in all]



class _Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("""
           INSERT INTO products (id, description, price, quantity) VALUES (?,?,?,?)
           """, [product.id, product.description,product.price, product.quantity])

    def find(self, product_id):
        c = self._conn.cursor()
        c.execute("""
           SELECT id, description, price, quantity FROM products WHERE id = ?
           """, [product_id])

        return Product(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""SELECT id, description, price, quantity FROM products""").fetchall()
        return [Product(*row) for row in all]

    def update(self, id , quantity):
        self._conn.execute("""UPDATE products SET quantity =(?) WHERE  id=(?)""", [quantity,id])





class _Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, coffee_stand):
        self._conn.execute("""
           INSERT INTO coffee_stands (id, location, number_of_employees) VALUES (?,?,?)
           """, [coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees])

    def find(self, coffee_stand_id):
        c = self._conn.cursor()
        c.execute("""
           SELECT id, location, number_of_employees FROM coffee_stands WHERE id = ?
           """, [coffee_stand_id])

        return Coffee_stand(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""SELECT id, location, number_of_employees FROM coffee_stands""").fetchall()
        return [Coffee_stand(*row) for row in all]


class _Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Activitie):
        self._conn.execute("""
           INSERT INTO activities VALUES (?,?,?,?)
           """, [Activitie.product_id, Activitie.quantity, Activitie.activator_id,Activitie.date])

    def find(self, activitie_id):
        c = self._conn.cursor()
        c.execute("""
           SELECT product_id, quantity, activator_id, date FROM activities WHERE id = ?
           """, [activitie_id])

        return Activitie(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""SELECT product_id, quantity, activator_id, date FROM activities""").fetchall()
        return [Activitie(*row) for row in all]


class Employees_Report:
    def __init__(self, conn):
        self._conn = conn

    def get_employees_report(self):

        c = self._conn.cursor()
        c.execute("""
            SELECT employees.name, employees.salary, coffee_stands.location,  (SUM(Products.price * Activities.quantity))
            FROM employees
            LEFT JOIN coffee_stands ON employees.coffee_stand = Coffee_stands.id
            JOIN activities ON employees.id = activities.activator_id
            JOIN products ON activities.product_id = products.id
            GROUP BY employees.id
            ORDER BY employees.name
        """)
        EmployeesReport = c.fetchall()
        if EmployeesReport:
            for e in EmployeesReport:
                print(e)



class Activities_Report:
    def __init__(self, conn):
        self._conn = conn

    def get_actions_report(self):
        ActivitiesReport = repo._conn.cursor().execute("""
        SELECT activities.date, products.description, activities.quantity, employees.name, suppliers.name
        FROM (activities
        LEFT JOIN products ON activities.product_id = products.id
        LEFT JOIN employees ON activities.activator_id = employees.id
        LEFT JOIN suppliers ON activities.activator_id = suppliers.id
        )
        GROUP BY employees.name , suppliers.name
        ORDER BY activities.date DESC
        """).fetchall()

        # ActivitiesReport = c.fetchall()


        if ActivitiesReport:
            for a in ActivitiesReport:
                print(a)



#The Repository
class Repository(object):
    def __init__(self):
        self._conn = sqlite3.connect('moncafe.db')
        self.Employees = _Employees(self._conn)
        self.Suppliers = _Suppliers(self._conn)
        self.Products = _Products(self._conn)
        self.Coffee_stands = _Coffee_stands(self._conn)
        self.Activities = _Activities(self._conn)
        self.Employees_Report = Employees_Report(self._conn)
        self.Activities_Report = Activities_Report(self._conn)



    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""CREATE TABLE employees( 
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                salary REAL NOT NULL,
                coffee_stand INTEGER REFERENCES coffee_stand(id)
                );
                CREATE TABLE suppliers(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                contact_information TEXT
                );
                CREATE TABLE products(
                id INTEGER PRIMARY KEY,
                description TEXT NOT NULL,
                price REAL NOT NULL, 
                quantity INTEGER NOT NULL
                );
                CREATE TABLE coffee_stands(
                id INTEGER PRIMARY KEY,
                location TEXT NOT NULL,
                number_of_employees INTEGER
                );
                CREATE TABLE activities(
                product_id INTEGER INTEGER REFERENCES product(id),
                quantity INTEGER NOT NULL,
                activator_id INTEGER NOT NULL,
                date DATE NOT NULL
                );""")






repo = Repository()
atexit.register(repo._close)

