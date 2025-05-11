scores =[]
while True:
    score = input("輸入成績")
    if score == "":
        break
    scores.append(score)


score = score[:len(score)]
print(score)
scores.sort()
print(scores)

