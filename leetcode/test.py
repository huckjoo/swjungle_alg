logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]
digits = []
letters = []
for log in logs:
    if log.split()[1].isdigit():
        digits.append(log)
    else:
        letters.append(log)
a = "a b c d e f g h i j k l m"
print(a.split()[1:])
