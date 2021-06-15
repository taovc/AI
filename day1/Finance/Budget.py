class Budget:
    _transactions = []
    def add_transactions(self, list):
        Budget._transactions.append(list[0])
        Budget._transactions.append(list[1])
        Budget._transactions.append(list[2])
    def show_transactions(self):
        print "You received", Budget._transactions[0], "euros"
        print "You received", Budget._transactions[1], "euros"
        print "You spent", -Budget._transactions[2], "euros"