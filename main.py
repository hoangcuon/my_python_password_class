from password import *
import logging
import sys

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s: %(message)s')

help_dictionary = {
    "\"help\"":"Shows this list.",
    "\"check_password\" or \"password_checker\"":"Checks your made up password to see it is secure enough.",
    "\"generate_password\" or \"password_generator\"":"Generates a random password.",
    }
fuck = f'\n {str(help_dictionary)}\n\nSuggest some ideas pls'
fuck = fuck.replace(",", "\n")
fuck = fuck.replace("{", "")
fuck = fuck.replace("}", "")
fuck = fuck.replace("'", "")

if len(sys.argv) == 2:
    command = sys.argv[1]

    if command == "password_checker" or command == "check_password":
        password_use = input("What will your password be? (jk just make up one): ")
        password(password_to_use=password_use, password_length="").security_check()
    elif command == "generate_password" or command == "password_generator":
        password_len = input("How long will your password be?: ")
        if password_len.isdigit():
            password_len = int(password_len)

            if password_len <= 7:
                logging.error("Please enter a number bigger than 7 the next time you run this command.")
                quit()
        else:
            logging.error("Please enter a number the next time you run this command.")
            quit()
        password(password_length=password_len, password_to_use="").generate()
    elif command == "help":
        logging.info(fuck)
    else:
        logging.error("UNKNOWN_COMMAND")
else:
    logging.error("BLANK_COMMAND")






