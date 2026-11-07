
import matplotlib.pyplot as plt

def main():
    filename = input("Enter the input file name: ")

    with open(filename, "r") as file:
        text = file.read().upper()

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    frequencies = []

    total = len(text)

    for letter in letters:
        count = text.count(letter)
        frequency = count / total
        frequencies.append(frequency)

    highest = max(frequencies)

    plt.bar(letters, frequencies)
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    plt.title("Letter Frequency Analysis")
    plt.ylim(0, highest * 1.1)
    plt.show()


if __name__ == "__main__":
    main()
