# create the project folder
mkdir empmgr-project

# enter in directory
cd empmgr-project

#check the path 
pwd

#create the folder inside project folder
mkdir empmgr
mkdir data

#then i create the empty folder 
__init__.py

#create the differnt module

empmgr/

__init__.py
models.py    # why we can used this @dataclass
storage.py
cli.py
validators.py


#put code module vise 
#import in __init__.py module 

from .storage import load_employees, save_employees
________________________________________________________________________________


1) create the virtual environment 

python -m venv .venv

2) go to the activate directory  to activate environment 

.venv\Scripts\Activate.ps1

3)install rich 

pip install rich

4) import in cli.py

from rich.console import Console
from rich.table import Table

if choice == "1":
    table = Table(title="Employees")

    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Department")
    table.add_column("Salary")

    for employee in employees:
        table.add_row(
            str(employee["id"]),
            employee["name"],
            employee["department"],
            f"{employee['salary']:,.2f}"
        )

    Console().print(table)




5) genrate requirment.txt
pip freeze > requirements.txt

6) run application using 

python -m empmgr.cli


________________________________________________________

# initialize git empty repo

git init

# check the status of your current changes 

git status

# create the .gitignore

# create and connect new repo in github 

git remote add origin YOUR_NEW_GITHUB_REPO_URL

# chck the current fetch and origin 

git remote -v

# check branch

git branch

# rename branch 

git branch -M main

# add changes 
git add .gitignore

# commite
git commit -m "Add Git ignore rules"

# git push -u origin main

