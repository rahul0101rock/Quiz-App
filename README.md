# Quiz-App
This is a simple Quiz Application, which offers simple quiz in multiple categories. Each category contains 10 questions (or more). when user submit the answer, user gets his/her score and the efficiency on the basis of his/her answers. 
## https://nvquizapp.pythonanywhere.com/

## Starting Quiz App
```
python manage.py makemigrations

python manage.py migrate
```
This create necessary tables for django and **Create table for model Questions (quizapp_questions)**

## Add or Remove from Category
### In *quizapp/models.py*
```python
CAT_CHOICES = (
        ('python', 'Python'),
        ('django', 'Django'),
        ('numpy', 'Numpy'),
        ('java', 'Core Java'),
    )
```
Add or Remove entries from **CAT_CHOICES**

## Add or Remove Questions from any Category
### In *Database_manage/questions.csv*
#### https://github.com/rahul0101rock/Quiz-App/blob/main/Database_manage/questions.csv
Add or Remove entries from *questions.csv* file

**Then run *importdB.py***

it will update data in table *quizapp_questions* in the database and then it will start showing on website
