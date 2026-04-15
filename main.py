#will I be able to understand class
class SimpleHash:
    def hash(self, text):
        h = 0
        for ch in text:
            h = (h * 31 + ord(ch)) % 1000000007
        return str(h) # i don't like prep test
class Acc:
    def __init__(self, username, password, app):
        self.username = username
        self.hasher = SimpleHash()
        self.password = self.hasher.hash(password)
        self.app = app
    def show(self):
        print("App:", self.app, "| Username:", self.username)
class Vault:
    def __init__(self):
        self.accounts = []
    def add_account(self, username, password, app):
        acc = Acc(username, password, app)
        self.accounts.append(acc)
        print("Account added!")
    def view_accounts(self):
        if len(self.accounts) == 0:
            print("No accounts stored.")
            return
        for acc in self.accounts:
            acc.show()
    def find_account(self, app):
        for acc in self.accounts:
            if acc.app == app:
                print("Found:")
                acc.show()
                return
        print("Not found")
    def delete_account(self, app):
        for i in range(len(self.accounts)):
            if self.accounts[i].app == app:
                del self.accounts[i]
                print("Deleted")
                return
        print("Not found")
class Auth:
    def __init__(self):
        self.hasher = SimpleHash()
        self.master_hash = None
        self.setup()
    def setup(self):
        master = input("Set master password: ")
        self.master_hash = self.hasher.hash(master)
    def login(self):
        attempt = input("Enter master password: ")
        if self.hasher.hash(attempt) == self.master_hash:
            print("Access granted\n")
            return True
        else:
            print("Access denied")
            return False
class App:
    def __init__(self):
        self.auth = Auth()
        self.vault = Vault()

    def run(self):
        if not self.auth.login():
            return
        while True:
            print("\n1. Add Account")
            print("2. View Accounts")
            print("3. Find Account")
            print("4. Delete Account")
            print("5. Exit")
            choice = input(">> ")
            if choice == "1":
                app = input("App: ")
                username = input("Username: ")
                password = input("Password: ")
                self.vault.add_account(username, password, app)
            elif choice == "2":
                self.vault.view_accounts()
            elif choice == "3":
                app = input("App to find: ")
                self.vault.find_account(app)
            elif choice == "4":
                app = input("App to delete: ")
                self.vault.delete_account(app)
            elif choice == "5":
                print("Goodbye")
                break
            else:
                print("Invalid choice")
program = App()
program.run()
#will be indented back after understanding
#i did not write this code well mostly yes but some was given to me by my academi
