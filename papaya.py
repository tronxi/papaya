import maude
import sys

def main(filename, debug=False):
    programFile = open(filename, "r").read()
    system = " < system : System | { none | print(\"\\0\"); ${program} println(\"\\0\"); } >"
    generatedSystem = system.replace("${program}", programFile)
    maude.init()
    maude.load("src/loads.maude")
    result = maude.getModule('SEMANTICS').parseTerm(generatedSystem).erewrite()
    if debug:
        print("\n\nResult:")
        print(result)

if __name__ == "__main__":
    debug = False
    if len(sys.argv) > 2 and sys.argv[2] == "--debug":
        debug = True
    main(sys.argv[1], debug)