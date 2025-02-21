class Automata:
    def __init__(self, Σ, δ, F):
        self.Σ = list(Σ)  # Convert the alphabet into a list
        self.δ = δ  
        self.s = 0  
        self.F = set(F)  


    def getEquivalentStates(self):
        states = len(self.δ)
        print(self.δ)
        table = [[False] * states for _ in range(states)]  # Initialize the table with all False, create a nxn table
        
        change = False
        # Mark the pairs {p, q} if p is final and q is not, or vice versa
        for i in range(states):
            for j in range(states):
                if (i in self.F) != (j in self.F):
                    table[i][j] = True 
                    change = True 

        print("\nInitial minimization table:")
        for row in table:
            print(row)

        while(change):
            change = False
            for i in range(1 , states):
                for j in range(states):
                    if i > j and not table[i][j]:
                        for lexema in range(len(self.Σ)):
                            p = self.δ[j][lexema + 1]
                            q = self.δ[i][lexema + 1]
                            if p != q and table[q][p] == True:
                               table[i][j] = True
                               change = True
                            
          
            


        # Identifico los states equivalentes
        pares_equivalentes = []
        for i in range(states):
            for j in range(i):
                if not table[i][j]:  # Si no está marcado, son states son equivalentes
                    pares_equivalentes.append((j,i ))  

        return pares_equivalentes

# Read the file and give it the alias "file"
with open("example.txt", "r") as file:
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
    
for idx, automata in enumerate(cases):
    equivalentes = automata.getEquivalentStates()
    print("states equivalentes:", " ".join(f"({p},{q})" for p, q in equivalentes))