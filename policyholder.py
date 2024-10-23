# Define a policy holder class
class Policyholder:
    def __init__(self, policyholder_id, fname, lname, address, status='Active'):
        self.policyholder_id = policyholder_id
        self.fname = fname
        self.lname = lname
        self.email = fname + '.' + lname + '@email.com'
        self.address = address
        self.status = status

    def register(self):
        pass

    def suspend(self):
        pass

    def reactivate(self):
        pass

