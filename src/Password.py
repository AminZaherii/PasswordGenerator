import random
import string


from jsonschema.validators import validate


# base class for generate password
class Password:
    def __init__(self, length):
        self.length = length

    def set_length(self, length):
        self.length = length


# class for generate numeric password as pincode
class PinCode(Password):
    def __init__(self, length):
        super().__init__(length=length)

    def generate(self):
        pincode = ''
        for i in range(self.length):
            pincode += str(random.randint(0, 9))
        return pincode


# class for generate complicated password
class ComplicatedPassword(Password):
    def __init__(self, length):
        super().__init__(length=length)
        self.characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    def generate(self):
        password = ''
        for i in range(self.length):
            password += random.choice(self.characters)
        return password

    def validate(self, password):
        lowercase_char = 0
        uppercase_char = 0
        digits_char = 0
        punctuation_char = 0
        for c in password:
            if c in string.ascii_lowercase:
                lowercase_char += 1
            elif c in string.ascii_uppercase:
                uppercase_char += 1
            elif c in string.digits:
                digits_char += 1
            elif c in string.punctuation:
                punctuation_char += 1

        print(lowercase_char)
        print(uppercase_char)
        print(digits_char)
        print(punctuation_char)
        if lowercase_char == 0 or uppercase_char == 0 or digits_char == 0 or punctuation_char == 0 or len(
                password) < self.length:
            return False
        else:
            return True