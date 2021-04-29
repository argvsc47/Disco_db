# Disco
Disco is minimalist password encoded database system made in python, that emphasizes simplicity and efficiency

# Example
```python
import DiscoDB

mydatabase = DiscoDB.Disco() # initialize database client
mydatabase.addDatabase('example') # make a new database called 'example'
print(mydatabase['example']) # use a db_client[db_name] syntax to access database

mydatabase['example'].addTable('mytable', {'column1': [], 'column2': []})

# in the example above we first access our database by using mydatabase['example']
# next we use the addTable method to add a new table to our database called 'mytable'
# the second argument is a dictionary containing column names 'column1' and 'column2' and their initial values (empty in both case)
```
