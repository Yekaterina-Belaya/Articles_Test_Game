task1 = input("Fill in the gaps with an article: ")
task2 = input("Fill in the gaps with an article: ")
task3 = input("Fill in the gaps with an article: ")
task4 = input("Fill in the gaps with an article: ")
task5 = input("Fill in the gaps with an article: ")
task6 = input("Fill in the gaps with an article: ")
task7 = input("Fill in the gaps with an article: ")
task8 = input("Fill in the gaps with an article: ")

paragraph = "When {} spotted cat first found {} nest, there was nothing in it, for it was only just finished. \nSo she said, 'I will wait!' for she was {} patient cat, and {} summer was before her. She waited {} week, \nand then she climbed up again to {} top of {} tree, and peeped into {} nest. \nThere lay two lovely blue eggs, smooth and shining.".format(task1, task2, task3, task4, task5, task6, task7, task8)

print("\nAnd here's what you got:")

print("\n" + paragraph)

score = 0

if task1 == "the":
    score += 1

if task2 == "the":
    score += 1

if task3 == "a":
    score += 1

if task4 == "the":
    score += 1

if task5 == "a":
    score += 1

if task6 == "the":
    score += 1

if task7 == "the":
    score += 1

if task8 == "the":
    score += 1

print("\nYou've got", score, "correct answers out of 8.")