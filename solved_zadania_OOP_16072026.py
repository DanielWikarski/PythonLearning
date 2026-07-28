def validate_non_empty_strigs(**values) -> None:
    for name, value in values.items():
        if not isinstance(value, str) or not value.strip():
            raise TypeError(f'Value {name} must be a non-empty string')


        
def validate_single_string_input(value: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise TypeError('Value must be a non-empty string')



        
class Address:
    def __init__(self, postal_code:str, city:str, street:str, house_number:str) -> None:

        validate_non_empty_strigs(
            postal_code=postal_code,
            city=city,
            street=street,
            house_number=house_number
        )

        self.postal_code = postal_code
        self.city = city
        self.street = street
        self.house_number = house_number

            
    def to_dict(self) -> dict:
        dict_summary = {
            "postal_code" : self.postal_code,
            "city" : self.city,
            "street" : self.street,
            "house_number": self.house_number
        }
        return dict_summary


class Job:

    def __init__(self, company: str, position: str, salary: float):
        validate_non_empty_strigs(
            company=company,
            position=position
        )
        if not isinstance(salary, float) or salary < 0:
            raise TypeError('Salary must be a positive float')

        self.company = company
        self.position = position
        self.salary = salary

    def give_rise(self, raise_amount):
        if not isinstance(raise_amount, float):
            raise ValueError("Value has to be numeric!")
        self.salary += raise_amount


    def to_dict(self) -> dict:
        dict_summary = {
            "company" : self.company,
            "position" : self.position,
            "salary" : self.salary
        }
        return dict_summary


class Person:

    def __init__(self, name: str, age: int, address: Address, job: Job = None) -> None:

        validate_non_empty_strigs(name=name)

        if not isinstance(age, int) or age < 0:
            raise TypeError('Age must be a positive integer')

        if not isinstance(address, Address):
            raise TypeError('address must be an instance of Address')

        if job is not None and not isinstance(job, Job):
            raise TypeError('job must be an instance of Job')

        self.name = name
        self.age = age
        self.address = address
        self.job = job
        self.friends = []

    def __repr__(self) -> str:
        return f'{self.name}, {self.age} lat'

    def add_friend(self, friend: 'Person') -> None:

        if not isinstance(friend, Person):
            raise TypeError('friend must be an instance of Person')

        if friend in self.friends:
            raise ValueError(f'{friend} is already on the friends list')

        if friend is self:
            raise ValueError('you cannot be friend with yourself')

        self.friends.append(friend)

    def remove_friend(self, friend_name:Person):
        if friend_name in self.friends:
            self.friends.remove(friend_name)
        else:
            print("Friend not found")



    def to_dict(self) -> dict:
        dict_summary = {
            "name" : self.name,
            "age" : self.age,
            "friends" : [friend for friend in self.friends],
            "address" : {
            "postal_code" : self.address.postal_code,
            "city" : self.address.city,
            "street" : self.address.street,
            "house_number": self.address.house_number
            },
            "job" : {
            "company" : self.job.company,
            "position" : self.job.position,
            "salary" : self.job.salary
            }
        }
        return dict_summary



class Employee(Person):
    def __init__(self, employee_id:int, departament:str,name: str, age: int, address: Address, job: Job = None) -> None:
        super().__init__(name, age, address, job)
        self.employee_id = employee_id
        self.departament = departament


class Author:
    def __init__(self, name:str, surname:str) -> None:
        self.name = name
        self.surname = surname

    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"

    def to_dict(self) -> dict:
        author = {
            "Author's name" : self.name,
            "Author's surname" : self.surname
        }
        return author


class Book:
    def __init__(self,book_title:str, book_author:Author, relase_date:int, pages:int ) -> None:

        validate_single_string_input(book_title)
        validate_single_string_input(book_author.name)
        validate_single_string_input(book_author.surname)
        if not isinstance(relase_date, int) and relase_date > 0:
            raise ValueError("Relase date has to be a number")
        if not isinstance(pages, int) and pages > 0:
                    raise ValueError("Number or pages has to be a number")
        self.book_title = book_title
        self.book_author = book_author
        self.relase_date = relase_date
        self.pages = pages

    def __repr__(self) -> str:
        return f"{self.book_title}, {self.relase_date}"

    def to_dict(self) -> dict:
        book_to_dict = {
            "book_title" : self.book_title,
            "book_author" : {
            "Author's name" : self.book_author.name,
            "Author's surname" : self.book_author.surname,
        },
        "relase_date" : self.relase_date,
        "pages" : self.pages

        }
        return book_to_dict




class Library:
    def __init__(self, librarys_name) -> None:
        self.librarys_name = librarys_name
        self.books =  []

    def add_book(self,book:Book):
        if not  isinstance(book, Book):
            raise ValueError("Passed argument is not a Book's object.")
        if book in self.books:
            raise ValueError("Book already exists in library and cannot be added again untill removed")
        self.books.append([str(book.book_title),int(book.relase_date),int(book.pages),str(book.book_author)])

    def remove_book(self, book:Book):
        if not book in self.books:
            raise ValueError("Book cannot be removed due to it doesn't exists in library")
        self.books.remove(book)


    def find_books_by_author(self, surname):
        found_books = []
        for book in self.books:
            if surname in book:
                found_books.append(book)
        return found_books

    def sort_books_by_year(self) -> list:
        books_sorted_year = sorted(self.books, key=lambda book: book[1])
        return books_sorted_year

    def sort_books_by_pages_desc(self) -> list:
        books_sorted_pages = sorted(self.books, key=lambda book: book[2], reverse=True)
        return books_sorted_pages

    def get_title_year_pairs(self) -> list:
        title_year_pairs =  []
        for book in self.books:
            title_year_pairs.append((book[0],book[1]))
        return title_year_pairs

    def sort_title_year_pairs(self) -> list:
        title_year_pairs = self.get_title_year_pairs()
        title_year_pairs = sorted(title_year_pairs, key=lambda pair: pair[1])
        return title_year_pairs

    def get_statistics(self):

        if len(self.books) == 0:
            print("There are no books in library yet.")
            return
        book_count = 0
        pages_count = 0
        for book in self.books:
            book_count += 1
            pages_count += book[2]
        avg_pages_count = pages_count // book_count
        return book_count, pages_count, avg_pages_count

    def to_dict(self) -> dict:
        library_info = {"Library's name" : self.librarys_name,
            "Books" : {

            }
        }

        for book in self.books:
            library_info["Books"][book[0]] = book[-1]
        return library_info





class Book2:
    def __init__(self,book_title:str, book_author:Author, pages:int, is_book_read:bool ) -> None:

        validate_single_string_input(book_title)
        validate_single_string_input(book_author.name)
        validate_single_string_input(book_author.surname)
        if not isinstance(pages, int) and pages > 0:
                    raise ValueError("Number or pages has to be a number")
        if not isinstance(is_book_read, bool):
                            raise ValueError("Book's read status has to be a bool type")
        self.book_title = book_title
        self.book_author = book_author
        self.pages = pages
        self.is_book_read = is_book_read

    def __repr__(self) -> str:
        return f"{self.book_title} - {self.book_author.name} {self.book_author.surname}, {self.pages} stron."



    @property
    def is_long(self) -> bool:
        if self.pages > 300:
            return True
        else:
            return False


    def mark_as_read(self):
        self.is_book_read = True




class BankAccount:

    def __init__(self, holders_name, initial_balance) -> None:
        validate_single_string_input(holders_name)
        if not isinstance(initial_balance, float | int) or initial_balance <0:
            raise TypeError("Balance has to be numeric type such as float or intiger and cannot be negative.")
        self.holders_name = holders_name
        self.__initial_balance = initial_balance
        self.operation_list = []


    def balance(self) -> float | int:
        return self.__initial_balance

    def deposit(self, deposit_amount:float | int):
        if isinstance(deposit_amount, int | float) and deposit_amount > 0:
            self.__initial_balance = self.__initial_balance + deposit_amount 
            self.operation_list.append(("deposit", deposit_amount))
        else:
            raise ValueError("Deposit amount has to be type of intiger or float and cannot be negative")

    def withdraw(self, withdraw_amount:float | int):
        if isinstance(withdraw_amount, int | float) and withdraw_amount > 0:
            if self.__initial_balance > withdraw_amount:
                self.__initial_balance = self.__initial_balance - withdraw_amount 
                self.operation_list.append(("withdraw", withdraw_amount))
            else:
                raise ValueError("You cannot withdraw more than you own")
        else:
            raise ValueError("Withdraw amount has to be type of intiger or float and cannot be negative")

    def show_account_history(self):
        for operation in self.operation_list:
            print(operation)


    def __lt__(self, other):
        return self.__initial_balance < other.__initial_balance

    def __gt__(self, other):
            return self.__initial_balance < other.__initial_balance


class Point:

    def __init__(self,x,y) -> None:

        if not isinstance(x, int | float) or not isinstance(y, int | float):
            raise TypeError("X and Y have to be type of intigers or floats ")
        self.x = x
        self.y = y

    def  __repr__(self) -> str:
        return f" X:{self.x}, Y:{self.y}"

    def move(self, dx, dy):
        if not isinstance(dx, int | float) or not isinstance(dy, int | float):
                    raise TypeError("dy and dx have to be type of intigers or floats ")
        self.x += dx
        self.y += dy

    @property
    def as_tuple(self) -> tuple:
        return (self.x,self.y)




class Rectangle:
        # lbc - left bottom corner, rtc - right top corner
    def  __init__(self, lbc:Point, rtc:Point) -> None:
        if not isinstance(lbc, Point) or not isinstance(rtc, Point):
            raise TypeError("lbc [left bottom corner] and rtc [right top corner] have to be objects of Point class.")
        #sprawdzam prawą stronę
        if not rtc.x > lbc.x and not rtc.y > lbc.y: 
            raise TypeError("rtc must be further left than lbc and further top than lbc")
        self.lbc = lbc
        self.rtc = rtc
        self.width = rtc.x - lbc.x
        self.height = rtc.y - lbc.y
        self.area = self.width * self.height
        self.perimeter = (self.width + self.height)*2

    def contains(self,point:Point) -> bool:
        if (point.y > self.lbc.y < self.rtc.y) and (point.x > self.lbc.x < self.rtc.x):
            return True
        else:
            return False





class Address2:
    def __init__(self, postal_code:str, city:str, street:str, house_number:str) -> None:

        validate_non_empty_strigs(
            postal_code=postal_code,
            city=city,
            street=street,
            house_number=house_number
        )

        self.postal_code = postal_code
        self.city = city
        self.street = street
        self.house_number = house_number

            
    def to_dict(self) -> dict:
        dict_summary = {
            "postal_code" : self.postal_code,
            "city" : self.city,
            "street" : self.street,
            "house_number": self.house_number
        }
        return dict_summary


class Customer:

    def __init__(self, customers_name, address:Address2) -> None:
        if not isinstance(customers_name, str):
            raise TypeError("Customer's name has to be type of string.")
        self.customers_name = customers_name
        if not isinstance(address, Address2):
            raise TypeError("Address has to be type of class Address2")
        self.address = address

    def __repr__(self) -> str:
        return f"{self.customers_name}"
    def to_dict(self) -> dict:
            dict_summary = {
                "Customer's name": self.customers_name,
                "Customer's Address": {
                    "postal_code" : self.address.postal_code,
                    "city" : self.address.city,
                    "street" : self.address.street,
                    "house_number": self.address.house_number
                }
            }
            return dict_summary



class Order:

    def __init__(self, customer:Customer, products_list:list) -> None:
        if not isinstance(customer, Customer):
            raise TypeError("Customer has to be type of class Customer")
        self.customer = customer
        if not isinstance(products_list, list):
            raise TypeError("Products list has to be type of list")
        self.products_list = products_list

        for product in products_list:
            validate_single_string_input(product[0])
            if not isinstance(product[1], int | float) or not product[1] > 0:
                raise TypeError("Price of product has to be type of intiger or float and cannot be negative.")
            if not isinstance(product[2], int) or not product[2] > 0:
                raise TypeError("QTY of product has to be declared as intiger and cannot be negative")

    def total_price(self):
        total_price = 0
        for product in self.products_list:
            total_price += product[1] * product[2]
        return total_price

    def add_product(self, products_name:str, price:float | int, qty:int):
        validate_single_string_input(products_name)
        if not isinstance(products_name, str):
            raise ValueError("Product's name has to be string type")
        if not isinstance(price, int | float) or not price > 0:
            raise TypeError("Price of product has to be type of intiger or float and cannot be negative.")
        if not isinstance(qty, int) or not qty > 0:
            raise TypeError("QTY of product has to be declared as intiger and cannot be negative")
        self.products_list.append((products_name, price, qty))

    def get_expensive_products(self, more_than_price):
        more_than_price_list = []
        for product in self.products_list:
            if product[1] >= more_than_price:
                more_than_price_list.append(product)
        return more_than_price_list

    def to_dict(self):
        dict_summary = {
            "Customer": self.customer,
            "Products": [product for product in self.products_list],
            "Total_price": self.total_price()
        }
        return dict_summary


class Employee:

    def __init__(self, employees_name, monthly_salary) -> None:
        validate_single_string_input(employees_name)
        if not isinstance(monthly_salary, int | float) or not monthly_salary > 0:
            raise TypeError("Employee's monthy salary has to be declared as intiger or float type and must be positive number")
        self.employees_name = employees_name
        self.__monthly_salary = monthly_salary

    def salary(self) -> int | float:
        return self.__monthly_salary

    def give_raise(self, raise_amount):
        if raise_amount > 0:
            self.__monthly_salary += raise_amount
        else:
            raise ValueError("Raise amount have to be positive number and greater than 0")

    def calculate_bonus(self) -> int | float:
        return self.__monthly_salary * 0.05



class Manager(Employee):

    def __init__(self, employees_name, monthly_salary, departament_title, employees_under) -> None:
        validate_single_string_input(employees_name)
        validate_single_string_input(departament_title)
        self.departament_title = departament_title
        if not isinstance(monthly_salary, int | float) or not monthly_salary > 0:
            raise TypeError("Employee's monthy salary has to be declared as intiger or float type and must be positive number")
        if not isinstance(employees_under, int) or not employees_under > 0:
            raise TypeError("Manager has to own at least 1 employee under itself and it has to be intiger type of input")
        self.employees_under = employees_under
        super().__init__(employees_name, monthly_salary)

    def calculate_bonus(self) -> int | float:
        return round(super().calculate_bonus() * 2  + (100 * self.employees_under),2)

class Developer(Employee):

    def __init__(self, employees_name, monthly_salary, known_technologies:list) -> None:
        validate_single_string_input(employees_name)
        if not isinstance(monthly_salary, int | float) or not monthly_salary > 0:
            raise TypeError("Employee's monthy salary has to be declared as intiger or float type and must be positive number")
        if not isinstance(known_technologies, list):
            raise TypeError("Developer's known technologies have to be a list type")
        for tech in known_technologies:
            validate_single_string_input(tech)
        self.known_technologies = known_technologies
        super().__init__(employees_name, monthly_salary)

    def add_technology(self, technology):
        validate_single_string_input(technology)
        if technology not in self.known_technologies:
            self.known_technologies.append(technology)
        else:
            raise ValueError("Technology already known")


    def calculate_bonus(self) -> int | float:
        return round((super().calculate_bonus() * 1.4) + (200*len(self.known_technologies)),2)


class Book3:
    def __init__(self,book_title:str, book_author:Author, relase_date:int, is_book_rented:bool) -> None:

        validate_single_string_input(book_title)
        validate_single_string_input(book_author.name)
        validate_single_string_input(book_author.surname)
        if not isinstance(relase_date, int) and relase_date > 0:
            raise ValueError("Relase date has to be a number")
        if not isinstance(is_book_rented, bool):
            raise TypeError("Book rented status has to be boolean type")
        self.book_title = book_title
        self.book_author = book_author
        self.relase_date = relase_date
        self.is_book_rented = is_book_rented

    def __repr__(self) -> str:
        return f"Book info: {self.book_title}, {self.relase_date} | Author: {self.book_author.name} {self.book_author.surname} | Is book being rented: {self.is_book_rented}"

    def to_dict(self) -> dict:
        book_to_dict = {
            "book_title" : self.book_title,
            "book_author" : {
            "Author's name" : self.book_author.name,
            "Author's surname" : self.book_author.surname,
        },
        "relase_date" : self.relase_date,
        "is book rented" : self.is_book_rented

        }
        return book_to_dict

class User:

    def __init__(self, users_name:str, limit_book_rent:int) -> None:
        validate_single_string_input(users_name)
        if not isinstance(limit_book_rent, int) or not limit_book_rent > 0:
            raise ValueError("Limit book rent has to be intiger type and cannot be negative or 0 (at least 1)")
        self.users_name = users_name
        self.limit_book_rent = limit_book_rent
        self.list_of_rented_books = []


class Library2(Library):
    def __init__(self) -> None:
        self.books = []
        self.registered_users = []

    def register_user(self, user:User):
        if not isinstance(user, User):
            raise TypeError("User has to be object of User class")
        if user in self.registered_users:
            raise ValueError("User already exists as registered")
        self.registered_users.append(user)


    def borrow_book(self, user:User, book:Book3):
        if not user in self.registered_users:
            raise ValueError("User is not registered. Register user and then try again.")
        if not book in self.books:
            raise ValueError("Book doesn't exist in library's book list.")
        if book.is_book_rented == True:
            raise ValueError("Book is already rented. Try to rent another book or wait till this book is returned.")
        if len(user.list_of_rented_books) >= user.limit_book_rent:
            raise ValueError("This user has reached its limit of rented books and cannot borrow another one.")
        book.is_book_rented = True
        user.list_of_rented_books.append(book)

    def return_book(self, user:User, book:Book3):
        if not book in user.list_of_rented_books:
            raise ValueError("This user doesn't have that book rented.")
        user.list_of_rented_books.remove(book)
        book.is_book_rented = False












