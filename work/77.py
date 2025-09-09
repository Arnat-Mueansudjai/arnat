class ProgrammingExamples:
    def __init__(self):
        pass

    def print_pattern(self, n=6):
        for i in range(1, n+1):
            for j in range(i):
                print(chr(65 + j), end="")  # 65 = ASCII 'A'
            print()

    def is_valid_pan(self, pan):
        if len(pan) != 10:
            return False
        return pan[:5].isalpha() and pan[5:9].isdigit() and pan[9].isalpha()

    def validate_user_pan(self, name, pan):
        if self.is_valid_pan(pan):
            print("Name:", name)
            print("PAN:", pan)
        else:
            print("Invalid PAN number")

    def encrypt(self, message, key=3):
        result = ""
        for char in message:
            result += chr(ord(char) + key)
        return result

    def reverse_string(self, s):
        return s[::-1]


if __name__ == "__main__":
    app = ProgrammingExamples()

    print("1. Print Pattern")
    app.print_pattern()

    print("\n2. Validate PAN")
    app.validate_user_pan("Armat", "ABCDE1234F")

    print("\n3. Encrypt Message")
    encrypted = app.encrypt("HELLO", 3)
    print("Encrypted:", encrypted)

    print("\n4. Reverse String")
    print("Reversed:", app.reverse_string("Python"))
