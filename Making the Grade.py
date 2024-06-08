def round_scores(student_scores):
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    return sum(1 for score in student_scores if score <= 40)


def above_threshold(student_scores, threshold):
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    increment = round((highest - 40) / 4)
    lower_thresholds = [41]
    i = 1
    while i < 4:
        lower_thresholds.append(lower_thresholds[0] + increment * i)
        i += 1
    return lower_thresholds


def student_ranking(student_scores, student_names):
    rankings = []
    for index, score in enumerate(student_scores):
        student = student_names[index]
        ranking_string = f"{index + 1}. {student}: {score}"
        rankings.append(ranking_string)
    return rankings


def perfect_score(student_info):
    for student in student_info:
        name, score = student
        if score == 100:
            return student
    return []
