class Client(Person):
    def __init__(self, first_name, last_name, address, cell_phone, email, gender):
        super().__init__(first_name, last_name)
        self.address = address
        self.cell_phone = cell_phone
        self.email = email
        self.gender = gender
    
    def __str__(self):
        return f"Client({super().__str__()}, address={self.address}, cell_phone={self.cell_phone}, email={self.email}, gender={self.gender})"