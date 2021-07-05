def login():
	permission = False
	login = input("Enter Login ---> ")
	while not permission:
		if login == "First":
			permission = True
			return print(f"Hello, {login}")
		else:
			login = input("I dont know this username, try again. Login ---> ")


if __name__ == "__main__":
	login()