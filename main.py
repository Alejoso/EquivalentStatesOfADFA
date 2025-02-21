class Automata:
    def __init__(self, Σ, δ, F):
        self.Σ = list(Σ)  # Convert the alphabet into a list
        self.δ = δ  
        self.s = 0  
        self.F = set(F)  

# Read the file and give it the alias "file"
with open("Documento.txt", "r") as file:
    lines = file.readlines()

# Extract number of automata
NumberOfAutomata = int(lines[0].strip())  
i = 1
cases = []

# Procces every automata
for _ in range(NumberOfAutomata):
    nLines = int(lines[i].strip())  #Get the numbre of states, then convert it into an int 
    Σ = lines[i+1].strip().split(" ")  # Get the alphabet, taking into account split for not getting empty spaces 
    F = list(map(int, lines[i+2].strip().split(" ")))  # Get final states 

    #Read the transition table
    δ = [list(map(int, lines[i+3+j].strip().split(" "))) for j in range(nLines)] #Convert the transition table data into an integer to create a matrix
    
    # Save the automata in the automata list
    cases.append(Automata(Σ, δ, F))

    # Increase the counter
    i = nLines + 3 + i
