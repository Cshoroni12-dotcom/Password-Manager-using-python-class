class SimpleHash:
    def hash(self, text):
        h = 0
        for ch in text:
            h = (h * 31 + ord(ch)) % 1000000007
        return str(h)
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
