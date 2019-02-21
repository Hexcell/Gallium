from lark import Lark
from lark.indenter import Indenter

class PostLex(Indenter):
	NL_type = "_NEWLN"
	def process(self, stream):
		comment = False
		for t in stream:
			print(t, t.type)
			yield t

parser = Lark(open("grammar.lark", "r").read(), parser="lalr", postlex=PostLex())

test = """
struct Name {
  name: str;
}


var test: int = 32;
if (test == 2) {
	var x: int = 23;

	var my_struct: struct<MyStruct>;
}
/*
else{
	var y: str = "asd";
}
*/

func main(ashdhd: int) {

}
"""

result = parser.parse(test)
print(result.pretty())