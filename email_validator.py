class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.__min_length = min_length
        self.__mails = mails
        self.__domains = domains

    def validate_name(self, name):
        return len(name) >= self.__min_length

    def validate_mail(self, mail):
        return mail in self.__mails

    def validate_domain(self, domain):
        return domain in self.__domains

    def validate(self, email):
        name, rest = email.split("@")
        mail, domain = rest.split(".")

        if self.validate_name(name) and self.validate_mail(mail) and self.validate_domain(domain):
            return True
        else:
            return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com")) 
print(email_validator.validate("georgios@gmail.net"))  
print(email_validator.validate("stamatito@abv.net"))  
print(email_validator.validate("abv@softuni.bg"))  

# Output: True
# Output: False
# Output: False
# Output: False
