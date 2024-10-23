# Define a policy holder class
class Policyholder:
    def __init__(self, policyholder_id, fname, lname, address, status='Active'):
        self.policyholder_id = policyholder_id
        self.fname = fname
        self.lname = lname
        self.email = f"{fname.lower()}.{lname.lower()}@email.com"
        self.address = address
        self.status = status

    @classmethod
    def register(cls, policyholder_id, fname, lname, address):
        """""
        class method to create a new policy holder
        """""
        return cls(policyholder_id, fname, lname, address)

    def suspend(self):
        if self.status == 'Active':
            self.status = 'Suspend'
            print(f"Policyholder {self.fname} {self.lname} has been suspended.")
        else:
            print(f"Policyholder {self.fname} {self.lname} is already suspended.")
    

    def reactivate(self):
        if self.status == 'Suspended':
            self.status = 'Active'
            print(f"Policyholder {self.fname} {self.lname} has been reactivated.")
        else:
            print(f"Policyholder {self.fname} {self.lname} is already active.")

