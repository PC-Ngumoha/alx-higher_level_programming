# SQL JOINS

### What is a join?
 A `join` is a system used by SQL tables to present data stored in multiple tables as though they were derived from a single table. It's usually used when we want to access to information that have been organized into seperate tables maybe due to some interrelation between them or maybe because we simply need said information to be presented simulataneously.

**NOTE:** *For the following write-up, we will be assuming that we will only be attempting to join two tables namely TableA & TableB together. This is intended to make it easier to explain each concept*

### Different joins available in S.Q.L

#### Inner Join

![Image of Inner Join](https://tableplus.com/assets/images/sql-joins/inner-join.png)

This is a type of join which returns only the values shared in common between the two tables being joined. A simple code example for this using the tables mentioned above would go something like this:
```
SELECT *
FROM TableA
INNER JOIN TableB
ON TableA.col1 = TableB.col2;
```

#### Full Outer Join

##### With Intersection

![Image of Full Outer Join](https://tableplus.com/assets/images/sql-joins/full-join.png)

In this type of join, all values on both tables which satisfies the `ON` condition for the join are returned and presented. A simple example:

```
SELECT *
FROM TableA
FULL JOIN TableB
ON TableA.col1 = TableB.col2;
```

##### Without Intersection

![Image of Full Outer Join without intersection](https://tableplus.com/assets/images/sql-joins/full-outer-join-no-intersection.png)

In this type of join, all values on both tables except those shared in common by both tables which satisfy the `ON` condition for the join are returned and presented. A simple example:

```
SELECT *
FROM TableA
FULL JOIN TableB
ON TableA.col1 = TableB.col2
WHERE TableA.col1 IS NULL 
OR TableB.col2 IS NULL
```

#### Left Outer Join

##### With Intersection

![Image of Left Outer Join](https://tableplus.com/assets/images/sql-joins/left-join.png)

In this type of join, all values in the leftmost table are returned when the `ON` condition is satisfied. A simple example:

```
SELECT *
FROM TableA
LEFT JOIN TableB
ON TableA.col1 = TableB.col2
```


##### Without Intersection

![Image of Left Outer Join without intersection](https://tableplus.com/assets/images/sql-joins/left-join-no-intersection.png)

In this type of join, only the values of the leftmost table which are not shared in common with the rightmost table are returned. A simple example:

```
SELECT *
FROM TableA
LEFT JOIN TableB
ON TableA.col1 = TableB.col2
WHERE TableB.col2 IS NULL
```

#### Right Outer Join

##### With Intersection

![Image of Right Outer Join](https://tableplus.com/assets/images/sql-joins/right-join.png)

In this type of join, all values of the rightmost table are returned as far as they satisfy the `ON` condition. A simple example:

```
SELECT *
FROM TableA
RIGHT JOIN TableB
ON TableA.col1 = TableB.col2
```

##### Without Intersection

![Image of Right Outer Join without intersection](https://tableplus.com/assets/images/sql-joins/right-join-no-intersection.png)
In this type of join, all values of the rightmost table are returned on satisfying the `ON` condition except those values which are shared in common by both of the tables. A simple example:

```
SELECT *
FROM TableA
RIGHT JOIN TableB
ON TableA.col1 = TableB.col2
WHERE TableA.col1 IS NULL
```


