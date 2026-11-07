
import os
import matplotlib.pyplot as plt

def main():
    folder = input("Enter the folder name: ")

    text = ""

    for filename in os.listdir(folder):
        if filename.endswith(".py"):
            with open(os.path.join(folder, filename), "r") as file:
                text += file.read().upper()

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    frequencies = []

    total = len(text)

    if total == 0:
        print("No Python files or text found.")
        return

    for letter in letters:
        count = text.count(letter)
        frequency = count / total
        frequencies.append(frequency)

    highest = max(frequencies)

    plt.bar(letters, frequencies)
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    plt.title("Python Code Letter Frequency Analysis")
    plt.ylim(0, highest * 1.1)
    plt.show()


if __name__ == "__main__":
    main()
