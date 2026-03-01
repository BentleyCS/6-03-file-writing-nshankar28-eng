from CSP_6_03_Writing_to_files import writeFile, sortNames, highScore


def test_sortNames():
    sortNames("names.txt", "namesNew.txt")  # must run before reading the file
    with open("namesNew.txt", "r") as f:
        sorted_names = [line.strip() for line in f if line.strip()]
    assert sorted_names == ["Alice", "Bob", "Charlie", "Diana", "Eve"], f"sortNames failed: {sorted_names}"
    print("sortNames passed!")

def test_highScore():
    avg = highScore(100)
    assert avg > 0, "highScore should return a positive average"
    print(f"highScore passed! Returned average: {avg:.2f}")

test_sortNames()
test_highScore()

print("\nAll tests passed!")
