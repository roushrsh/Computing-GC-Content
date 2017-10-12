with open ("rosalind_gc.txt", "r") as myfile:  #import file
    s=myfile.read()

def calcGC(string): #method to calculate GC percent
    x=0
    y=0
    for i in string: #counts number of bases
        if (i=='C' or i=='G' or i == "T" or i == "A" or i == "U"):
            y = y+1
            if (i=='C' or i=='G'): #in the case that the base is a C or G, we count how many we have for calculation
                x=x+1
    return (float(x) / float(y) * 100) #does the math in a float for %GC

t = s.split(">") #split them by the > infront of Rosalind
text2bprintedRose, text2bprinted, currentText,currentTextRose ="","","","" #here we store what we're evaluating (the rosalind name, and the base list) as well as what currently has the highest GC content (both rosalind and base list)
percGC= 0 #place to store %GC

for x in t:  #going through list
    if "Rosalind" in x: #get rid of empty lists or errors
        currentTextRose = x[:13]  #we know the length is rosalind + _ + /d/d/d/d so we can take it
        currentText = x[13:] #take what remains as the bases
        if (calcGC(currentText) > percGC): #if the gc content is more, then we store
            percGC = calcGC(currentText)
            text2bprinted = currentText
            text2bprintedRose = currentTextRose #not needed tbqh. I've only put it if the bioinformatician would want to print the GC list
answerGC = str(round(percGC, 6))  #round down to 6 decimal places for error
print text2bprintedRose, answerGC #print answer to console
