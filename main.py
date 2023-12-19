import os
import commands
import colorama
from colorama import init
from colorama import Fore, Back, Style
init()
loginActive = True
userlogincache = "NULL" # cache user login
userpasscache = "NULL" # cachd user pass
from datetime import datetime

def get_time():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
# init log file

def init_logs(): 
    if not os.path.exists('log.txt'):
        with open('log.txt', 'w'):
            pass
init_logs()

# add log in log file
def log(logtype: str, logtext: str) -> bool:
    with open('log.txt', 'a') as f:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        f.write(f'[ {logtype} | %s ] {logtext}\n' % (current_time))
    return True

log("LOG", "Log initied")

# users file init

def init_file(): 
    if not os.path.exists('usersbase.file'):
        log("ERROR", "User's base is not exists, creating.")
        log("LOG" ,"User's base created successfully")
        with open('usersbase.file', 'w'):
            pass

# System crash

def crashSystem(reason: str):
	print("Error system secure shutdown failure")
	print("Check log.txt")
	log("FATAL", "System has been not secure shutdowned")
	log("FATAL", "Please re-install system build on oficall githib page")
	log("FATAL", "Or wait for stable build")
	log("FATAL","Crash by reason: ")
	log("FATAL", reason)

# get user from usersbase

def get_user(login: str, password: str, secretcode: str) -> bool:
    with open('usersbase.file', 'r') as f:
        users = f.read().splitlines()
    for user in users:
        args = user.split(':')
        if login == args[0] and password == args[1] and secretcode == args[2]: 
            return True
    return False

# add user to usersbase

def add_user(login: str, password: str, secretcode: str) -> bool:
    with open('usersbase.file', 'r') as f:
        users = f.read().splitlines() 

    for user in users:
        args = user.split(':')
        if login == args[0] and secretcode: 
            return False  
    with open('usersbase.file', 'a') as f:
        f.write(f'{login}:{password}:{secretcode}\n') 
    return True

# main login page

init_file()
log("LOG", "User's base loaded succsesfully")
log("LOG", "Searching ADMIN account.")
admin_account = get_user("root", "admin", "6")
if admin_account == False:
	add_user("root", "admin", "P23A02_standart_root_pass_please_change")
	log("ERROR", "ADMIN Account is not exist, Creating.")
else:
	log("LOG", "ADMIN Account finded! Countinue")
print("")
print(Fore.GREEN +"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("||||			PYTHON OS                               ||||")
print("||||		  	VERSION P23A02                          ||||")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("")
print(Fore.WHITE +"Please register or login")
print("")
print("Hello, please choose:")
print("1. Log-in")
print("2. Register")
print("3. Exit")
print("")
while loginActive:
	userinput = input("> ")
	if userinput == "1":
		os.system('cls||clear')
		print("LOGIN | 1/3")
		print(" ")
		login = input("Enter Login > ")
		userlogincache = login
		os.system('cls||clear')
		print("LOGIN | 2/3")
		print(" ")
		password = input("Enter Password > ")
		userpasscache = password
		os.system('cls||clear')
		print("LOGIN | 3/3")
		print(" ")
		secretcode = input("Enter Secret Passcode > ")
		result = get_user(login, password, secretcode)
		if result:
			print("You successfully log-in into account")
			loginActive = False
			log("LOG", "Log-in in %s account" % (userlogincache))
		else:
			os.system('cls||clear')
			log("WARNING", "Log-in in %s failed" % (userlogincache))
			print("")
			print(Fore.GREEN +"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
			print("||||			PYTHON OS                               ||||")
			print("||||		  	VERSION P23A02                          ||||")
			print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
			print("")
			print(Fore.WHITE +"Please register or login")
			print("")
			print("Hello, please choose:")
			print("1. Log-in")
			print("2. Register")
			print("3. Exit")
			print("")
			print("Wrong Login or Password")
			print("")
	elif userinput == "2":
		os.system('cls||clear')
		print("REGISTRATION | 1/3")
		print(" ")
		login = input("Enter your login > ")
		os.system('cls||clear')
		print("REGISTRATION | 2/3")
		print(" ")
		newpass = input("Enter your password > ")
		os.system('cls||clear')
		print("REGISTRATION | 3/3")
		print(" ")
		secretcode = input("Enter secred Passcode > ")
		os.system('cls||clear')
		log("LOG", "Created new account. Name: %s " % (login))
		add_user(login, newpass, secretcode)
		print("")
		print(Fore.GREEN +"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
		print("||||			PYTHON OS                               ||||")
		print("||||		  	VERSION P23A02                          ||||")
		print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
		print("")
		print(Fore.WHITE +"Please register or login")
		print("")
		print("Hello, please choose:")
		print("1. Log-in")
		print("2. Register")
		print("3. Exit")
		print("")
		print("User created!")
		print("")
	elif userinput == "3":
		log("LOG", "Closing log storage goodbye")
		exit()
	else:
		os.system('cls||clear')
		print("")
		print(Fore.GREEN +"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
		print("||||			PYTHON OS                               ||||")
		print("||||		  	VERSION P23A02                          ||||")
		print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
		print("")
		print(Fore.WHITE +"Please register or login")
		print("")
		print("Hello, please choose:")
		print("1. Log-in")
		print("2. Register")
		print("3. Exit")
		print("")
		print("Wrong answer!")
		print("")
os.system('cls||clear')
mainPanel = True
print("hello,", userlogincache)
print("How can i help you?")
print("1. Change login")
print("2. Change password")
print("3. Enter command ")
print("4. Exit")
while mainPanel:
	userinput = input()
	if userinput == "1":
		with open ('usersbase.file', 'r') as f:
			old_data = f.read()
			print("1")
		print("2")
		new_data = old_data.replace('root:admin:6', 'rbsdfgist:admin:6')
		print("3")
	elif userinput == "2":
		print("2")
	elif userinput == "3":
		commandsPanel = True
		os.system('cls||clear')
		log("LOG", "Enetering in console mode, login: %s" % (userlogincache))
		print("Python OS 2023")
		print("")
		print("Console version, P23A02")
		print("Print help to see help list, or input exit")
		while commandsPanel:
			cmdinput = input("> ")
			if cmdinput == "exit":
				log("LOG", "Exit from console mode, login: %s" % (userlogincache))
				commandsPanel = False
				os.system('cls||clear')
				print("How can i help you?")
				print("1. Change login")
				print("2. Change password")
				print("3. Enter command ")
				print("4. Exit")
			elif cmdinput == "help":
				commands.help()
			elif cmdinput == "check-user":
				username = input("> Username: ")
				commands.checkuser(username)
			elif cmdinput == "run-programm":
				print("Vse programi dolzni bit v papke programms.")
				programm = input("> Programm name: ")
				startprog = input("You are sure to start this programm? Y/N: ")
				if startprog == "Y":
					log("LOG", "Starting programm: %s, login: %s" % (programm, userlogincache))
					os.system('python programms/%s/main.py' % (programm))
				elif startprog == "y":
					log("LOG", "Starting programm: %s, login: %s" % (programm, userlogincache))
					os.system('python programms/%s/main.py' % (programm))
				else:
					print("Program startup failed")
			elif cmdinput == "":
				print("")
			else:
				print("Unknown command type help to see list of commands.")
			
	elif userinput == "4":
		log("LOG", "Closing log storage goodbye")
		break
	else:
		os.system('cls||clear')
		print("[ERROR] Wrong answer!")
		print("How can i help you?")
		print("1. Change login")
		print("2. Change password")
		print("3. Enter command ")
		print("4. Exit")
crashSystem("SYS Process has been closed by user")