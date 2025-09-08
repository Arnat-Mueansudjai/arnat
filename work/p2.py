class PanValidator:
    def __init__(self, name, pan):
        self.name = name
        self.pan = pan

    def is_valid_pan(self):
        if len(self.pan) != 10:
            exit()
        first_five = self.pan[:5].isalpha()     
        middle_four = self.pan[5:9].isdigit()   
        last_one = self.pan[9].isalpha()        
        return first_five and middle_four and last_one

    def show_details(self):
        if self.is_valid_pan():
            print("Correct")
        else:
            print("Incorrect!")


name = input("Enter Name: ")
pan = input("Enter PAN: ")

user = PanValidator(name, pan)
user.show_details()
