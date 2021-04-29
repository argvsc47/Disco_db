# Disco
Disco is minimalist password encoded database system made in python, that emphasizes simplicity and efficiency

# Installation
```
pip install Disco_db
```
# Examples

## making a new database and table

```python
import Disco_db

myclient = Disco_db.Disco() # initialize database client
myclient.addDatabase('example') # make a new database called 'example'
# you can also specify a custom password instead of the default "12345678" and a custom salt instead of 'salt_'
# by setting the arguments pw and sl respectively

print(myclient['example']) # use a db_client[db_name] syntax to access database

myclient['example'].addTable('mytable', {'column1': [], 'column2': []})

# in the example above we first access our database by using myclient['example']
# next we use the addTable method to add a new table to our database called 'mytable'
# the second argument is a dictionary containing column names 'column1' and 'column2' and their initial values (empty in both case)
```

## saving a database

```python
...

myDatabase['example'].commit() 
# the commit method saves the database in a file with the .dd extension encoded with an elliptic curve
```

## loading a database

if you already have a database, to access it you can follow the example below

```python
import Disco_db

myclient = Disco_db.Disco()
myclient.loadDatabase('example') 
# if you used the default settings when making your database this is enough else you can specify the pw and sl argument again

print(myclient['example'])
```
