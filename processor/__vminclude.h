#ifndef __VMI
#define __VMI

#define SYS_ADDR_TEMP (0x1000)
#define SYS_ADDR_CODEBASE (0x1200)
#define SYS_ADDR_DICTBASE (0x0100)
#define KW_AT (0)
#define KW_CAT (1)
#define KW_PLING (2)
#define KW_CPLING (3)
#define KW_GREATERR (4)
#define KW_RGREATER (5)
#define KW_SEMICOLON (6)
#define KW_LSQBLITERALRSQB (7)
#define KW_LSQBBZERORSQB (8)
#define KW_LSQBHALTRSQB (9)
#define KW_LSQBNOPRSQB (10)
#define KW_PLUS (11)
#define KW_NAND (12)
#define KW_2SLASH (13)
#define KW_0EQUALS (14)
#define KW_LSQBTEMPRSQB (15)
#define KW_LSQBCODEBASERSQB (16)
#define KW_LSQBDICTIONARYRSQB (17)
#define KW_CURSORPLING (18)
#define KW_SCREENPLING (19)
#define KW_KEYBOARDAT (20)
#define KW_BLOCKREADAT (21)
#define KW_LSQBSTACKRESETRSQB (22)
#define KW_BLOCKWRITEPLING (23)
#define KW_0 (24)
#define KW_1 (25)
#define KW_2 (26)
#define KW_MINUS1 (27)
#define KW_DUP (28)
#define KW_DROP (29)
#define KW_SWAP (30)
#define KW_OVER (31)
#define KW_QUESTIONDUP (32)
#define KW_NOT (33)
#define KW_AND (34)
#define KW_OR (35)
#define KW_XOR (36)
#define KW_1PLUS (37)
#define KW_1MINUS (38)
#define KW_NEGATE (39)
#define KW_MINUS (40)
#define KW_2STAR (41)
#define KW_0LESS (42)
#define KW_PLUSPLING (43)
#define KW_LSQBEXECRSQB (44)
#define KW_LSQBNEXTRSQB (45)
#define KW_COUNT (46)

#ifdef MNEMONICS
static const char *_mnemonics[] = { 
"@","c@","!","c!",">r","r>",";","[literal]","[bzero]","[halt]","[nop]","+","nand","2/","0=","[temp]","[codebase]","[dictionary]","cursor!","screen!","keyboard@","blockread@","[stackreset]","blockwrite!","0","1","2","-1","dup","drop","swap","over","?dup","not","and","or","xor","1+","1-","negate","-","2*","0<","+!","[exec]","[next]"
};
#endif
#endif
