from abc import ABC, abstractmethod

'''
    The Factory Method is one of the well-known design patterns in software engineering, 
    used to deal with the problem of creating objects without specifying the exact class of object that will be created. 
    This is achieved by defining an interface for creating an object, 
    but allowing subclasses to alter the type of objects that will be created. Essentially, 
    the Factory Method pattern provides a way to encapsulate the instantiation of a class.
'''

# Product Interface
class Document(ABC): # Abstract method 
    @abstractmethod
    def create(self): # Declares an abstract method create. This method must be implemented by any subclass of Document to define how the document is created.
        pass

# Concrete Products
class WordDocument(Document):
    def create(self):
        print("Creating a Word document.")

class ExcelDocument(Document):
    def create(self):
        print("Creating an Excel document.")

class PDFDocument(Document):
    def create(self):
        print("Creating an PDF document.")

# Creator Class
class Application(ABC):
    @abstractmethod
    def create_document(self):
        pass
    def new_document(self): 
        doc = self.create_document() # A concrete method that creates a new document by calling create_document to obtain an instance of Document
        doc.create() # and then calling the document's create method.

# Concrete Creators
class WordApplication(Application):
    def create_document(self):
        return WordDocument()

class ExcelApplication(Application):
    def create_document(self):
        return ExcelDocument()

class PDFApplication(Application):
    def create_document(self):
        return PDFDocument()

app = WordApplication()
app.new_document()

app = ExcelApplication()
app.new_document()

app = PDFApplication()
app.new_document()
