class Book():

    def __init__(self,Title,author,num_pages):
        self.Title = Title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.Title} by {self.author}"

    def __eq__(self,other):
        return self.Title == other.Title and self.author == other.author

    def __lt__(self,other):
        return self.num_pages < other.num_pages

    def __add__(self,other):
        return self.num_pages + other.num_pages

    def __contains__(self,other):
        return other in self.Title

    def __getitem__(self,index):
        if index == "title":
            return self.Title
        elif index == "author":
            return self.author
        elif index == "num_pages":
            return self.num_pages
        else:
            raise 'not found'

book1 = Book("Python Programming","Kalathee",100)
book2 = Book("harry potter","J K",120)
book3 = Book("the king","Akash",166)
book4 = Book("the king","Akash",124)

print(book3)
print(book2)
print(book1)
print(book4==book3)
print(book4>book3)
print(book4<book3)
print(book4+book3)
print("king" in book3)
print("rowling" in book3)
print(book3['title'])
print(book3['author'])
