class UserValidator:

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

    @staticmethod
    def validate_age(age):
        return 18<=age<=120

    @staticmethod
    def validate_username(username):
        return len(username) >= 3


print(UserValidator.validate_email("test@example.com"))
print(UserValidator.validate_email("test^example.com"))
print(UserValidator.validate_email("test@examplecom"))
print(UserValidator.validate_age(5))
print(UserValidator.validate_age(121))
print(UserValidator.validate_age(65))
print(UserValidator.validate_username("To"))
print(UserValidator.validate_username("Paweł"))
print(UserValidator.validate_username("Hieromomomkukukukuuknaaaaaan"))
