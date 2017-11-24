#
#	CPU Generator
#
def convert(x):
	x = x.replace("!","PLING").replace("@","AT").replace("+","PLUS")
	x = x.replace("/","SLASH").replace(">","GREATER").replace(";","SEMICOLON")
	x = x.replace("=","EQUALS").replace("[","LSQB").replace("]","RSQB")
	x = x.replace("-","MINUS").replace("<","LESS").replace("?","QUESTION")
	x = x.replace("*","STAR")
	return x

tempAddress = 0x1000
codeAddress = 0x1200
dictAddress = 0x0100 

src = [x.replace("\t"," ") for x in open("corewords.def").readlines()]
src = [x if x.find("//") < 0 else x[:x.find("//")] for x in src]
src = [x.strip() for x in src]
src = [x.strip() for x in (" ".join(src)).split("{{") if x.strip() != ""]

keyWords = []
keyWordCode = {}
keyWordIdentifier = {}

for l in src:
	elements = l.split("}}")
	word = elements[0].strip().lower();
	code = elements[1]+";break;".replace(";;"," ")
	keyWords.append(word)
	keyWordCode[word] = code 
	keyWordIdentifier[word] = "KW_"+convert(word.upper())

h = open("__vmcase.h","w")
for w in keyWords:
	h.write("case {0}:\n    {1}\n".format(keyWordIdentifier[w],keyWordCode[w]))
h.close()

h = open("__vminclude.h","w")
h.write("#ifndef __VMI\n#define __VMI\n\n")
h.write("#define SYS_ADDR_TEMP (0x{0:04x})\n".format(tempAddress))
h.write("#define SYS_ADDR_CODEBASE (0x{0:04x})\n".format(codeAddress))
h.write("#define SYS_ADDR_DICTBASE (0x{0:04x})\n".format(dictAddress))
for i in range(0,len(keyWords)):
	h.write("#define {0} ({1})\n".format(keyWordIdentifier[keyWords[i]],i))	
h.write("#define KW_COUNT ({0})\n".format(len(keyWords)))
h.write("\n#ifdef MNEMONICS\n")
h.write("static const char *_mnemonics[] = { \n")
h.write(",".join(['"'+x+'"' for x in keyWords]))
h.write("\n};\n#endif\n")
h.write("#endif\n")
h.close()

wordList = ",".join(['"'+x+'"' for x in keyWords])
h = open("vmcompilerinfo.py","w")
h.write("#\n# Generated by generate.py \n#\n")
h.write("class VMCompilerInfo:\n")
h.write("  def getWordList(self):\n")
h.write("    return ["+wordList+"]\n")
h.write("  def getDictionaryBase(self):\n")
h.write("    return 0x{0:04x}\n".format(dictAddress))
h.write("  def getCodeBase(self):\n")
h.write("    return 0x{0:04x}\n".format(codeAddress))
h.write("  def getBaseLoadAddress(self):\n")
h.write("    return 0x0000\n")


