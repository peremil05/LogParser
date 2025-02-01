from sys import argv
#from re import *

def init(scriptName):
    global script
    with open(scriptName) as script:
        # Get raw script without comments (this assumes comments are on their own line) and remove any newline characters.
        script = [line.replace('\n', '') for line in script.readlines() if "//" not in line] 

    # Have input and out be on lines 1 and 2 as standard?
    global inputPath
    global outputPath
    foundInput = False
    foundOutput = False
    for line in script:
        if "in = " in line:
            inputPath = line.split('=')[1]
            foundInput = True
        if "out = " in line:
            outputPath = line.split('=')[1]
            foundOutput = True
        if foundInput and foundOutput:
            return

if __name__ == "__main__":
    script = []
    inputPath = ""
    outputPath = ""
    init(argv[1])
    print(f"Input: {inputPath}\nOutput: {outputPath}")

'''
script = open(argv[1], "r")

content = script.read()

print(content)
'''
