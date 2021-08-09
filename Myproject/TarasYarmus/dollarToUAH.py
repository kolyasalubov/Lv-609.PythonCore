import requests # Викачуємо модуль для обробки URL
from bs4 import BeautifulSoup # Модуль для роботи з HTML
import time # Викачуємо модуль, щоб пітом виводити текст з вказаними паузами

# Основний клас
class Currency:
	# Силка на сторінку звідки буде братись інфа про акутальний курс
	DOLLAR_UAH = 'https://www.google.com/search?q=1+dollar+to+uah&oq=1+dollar+to+uah&aqs=chrome..69i57j0i22i30j0i10i22i30.2633j0j9&sourceid=chrome&ie=UTF-8'
	# Заголовки для передачі разом з URL 
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

	current_converted_price = 0
	difference = 5 # Різниця з якою буде порівняння і вивід повідомлення

	def __init__(self):
		# Встановлення курсу валюти при створенні обєкту
		self.current_converted_price = float(self.get_currency_price().replace(",", "."))

	# Метод для отримання курсу валюти
	def get_currency_price(self):
		# Парсим всю сторінку
		full_page = requests.get(self.DOLLAR_UAH, headers=self.headers)

		# Розбираємо через BeatifulSoup
		soup = BeautifulSoup(full_page.content, 'html.parser')

		# Отримуємо потрібне значення і повертаємо його
		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		return convert[0].text

	# Перевірка зміни валюти
	def check_currency(self):
		currency = float(self.get_currency_price().replace(",", "."))
		if currency >= self.current_converted_price + self.difference:
			print("Курс виріс")
			self.send_mail()
		elif currency <= self.current_converted_price - self.difference:
			print("Курс впав")
			self.send_mail()

		print("Зараз курс: 1 долар = " + str(currency) + ' гривень')
		time.sleep(10) # Засипання програми на 10 секунд
		self.check_currency()

# Створення обєкту і виклик методу
currency = Currency()
currency.check_currency()
