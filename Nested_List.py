students = list()
score_list = list()
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
    score_list.append(score)

score_list = list(set(score_list))
score_list.sort()
second_high = score_list[-2]

out = [i[0] for i in students if i[1] == second_high]
out.sort
for i in out:
    print(i)
