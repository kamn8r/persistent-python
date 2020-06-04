def me_time(work_time):
    if work_time < 7:
        pto = "0"
        return pto
    else:
        pto = work_time / 7
        return pto

work_time = int(input("How many days have you worked?"))
print("you have:",me_time(work_time),"days off.")

