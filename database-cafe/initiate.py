import sqlite3

from persistence import *

# The Repository
from persistence import _Employees
from persistence import _Activities
from persistence import _Coffee_stands
from persistence import _Products
from persistence import _Suppliers
from persistence import Repository
import sys
import printdb
import actions
import os


if os.path.isfile("moncafe.db"):
    os.remove("moncafe.db")
    repo.__init__()

def my_main():
    # inputFileName = args[0]
    # with open(inputFileName) as inputFile:
    inputFile = open(sys.argv[1], 'r')
    for line in inputFile:
        # if len(line[0])-1:
        line = line.strip()
        line = line.split(', ')
        if line[0] == 'C':
            repo.Coffee_stands.insert(Coffee_stand(line[1], line[2], line[3]))
        elif line[0] == 'S':
            repo.Suppliers.insert(Supplier(line[1], line[2], line[3]))
        elif line[0] == 'E':
            repo.Employees.insert(Employee(line[1], line[2], line[3], line[4]))
        elif line[0] == 'P':
            repo.Products.insert(Product(line[1], line[2], line[3], 0))
    repo._conn.commit()







if __name__ == '__main__':
    repo.create_tables()
    my_main()
    actions.action()
    printdb.printall()
