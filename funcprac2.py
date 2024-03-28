def calc_average(score1, score2, score3, score4, score5):
    return (score1+score2+score3+score4+score5) / 5
def determine_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
def main():
    score1 = int(input("Enter score 1: "))
    score2 = int(input("Enter score 2: "))
    score3 = int(input("Enter score 3: "))
    score4 = int(input("Enter score 4: "))
    score5 = int(input("Enter score 5: "))
    avg = calc_average(score1, score2, score3, score4, score5)
    print("Average score:", avg, determine_grade(avg))
main()