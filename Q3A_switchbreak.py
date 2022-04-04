
# get module code = CSC1009
module = "CSC1009"

# switch case of what the module name is given a module code
match module:
    case "CSC1006":
        print("Mathematics 2")
    case "CSC1007":
        print("Operating Systems")
    case "CSC1008":
        print("Data Structures and Algorithms")
    case "CSC1009":
        print("Object Oriented Programming")
    case "CSC1010":
        print("Computer Networks")
    case _:
        print("Unknown Module")

print("Switch Exited")