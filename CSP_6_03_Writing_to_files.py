import random

def writeFile(inputList, fileName):
    with open(fileName, "w") as f:
        for item in inputList:
            f.write(str(item) + "\n")


def sortNames(fileName, targetFile):
    with open(fileName, "r") as f:
        names = [line.strip() for line in f if line.strip()]

    names.sort()

    with open(targetFile, "w") as f:
        for name in names:
            f.write(name + "\n")

    print(f"Sorted names written to '{targetFile}': {names}")


def highScore(newScore: int):
    with open("scores.txt", "a") as f:
        f.write(str(newScore) + "\n")

    with open("scores.txt", "r") as f:
        scores = [int(line.strip()) for line in f if line.strip()]

    average = sum(scores) / len(scores)
    print(f"New score: {newScore} | All scores: {scores} | Average: {average:.2f}")
    return average

writeFile(["Charlie", "Alice", "Eve", "Bob", "Diana"], "names.txt")
writeFile([45, 78, 92, 61, 55], "scores.txt")
sortNames("names.txt", "namesNew.txt")
highScore(random.randint(1, 100))