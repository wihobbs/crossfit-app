### copyright 2021 William Hobbs
### all rights reserved
### license pursuant to MIT Public License
### ----------------------------------------

from pymongo import MongoClient
import datetime
import json


def main():
    ## Client login information on local machine goes here. I use an Atlas cluster.
    db = client["CCF-October"]


    ### testdata = ["Hobbs", "8/18/2021", "30 Clean and Jerks", "75 lbs", "4:58"]

    wod = ["WOD Time (mm:ss)", "Number of Activities"]
    activities = ["Activity", "Sets", "Reps", "Weight (lbs)"]
    answers = {"Date": str(datetime.date.today())}

    for item in wod:
        answers[item] = str(input(item))

    print(answers)
    print(answers.get("Number of Activities"))

    for activity in range(int(answers.get("Number of Activities"))):
        answers[activity] = {}
        for item in activities:
            answer = str(input(item))
            answers[activity][item] = answer
    
    push = json.dumps(answers)
    print(push)

    db.insert_one(push)

main()