def studentmarks(marks):
    if marks>=80:
        return "Destinction"
    elif marks>=60:
        return "FirstClass"
    elif marks>=30:
            return "SecondClass"
    else :
        return "Fail"

Status=studentmarks(59)
print(Status)