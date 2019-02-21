# Gallium
Gallium is a statically typed, compiled language written in Python.

### Progress
- [x] Define the grammar for the language
- [x] Write a competent lexer
- [ ] Write a post lexer using Lark
- [ ] Write a parser transformer (AST shit)
- [ ] Write a compiler (preferably with LLVM)
- [ ] Compile to C/native code
- [ ] Write a competent standard library

### Features
- variables and constants, `var name: str = "fabian"`
- `if`, `elif`, and `else` statements
- `for`, `foreach` and `while` loops
- functions
- `struct`'s

### Example
```
import io;

func main(args: str[]): int {
  // oh look, i'm a comment
  var name: str = "fabian";
  var age: int<32> = 18;

  io:print(name);
  io:print(age);
}
```