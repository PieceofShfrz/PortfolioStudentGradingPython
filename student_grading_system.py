class MidtermGrade():
    """Constructor to initialize midterm grade attributes."""
    def __init__(self, npm, name, grade):
        self.npm = npm
        self.name = name
        self.grade = grade
    
    def show_midterm_grade(self):
        """Display midterm grade information."""
        print("The student " + self.name + " with npm " + 
              str(self.npm) + " has a midterm grade of " + str(self.grade)
                + ".")
        
        
class FinalGrade(MidtermGrade):
    def __init__(self, npm, name, grade):
        """Constructor for FinalGrade, inheriting from the MidtermGrade class"""
        super().__init__(npm, name, grade)
    
    def show_final_grade(self):
        """Display midterm grade information."""
        print("The student " + self.name + " with npm " + 
              str(self.npm) + " has a final grade of " + str(self.grade)
                + ".")


#Input midterm accreditation data
midterm_accreditation_data = {}
midterm_input_active = False #Set to false if we want to stop inputting
midterm_save_active = True #set to True if we want to pull out the data

#Function to save accreditation data to a file
def save_midterm_accreditation_data(filename, data):
    try:
        with open (filename, 'w') as file:
            for name, accreditation in data.items():
                file.write(f"{name} has an accreditation of {accreditation}\n")
        return True #Return true if saving is successful
    except Exception as e:
        print(f"Error saving data: {e}")
        return False  # Return False if there's an error

#Input and examine the accreditation
while midterm_input_active:
    name = input("\nEnter the name: ")
    try:
        grade = int(input("What is grade? "))
    except ValueError:
        #Handle invalid input for grade
        print("Invalid input. Please enter a valid grade")
        continue
    
    #Determine accreditation based on the grade
    if  grade >= 85:
        accreditation = 'A'
    elif grade >= 75:
        accreditation = 'B'
    else:
        accreditation = 'C'
    
    #midterm_accreditation_data [name] = accreditation
    midterm_accreditation_data[name] = accreditation

    repeat = input("Would you like to input again? ")
    if repeat.lower() == 'no':
        midterm_input_active = False
        #Save the accreditation data to a file if we stop inputting
        midterm_save_active = save_midterm_accreditation_data('midterm_accreditation.txt', midterm_accreditation_data)
    
# Load and display accreditation data to the terminal
print("\n===================Results of Midterm Accreditation===================")
if midterm_save_active:
    with open('midterm_accreditation.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
else:
    print("Data was not saved")



#Input final accreditation data
final_accreditation_data = {}
final_input_active = False
final_save_active = True

#Function to save accreditation data to a file
def save_final_accreditation_data(filename, data):
    try:
        with open (filename, 'w') as file:
            for name, accreditation in data.items():
                file.write(f"{name} has an accreditation of {accreditation}\n")
        return True #Return true if saving is successful
    except Exception as e:
        print(f"Error saving data: {e}")
        return False  # Return False if there's an error

#Input and examine the accreditation
while final_input_active:
    name = input("\nEnter the name: ")
    try:
        grade = int(input("What is grade? "))
    except ValueError:
        #Handle invalid input for grade
        print("Invalid input. Please enter a valid grade")
        continue
    
    #Determine accreditation based on the grade
    if  grade >= 85:
        accreditation = 'A'
    elif grade >= 75:
        accreditation = 'B'
    else:
        accreditation = 'C'
    
    #midterm_accreditation_data [name] = accreditation
    final_accreditation_data[name] = accreditation

    repeat = input("Would you like to input again? ")
    if repeat.lower() == 'no':
        final_input_active = False
        #Save the accreditation data to a file if we stop inputting
        final_save_active = save_final_accreditation_data('final_accreditation.txt', final_accreditation_data)

print("\n===================Results of Final Accreditation===================")
if final_save_active:
    with open('final_accreditation.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
else:
    print("Data was not saved")























