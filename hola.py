class bank: 
    def __init__(self, name):
        self.name = name
        self.clients = []
        self.money = 0.0

class client:
    def __init__(self,client_id, name):
        self.client_id = client_id
        self.name = name
        self.client_accounts = []
        self.client_total_money = 0.0


class client:
    def __init__(self,account_id, client_id):
        self.account_id = account_id
        self.client = client_id
        self.account_money = 0.0
