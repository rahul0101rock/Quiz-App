import django
import pandas as pd
import os
import quiz
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz.settings")
django.setup()
from quizapp.models import Questions
from pathlib import Path

csvfile = Path(r"Database_manage/questions.csv")  # Your csv file path
df = pd.read_csv(csvfile)
sh = df.shape
c = 0
for i in range(sh[0]):
    c += 1
    q = 'q' + str(c)
    q = Questions(
        question=df.iloc[i, 0],
        option_a=df.iloc[i, 1],
        option_b=df.iloc[i, 2],
        option_c=df.iloc[i, 3],
        option_d=df.iloc[i, 4],
        answer=df.iloc[i, 5],
        catagory=df.iloc[i, 6], # choose a right value
    )
    q.save()
print("done")
