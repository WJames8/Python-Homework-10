
import ast

def read_path(filename):
    with open(filename, "r") as file:
        rows, columns = map(int, file.readline().split())

        path = []
        for line in file:
            path.append(ast.literal_eval(line.strip()))

    return rows, columns, path


def encrypt(message, rows, columns, path):
    message = message.upper().replace(" ", "")

    if len(message) > rows * columns:
        raise ValueError("Message is too long for the grid.")

    original_length = len(message)

    while len(message) < rows * columns:
        message += "X"

    grid = []
    for row in range(rows):
        grid.append(list(message[row * columns:(row + 1) * columns]))

    ciphertext = ""

    for row, column in path:
        ciphertext += grid[row][column]

    return ciphertext, original_length


def decrypt(ciphertext, rows, columns, path, original_length):
    grid = [[''] * columns for _ in range(rows)]

    for index, (row, column) in enumerate(path):
        grid[row][column] = ciphertext[index]

    plaintext = ""

    for row in range(rows):
        for column in range(columns):
            plaintext += grid[row][column]

    return plaintext[:original_length]


filename = input("Enter the path file name: ")

rows, columns, path = read_path(filename)

message = input("Enter a message: ")

encrypted, original_length = encrypt(message, rows, columns, path)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, rows, columns, path, original_length)
print("Decrypted message:", decrypted)
