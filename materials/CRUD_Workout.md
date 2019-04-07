# Python Shell CRUD Workout
> To be a proficient django developer, I should both be familiar with how data is created, read, updated, and deleted, and the syntax needed to perform these operations in the API. This workout is an extension of the official django tutorial's playing with the API section, but with added structure and less explanation. I was practicing this routine on my own, and only decided to compile it in case anybody else finished the tutorial and wanted some additional review.  

### Getting started

Complete the [django polls tutorial](https://docs.djangoproject.com/en/2.1/intro/tutorial01/) using their naming system, or clone my version from the README.md. For these excercises, make sure the server is not running. CTRL + C to exit, if so. 

#### PreWorkout
From your console, navigate to the folder where the sqlite3.db is stored. On my project, this is 'mysite.'

From your console, execute: ```sqlite3 db.sqlite3```

you should now see ```sqlite>``` as the mode of input for your console. 

 

Turn column and headers on, and follow along with the markdown code:
```
sqlite> .mode column
sqlite> .headers on
```

```
sqlite> SELECT * FROM polls_question;
```

the following output should appear:
```
id          question_text                              pub_date           
----------  -----------------------------------------  -------------------
1           What was your first programming language?  2019-04-07 01:30:41
2           What was the first app you ever built?     2019-04-07 01:32:39
3           What was your first tech job?              2019-04-07 01:33:09
4           Do you love coding?                        2019-04-07 01:34:01
```

```
sqlite> SELECT * FROM polls_choice;
```
again, the following will appear.
```
id          choice_text  votes       question_id
----------  -----------  ----------  -----------
1           Python       0           1          
2           Javascript   0           1          
3           C++          0           1          
4           Calculator   0           2          
5           Website      0           2          
6           Game         0           2          
7           Programmer   0           3          
8           Support      0           3          
9           Project Man  0           3          
10          Maybe        0           4          
11          Yes          0           4          
12          I eat, slee  0           4          
```
Lets get rid of all this data. First, note the ```question_id``` column and ```id``` column. Because of the foreign key relationship defined in the models, only matching id's will have logical ```question_text``` and ```choice_text``` relations.

Erase the data in tables:

```DELETE FROM polls_question;```

```DELETE FROM polls_choice;```

let's check it:

```SELECT * FROM polls_question```

```sqlite>```

No data, so the delete was successful.

Now perform a simple insert statement:

```sqlite> INSERT INTO polls_question (question_text, pub_date) VALUES ('how are you', 'April 6th, 2019');```

**Before we check the table again, what do you think the value for id will be?**

There were 4 questions before, and we erased the data.

```SELECT * FROM polls_question```
 
 the output is:
 
 ```
id          question_text  pub_date       
----------  -------------  ---------------
5           how are you    April 6th, 2019
```

id = 5. 

Even though the data is deleted, the auto-increment continues. 

Perform the next 3 commands to fix the current error, and delete the auto-increment from polls_choice:


```UPDATE polls_question SET id = 1;


```UPDATE sqlite_sequence SET seq = 1 where name = 'polls_question';```


```DELETE FROM sqlite_sequence WHERE name = 'polls_choice';```












 








