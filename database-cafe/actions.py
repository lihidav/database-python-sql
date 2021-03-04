import sqlite3

from persistence import *
import datetime
# The Repository
from persistence import _Employees
from persistence import _Activities
from persistence import _Coffee_stands
from persistence import _Products
from persistence import _Suppliers
from persistence import Repository
import sys
import os


def action():
    # actionFileName = args[0]
    # with open(actionFileName) as actionFile:
    actionFile = open(sys.argv[2], 'r')
    for line in actionFile:
        line=line.strip()
        line = line.split(', ')
        if int(line[1]) + int(repo.Products.find(line[0]).quantity) >= 0:
            quantity = line[1]
            quantity1 = int(repo.Products.find(line[0]).quantity) + int(quantity)
            repo.Products.update(line[0], quantity1)
            repo.Activities.insert(Activitie(line[0], line[1], line[2], line[3]))
        repo._conn.commit()

            # month = line[4:6]
            # if month[:1] == "0":
            #     month1 = month[1]
            # else:
            #     month1 = month
            # date = date(int(date[:4]), int(month1), int(date[6:]))

        #
        # else:
        #     id_supplier = line[2]
        #     id_profuct = line[0]
        #     quantity = line[1]
        #     date = line[3]
        #     date = datetime.date(date[:4], date[4:6], date[6:])
        #     repo.Activities.insert(id_product, quantity, id_supplier, date)


if __name__ == '__main__':
    action()
