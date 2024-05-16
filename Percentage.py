n = int(input())
student_marks = {}
percentage = 0
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

get_student_score = student_marks.get(query_name)

for i in get_student_score:
    percentage += i

result = percentage/len(get_student_score)
print("{:.2f}".format(result))
