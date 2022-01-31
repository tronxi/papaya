import maude
import sys

def main(filename):
    programFile = open(filename, "r").read()
    initialProgram = "print(\"\"); print(\"\"); print(\"\"); ${program}"
    generatedProgramFile = programFile.replace("${program}", initialProgram)
    system = " < system : System | { none | ${program} } >"
    generatedSystem = system.replace("${program}", generatedProgramFile)
    # print(generatedSystem)
    maude.init()
    maude.load("src/loads.maude")
    maude.getModule('SEMANTICS').parseTerm(generatedSystem).erewrite()

if __name__ == "__main__":
    main(sys.argv[1])