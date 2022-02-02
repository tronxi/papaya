import maude
import sys

def main(filename, debug=False):
    programFile = open(filename, "r").read()
    initialProgram = "function 'main() { print(\"\"); print(\"\"); print(\"\"); "
    generatedProgramFile = programFile.replace("function 'main() {", initialProgram)

    system = " < system : System | { none | ${program} } > "
    generatedSystem = system.replace("${program}", generatedProgramFile)

    maude.init()
    maude.load("src/loads.maude")
    result,rewrites = maude.getModule('SEMANTICS').parseTerm(generatedSystem).erewrite()
    if debug:
        print("\nResult:")
        print(result)

if __name__ == "__main__":
    debug = False
    if len(sys.argv) > 2 and sys.argv[2] == "-d":
        debug = True
    main(sys.argv[1], debug)