# Sudoku database schema

Our app will use one table to store users and another to store boards. They are located in the sudoku-db-1 container.

### Signature:

`user(id, email, pwd, token)`

- id: username associated with particular user
- email: email user inputs to access account
- pwd: password user inputs to access account
- token: authentication program uses to verify user has signed in properly

`board(id, state, difficulty, answer, style, user, isfinished, initState)`

- id: unique identifier for board
- state: current user progress
- difficulty: easy, medium, or hard
- answer: solution (final state)
- style: variant selected by user
- user: user id (who is solving this board)
- isfinished: 0 or 1 based on whether board is completed
- initState: the initial generated state of the board

### Relations and typing:

Users are keyed by their id/username. Boards are keyed by their id. This is a many-to-one relation, where one user can have many boards associated with them. Currently, all fields are either ints or strings, but this can be changed as determined.

### Relational diagram:

![ERD](./Sudoku DB Schema_updated.png)

### Example query:

```sh
SELECT id, state
    FROM Boards
    WHERE isfinished == True
```

### Modifying the table:

See https://www.w3schools.com/mysql/mysql_alter.asp.
