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




p1_address = Address("15-743", "Białystok", "Wierzbowa", "5A")
p1_job = Job("Orange", "Salesman", 8000.00)
person1 = Person("Daniel", 27, p1_address, p1_job)

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




author1 = Author("Adam", "Mickiewicz")
author2 = Author("Bolesław", "Prus")





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


book1 = Book("Dziady", author1, 1821, 250)
book2 = Book("Dziady 2", author1, 1823, 255)
book3 = Book("Lalka", author2, 1887, 600)


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




library = Library("World of Books")
library.add_book(book2)
library.add_book(book3)
library.add_book(book1)

books_sorted = library.sort_books_by_year()
books_sorted_by_pages = library.sort_books_by_pages_desc()
title_year_pairs = library.get_title_year_pairs()
sorted_title_year_pairs = library.sort_title_year_pairs()
statistics = library.get_statistics()
library_to_dict = library.to_dict()


