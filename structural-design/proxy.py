'''
    The Proxy design pattern is a structural pattern that provides a surrogate or proxy for another object
    to control access to it. This pattern is useful for performing operations before or after interacting
    with the real object, without clients needing to be aware of this intermediation.
'''

class Document:
    def __init__(self, content):
        self.content = content

    def display(self):
        print(f"Displaying document with content: {self.content}")

class DocumentProxy:
    def __init__(self, document, user):
        self.document = document
        self.user = user

    def display(self):
        if self.user.has_permission('view'):
            self.document.display()
        else:
            print("You do not have permission to view the document.")

class User:
    def __init__(self, permissions):
        self.permissions = permissions

    def has_permission(self, permission):
        return permission in self.permissions

doc = Document("Some confidential content")
user = User(["view"])
proxy = DocumentProxy(doc, user)
proxy.display() # Displaying document with content: Some confidential content

user_without_permission = User([])
proxy_no_permission = DocumentProxy(doc, user_without_permission)
proxy_no_permission.display() # You do not have permission to view the document.