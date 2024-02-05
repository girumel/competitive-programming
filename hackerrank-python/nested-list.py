if __name__ == "__main__":
    students = []
    scores = []
    for _ in range(int(input())):
        student = []
        name = input()
        score = float(input())
        student.append(name)
        student.append(score)
        students.append(student)

    for student in students:
        scores.append(student[1])
    for score in scores:
        if scores.count(score) > 1:
            scores.remove(score)

    scores.sort(reverse=True)
    second_lowest_score = scores[-2]

    second_lowest_names = []
    for student in students:
        if student[1] == second_lowest_score:
            second_lowest_names.append(student[0])

    second_lowest_names.sort()
    for name in second_lowest_names:
        print(name)
