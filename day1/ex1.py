def show_transactions (list):
    print "You received", list[0], "euros"
    print "You received", list[1], "euros"
    print "You spent", -list[2], "euros"
    return

transactions = [512 , 42.08 , -12]
show_transactions ( transactions )