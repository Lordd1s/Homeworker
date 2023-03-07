import re
import base64


def deco_auth(func):
    password_reqs = re.compile(r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!]).*$")

    def wrapper(*args):
        password = ''.join(map(str, args))
        if password_reqs.match(password):
            return func(*args)
        else:
            return "Password must be followed requirements: lengths: 8 or more, chars at least: one number, " \
                   "one special symbol(@#$%^&+=!), one capital letter and one lowercase letter "

    return wrapper


@deco_auth
def auth_test_func(password):
    return f"Function executed. You entered password {password}"


print(auth_test_func("jnljtyhnletkyJJh6541@"))


class Coding:
    @staticmethod
    def encoding(text: str):
        result = base64.b64encode(text.encode())
        return result

    @staticmethod
    def decoding(text: bytes):
        result = base64.b64decode(text)
        return result


user_input = input("Enter the word: ")
res1 = Coding.encoding(user_input)
res2 = Coding.decoding(res1)
print(res1, "\n", res2)
