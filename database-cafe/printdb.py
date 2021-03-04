

from persistence import repo
from persistence import Employees_Report
import persistence


def print_activities():
    print("Activities")
    for activitie in repo.Activities.find_all():
        print(tuple(activitie.__dict__.values()))


def print_coffee_stands():
    print("Coffee_stands")
    for coffee_stand in repo.Coffee_stands.find_all():
        print(tuple(coffee_stand.__dict__.values()))

def print_employees():
    print("Employee")
    for employee in repo.Employees.find_all():
        print(tuple(employee.__dict__.values()))

def print_product():
    print("product")
    for product in repo.Products.find_all():
        print(tuple(product.__dict__.values()))

def print_supplier():
    print("Supplier")
    for supplier in repo.Suppliers.find_all():
        print(tuple(supplier.__dict__.values()))

def print_employees_report():
    print("Employees Report")
    repo.Employees_Report.get_employees_report()
    # for Employees_Report in repo.Employees_Report.get_employees_report():
    #     print(Employees_Report)

def print_activities_report():
    print("Activities")
    repo.Activities_Report.get_actions_report()
    # for Activities_Report in repo.Activities_Report.get_actions_report():
    #     print(Activities_Report)

def printall():
    print_activities()
    print_coffee_stands()
    print_employees()
    print_product()
    print_supplier()
    print_employees_report()
    print_activities_report()


if __name__ == '__main__':
    printall()