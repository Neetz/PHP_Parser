import ply.lex as lex
import argparse
import re
import sys
parser = argparse.ArgumentParser()
parser.add_argument('-F','--file')
args = parser.parse_args()
F=args.file
if F is None:
	print("ENTER THE INPUT")
	print("ENTER eof AT LAST...")
	buffer = []
	while True:
		print("> ", end="")
		line = input()
		if line == "eof":
			break
		buffer.append(line)
	all = "\n".join(buffer)

else:
	try:
		f = open(args.file)
		all = f.read()
		f.close()
	except FileNotFoundError:
		print("Entered File is not found")
		sys.exit(1)
tokens=['START','DECIMAL','REAL','ID','RESERVED','PRINTSTATEMENT','END','STRINGVARIABLE']
reserved={
'abstract':'ABSTRACT','and':'AND','as':'AS','break':'BREAK','callable':'CALLABLE','case':'CASE',
'catch':'CATCH','class':'CLASS','clone':'CLONE','const':'CONST','continue':'CONTINUE',
'declare':'DECLARE','default':'DEFAULT','do':'DO','echo':'ECHO','else':'ELSE','elseif':'ELSEIF',
'enddeclare':'ENDDECLARE','endfor':'ENDFOR','endforeach':'ENDFOREACH','endif':'ENDIF',
'endswitch':'ENDSWITCH','endwhile':'ENDWHILE','extends':'EXTENDS','final':'FINAL','for':'FOR',	'foreach':'FOREACH','function':'FUNCTION','global':'GLOBAL','goto':'GOTO','if':'IF',
'implements':'IMPLEMENTS','include':'INCLUDE','include_once':'INCLUDE_ONCE','instanceof':'INSTANCEOF',
'insteadof':'INSTEADOF','interface':'INTERFACE','namespace':'NAMESPACE','new':'NEW','or':'OR',
'print':'PRINT','private':'PRIVATE','protected':'PROTECTED','public':'PUBLIC','require':'REQUIRE',
'require_once':'REQUIRE_ONCE','return':'RETURN','static':'STATIC','switch':'SWITCH','string':'STRING','throw':'THROW','trait':'TRAIT','try':'TRY','use':'USE','var':'VAR','while':'WHILE','xor':'XOR',
'yield':'YIELD','array':'ARRAY','die':'DIE','empty':'EMPTY','eval':'EVAL','EXIT':'EXIT','isset':'ISSET','list':'LIST','unset':'UNSET'		
}

tokens += list(reserved.values())
def t_START(t):
	r'\<\?(php)'
	return t
def t_END(t):
	r'\?\>'
	return t
def t_DECIMAL(t):
	r'(\d+)(\.)\d+("E"("+"|"-")?\d+)?'
	print(t.value+'\t:\t'+t.type)
	return t
def t_REAL(t):
	r'\d+("E"("+"|"-")?\d+)?'
	print(t.value+'\t:\t'+t.type)
	return t
def t_STRINGVARIABLE(t):
	r'(\'|\")(.*)(\'|\")'
	print(t.value+'\t:\t'+t.type)
	return t
def t_PRINTSTATEMENT(t):
	r'(echo|print)(\s*)(\'|\")(.*)(\'|\")'
	print(t.value+'\t:\t'+t.type)
	return t
def t_ID(t):
	r'[\$][a-zA-Z_][a-zA-Z_0-9]*'
	print(t.value+'\t:\t'+t.type)
	return t
def t_RESERVED(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	if t.value in reserved: # Check for reserved words
		t.type = reserved[ t.value ]
		print(t.value+'\t:\t'+t.type)
		return t
	else:
		print(t.value+" is INVALID at line no."+str(t.lexer.lineno))
    
def t_COMMENT(t):
	r'\#.*|\/\*((.|\n)*?)\*\/|\/\/.*'
	t.lexer.lineno += t.value.count('\n')
	pass
def t_ADDASSIGN(t):
	r'\+(\s*)\=' 
	print(t.value+'\t:\t'+t.type)
def t_SUBASSIGN(t):
	r'-(\s*)\=' 
	print(t.value+'\t:\t'+t.type)
def t_MULASSIGN(t):
	r'\*(\s*)\=' 
	print(t.value+'\t:\t'+t.type)
def t_DIVASSIGN(t):
	r'\/(\s*)\=' 
	print(t.value+'\t:\t'+t.type)
def t_MODASSIGN(t):
	r'\%(\s*)\=' 
	print(t.value+'\t:\t'+t.type)
def t_CONCATASSIGN(t):
	r'\.(\s*)\=' 
	print(t.value+'\t:\t'+t.type)
def t_INCREEMENT(t):
	r'\+\+' 
	print(t.value+'\t:\t'+t.type)
def t_DECREEMENT(t):
	r'--' 
	print(t.value+'\t:\t'+t.type)
def t_PLUS(t):
	r'\+' 
	print(t.value+'\t:\t'+t.type)
def t_MINUS(t):		
	r'-'
	print(t.value+'\t:\t'+t.type)
def t_MULTIPLICATION(t):		
	r'\*'
	print(t.value+'\t:\t'+t.type)
def t_DIVISION(t):		
	r'\/'
	print(t.value+'\t:\t'+t.type)
def t_MODULOS(t):		
	r'\%'
	print(t.value+'\t:\t'+t.type)
def t_IDENTICAL(t):		
	r'\=\=\='
	print(t.value+'\t:\t'+t.type)
def t_EQUAL(t):		
	r'\=\='
	print(t.value+'\t:\t'+t.type)
def t_ASSIGNMENT(t):		
	r'\='
	print(t.value+'\t:\t'+t.type)
def t_NOTIDENTICAL(t):		
	r'\!\=\='
	print(t.value+'\t:\t'+t.type)
def t_NOTEQUAL(t):		
	r'\!\=|\<\>'
	print(t.value+'\t:\t'+t.type)
def t_CONCAT(t):
	r'\.' 
	print(t.value+'\t:\t'+t.type)
def t_RIGHTSHIFT(t):
	r'\>\>'
	print(t.value+'\t:\t'+t.type)
def t_LEFTSHIFT(t):
	r'\<\<'
	print(t.value+'\t:\t'+t.type)
def t_GE(t):		
	r'\>\='
	print(t.value+'\t:\t'+t.type)
def t_LE(t):		
	r'\<\='
	print(t.value+'\t:\t'+t.type)
def t_GT(t):		
	r'\>'
	print(t.value+'\t:\t'+t.type)
def t_LT(t):		
	r'\<'
	print(t.value+'\t:\t'+t.type)
def t_QUESTION(t):		
	r'\?'
	print(t.value+'\t:\t'+t.type)
def t_SEMICOLON(t):
	r'\;'
	print(t.value+'\t:\t'+t.type)
def t_LPAREN(t):
	r'\('
	print(t.value+'\t:\t'+t.type)
def t_RPAREN(t):
	r'\)'
	print(t.value+'\t:\t'+t.type)
def t_LBRACKET(t):
	r'\['
	print(t.value+'\t:\t'+t.type)
def t_RBRACKET(t):
	r'\]'
	print(t.value+'\t:\t'+t.type)
def t_LBRACE(t):
	r'\{'
	print(t.value+'\t:\t'+t.type)
def t_RBRACE(t):
	r'\}'
	print(t.value+'\t:\t'+t.type)
def t_COLON(t):
	r'\:'
	print(t.value+'\t:\t'+t.type)
def t_COMMA(t):
	r'\,'
	print(t.value+'\t:\t'+t.type)
def t_QUOTES(t):
	r'\'|\"'
	print(t.value+'\t:\t'+t.type)
def t_LOGICALAND(t):
	r'\&\&'
	print(t.value+'\t:\t'+t.type)
def t_BITWISEAND(t):
	r'\&'
	print(t.value+'\t:\t'+t.type)
def t_LOGICALOR(t):
	r'\|\|'
	print(t.value+'\t:\t'+t.type)
def t_BITWISEOR(t):
	r'\|'
	print(t.value+'\t:\t'+t.type)
def t_BITWISEXOR(t):
	r'\^'
	print(t.value+'\t:\t'+t.type)
def t_BITWISENOT(t):
	r'\~'
	print(t.value+'\t:\t'+t.type)
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
def t_error(t):
	print("Illegal character %s at line no: %d" % (repr(t.value[0]),t.lexer.lineno))
	#l=len(t.value)
	t.lexer.skip(1)
t_ignore = ' \t'
pattern="\<\?(php)"
if re.match(pattern,all):
	pass
else:
	print("ERROR: Programme should start from <?php")
print("THE TOKENS PRODUCED ARE:")
print('-'*50)
lexer=lex.lex()
lexer.input(all)
for t in lexer:
	pass
print('-'*50)
pattern="(.|\n)*\?\>$"
if re.match(pattern,all):
	pass
else:
	print("ERROR: Programme should end with ?>")
