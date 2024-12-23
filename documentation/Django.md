# Django Documentation

### Use Instructions:

##### Models.py

Within models.py are classes that are the data models in Django. With these, you are able to use them to create, get, update, and delete just like SQL queries. Since there are two tables, there are two classes.

Users: the model that interacts with the user table in the database.

Boards: the model that interacts with the board table in the database.

For information about the classes themselves, view comments in the models.py file.

##### Create Objects

To represent the database table, this is how Django does it. The class represents the entire database table and an instance of that class represents a particular record or query statement in that database table.

###### Insert

The following Django code initializes an instance of the User class. This is equal to the Insert statement in MySQL.

```
from sudoku.models import Users
u = Users(id="username", pwd="password", email="test@email.com")
u.save()
```

Note: Django **does not** connect to the database until you call `save`

###### Insert Shortcut

There is a shortcut you can use to create a row in the database. The `create` method combined creating an instance and then applying the `save` function all in one go. An example code snippet is below.

```
alt_u = Users.objects.create(id="user", pwd="pass", email="something@test.com")
```

Note: It requires you to use `objects` on the **class**. See below for further details.

###### Get

To retrieve rows of data from our database, we must create a QuerySet on our model class by calling `objects` on the **class**. This QuerySet can have zero or many filters and is the equivalent of the Select statement with `filter` representing the limiting causes such as Where and Limit. To get only a single row of data you can use the `get` method.

See an example Select all users statement.

```
all_users = Users.objects.all()
```

And here's an example of a Select statment with a Where filter.

```
r_users = Users.objects.filter(id__startsWith("R"))
```

And here's an example of getting a specific user.

```
one_user = Users.get(id="Bucky Badger")
```

Note: QuerySets are lazy thus creating a QuerySet does not involve database activity. The SQL query is only run once the QuerySet is evaluated. For more information, view the Making Queries reference at the end of the document.

###### Update

Once you have an instance, either via creating a new instance or retrieving one via get, you can then make any change then call `save`. This is the equivalent of the Update in SQL. For example:

```
one_user.password = "p@ssw0rd"
one_user.save()
```

This performs an Update statement that changes Bucky Badger's password.

Note: Like when inserting, Django does not hit the database until you call `save`.

You are also able to edit several rows at once with the `update` method. For example, if we wanted to change the email for all the users that start with the letter R this is how we would do it:

```
r_users.update(email="share@email.com")
```

###### Delete

Similar to update, when you have an instance or a QuerySelect, you can call `delete` on those and that is the equivalent of the Delete SQL method.

For example, this is deleting all the users that start with "R".

```
r_users.delete()
```

And this is deleting the user we first created in the Insert section.

```
u.delete()
```

### References:

[Making queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/)
