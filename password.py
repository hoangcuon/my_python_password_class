import random
import re
import logging

logging.basicConfig(level=logging.INFO, format='[(%(asctime)s) - %(levelname)s] %(message)s')
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
abcs = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '', ' '
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
higher_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|',
                '\\', ':', ';', '?', '/', "\"","'","\<","\,","\>","\."]

class Password:

    def __init__(self, password_length, password_to_use):
        self.password_length = password_length
        self.password_to_use = password_to_use

    def generate(self):
        letters = number + alphabet + symbols + higher_case
        list = []
        val = ""

        for i in range(self.password_length):
            random.shuffle(letters)
            list.append(random.choice(letters))

        password = val.join(list)
        logging.info(f'Password: {password}')

    def security_check(self):
        password = self.password_to_use
        a = '|'.join(map(re.escape, abcs))
        a = re.split(a, password)

        check = any(item in a for item in number)
        check_again = any(item in a for item in symbols)
        check_again_2 = any(item in a for item in higher_case)
        if len(password) > 7 and check and check_again and check_again_2:
            logging.info("Pass!")
        elif len(password) <= 7:
            logging.error("Please enter a password to continue.")
        else:
            logging.error("Your password must contain a number, symbol, lowercase and highercase letters.")


        

