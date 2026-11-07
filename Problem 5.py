
import urllib.request
import matplotlib.pyplot as plt

def main():
    url = input("Enter the URL of the text file: ")

    response = urllib.request.urlopen(url)
    text = response.read().decode("utf-8").upper()
    response.close()

    counts = [0] * 256

    for character in text:
        value = ord(character)

        if value < 256:
            counts[value] += 1

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    frequencies = []

    total = sum(counts)

    for letter in letters:
        count = counts[ord(letter)]
        frequency = count / total
        frequencies.append(frequency)

    highest = max(frequencies)

    plt.bar(letters, frequencies)
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    plt.title("Letter Frequency Analysis")
    plt.ylim(0, highest * 1.1)
    plt.show()

    filename = input("Enter the output file name: ")

    with open(filename, "w") as file:
        for letter in letters:
            count = counts[ord(letter)]
            file.write(f"{letter} {count}\n")

    print("Frequency data saved to", filename)


if __name__ == "__main__":
    main()
