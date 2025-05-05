class InformationManagementExpertSystem:
    def __init__(self):
        self.data = {}

    def add_information(self , key , value):
        self.data[key] = value
        print(f"information '{key}' added siccessfully")

    def get_information(self , key):
        if (key in self.data):
            return self.data[key]
        else:
            print(f"information {key} not found")
            return None
    
    def remove_information(self , key):
        if (key in self.data):
            del self.data[key]
            print(f"information {key} removed seccessfully")
        else:
            print(f"information {key} not found ")
    
    def display_all_information(self):
        if self.data:
         print("All information:")
         print(self.data)  # Directly print the dictionary
        else:
         print("No information available.")


expert_system = InformationManagementExpertSystem()
expert_system.add_information("name" , "prem")
expert_system.add_information("age" , 22)
expert_system.display_all_information()
print(expert_system.get_information("name"))
expert_system.remove_information("age")
expert_system.display_all_information()