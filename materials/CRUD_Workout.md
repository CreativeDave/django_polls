# Python Shell CRUD Workout
> To be a proficient django developer, I should both be familiar with how data is created, read, updated, and deleted, and the syntax needed to perform these operations in the API. This workout is an extension of the official django tutorial's playing with the API section, but with added structure and additional attention to the database operation. I was practicing this routine on my own, and only decided to compile it in case anybody else finished the tutorial and wanted some additional review.  

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


```UPDATE polls_question SET id = 1;```


```UPDATE sqlite_sequence SET seq = 1 where name = 'polls_question';```


```DELETE FROM sqlite_sequence WHERE name = 'polls_choice';```

Now the auto incrementing primary key will begin at 1 for both tables. We have 1 question, and 0 choices. 

Open the python shell and let's begin the workout in the API. ```CTRL + D```  exits the sqlite console.

```python manage.py shell```

When you see the ```>>>``` its time to **begin.**
```
>>> from polls.models import *
>>> from django.utils import timezone
```

#### SET 1:

 1. insert data into *question_text* and *pub_date* to create Question object.
 ```
 >>> Question(question_text="whats your name?", pub_date=timezone.now()).save()
 ```
 2. view all question objects. Observe how objects are derived.
 ```
 >>> Question.objects.all()

 <QuerySet [<Question: how are you>, <Question: whats your name?>]>
 ```
 3. insert data for Choice class objects, observe fk question_id
 ```
 >>> Choice(choice_text="nada", votes=0, question_id=1).save()
 
 >>> Choice(choice_text="Dave", votes=0, question_id=2).save()
 ```
 4. view all choices. Which table and column? question_id? 
 ```
 >>> Choice.objects.all()

 <QuerySet [<Choice: Dave>, <Choice: nada>]>
 ```
 5. assign variable to question we just created using id attribute
 ```
 >>> q=Question.objects.get(id=2)
 ```
 6. view choices. observe databse is filtering fk question_id = 2
 ```
 >>> q.choice_set.all()
 
 <QuerySet [<Choice: Dave>]>
 ```

#### SET 2:

1. create another question
```
>>> Question(question_text="whats the time?", pub_date=timezone.now()).save()
```
2. create a choice, note fk question_id
```
>>> Choice(choice_text="noon", votes=0, question_id=3).save()
```
3. create another choice
```
>>> Choice(choice_text="midnight", votes=0, question_id=3).save()
```
4. view all questions. how is id being handled for each in db?
```
>>> Question.objects.all()

<QuerySet [<Question: how are you>, <Question: whats your name?>, <Question: whats the time?>]>
```
5. assign variable to question, using primary key this time
```
>>> q=Question.objects.get(pk=3)
```
6. view all related choices. observe how choice_set filters question_id = 3
```
>>> q.choice_set.all()

<QuerySet [<Choice: noon>, <Choice: midnight>]>
```
7. change question text and save
```
>>> q.question_text="what time is it?"

>>> q.save()
```

#### SET 3

1. create another question
```
>>> Question(question_text="favorite color?", pub_date=timezone.now()).save()
```
2. create a choice
```
>>> Choice(choice_text="blue", votes=0, question_id=4).save()
```
3. create another choice
```
>>> Choice(choice_text="green", votes=0, question_id=4).save()
```
4. view Question class object data with id 4
```
>>> Question.objects.filter(id=4)

<QuerySet [<Question: favorite color?>]>
```
5. view choices for this question. How is this being filtered?
```
>>> Question.objects.get(id=4).choice_set.all()

<QuerySet [<Choice: blue>, <Choice: green>]>
```
6. select choice blue, and assign it a variable
```
c=Question.objects.get(pk=4).choice_set.get(choice_text="blue")
```
7. change the value to red and save
```
>>> c.choice_text="red"

>>> c.save()
```
8. view choices again for this question
```
>>> Question.objects.get(id=4).choice_set.all()

<QuerySet [<Choice: red>, <Choice: green>]>
```
9. count the choices. observe db is only filtering on fk
```
>>> Question.objects.get(id=4).choice_set.count()

2
```
10. filter choice_set using built-in functions 
```
>>> Question.objects.get(id=4).choice_set.filter(choice_text__startswith='green')
    
<QuerySet [<Choice: green>]>
```
11. assign all data from question class objects to variable
```
q=Question.objects.all()
```
12. delete all Question objects
```
>>> q.delete()

(10, {'polls.Choice': 6, 'polls.Question': 4})
```

##### Cool down

we can check the polls_question table to make sure the data was deleted:
```
>>> Question.objects.all()

<QuerySet []>
```
But what do you think about polls_choice? In the sqlite command line interface we had to delete the data from each table separately. 

```
>>> Choice.objects.all()

<QuerySet []>
```

The Choice objects were deleted as well. This has to do with how we assigned the foreign key relationship in models.py. If you take a look, you'll see the parameter ```on_delete=models.CASCADE```

```
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
 ```
 
 if *CASCADE* is specified, when the referenced object is deleted, it also delete the objects that have references to it.
 
 If we wanted to delete all Question objects, sparing the Choice objects, we would have to instead specify:
 
 ```question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, NULL=True)```
 
But this would create a situation with a possible reference to an object that doesn't exist, best to leave it as CASCADE for this simple application.
 

