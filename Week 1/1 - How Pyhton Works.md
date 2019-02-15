<!-- STATICS -->
[pyhton_logo]: ../Static/Pics/python_logo_2.png "Pyhton Logo"
[pyhton_interpreter]: ../Static/Pics/python_interpreter.jpeg "Pyhton Interpreter"
[pyhton_interpreter_inside]: ../Static/Pics/interpreter_inside.png "Pyhton Interpreter White Box"
[parsetree]: ../Static/Pics/parsetree.png "Pars Tree"
[ast]: ../Static/Pics/ast.png "Pars Tree"
[pyexec]: ../Static/Pics/pyexec.png "How Python Works!"
<!-- END STATICS -->
![][pyhton_logo]
# How Python Works
## Pyhton Interpreter <a name="FN1">1</a>
![][pyhton_interpreter]
An interpreter is a kind of program that executes other programs. When you write a Python program, the Python interpreter reads your program and carries out the instructions it contains. In effect, the interpreter is a layer of software logic between your code and the computer hardware on your machine.

When the Python package is installed on your machine, it generates a number of components— minimally, an interpreter and a support library. Depending on how you use it, the Python interpreter may take the form of an executable program, or a set of libraries linked into another program. Depending on which flavor of Python you run, the interpreter itself may be implemented as a C program, a set of Java classes, or something else. Whatever form it takes, the Python code you write must always be run by this interpreter. And to enable that, you must install a Python interpreter on your computer.
+ CPython is the default interpreter for Python which is written in C programming language.
+ Jython is another popular implementation of python interpreter written using Java programming language.
+ PyPy is a Python interpreter implemented in a restricted statically-typed subset of the Python language called RPython. The interpreter features a just-in-time compiler and supports multiple back-ends (C, CLI, JVM). Thanks to its [Just-in-Time compiler](https://en.wikipedia.org/wiki/Just-in-time_compilation), Python programs often run faster on PyPy.
### Python’s view of interpreter <a name="FN1">2</a>
![][pyhton_interpreter_inside]
From the figure above, it can be inferred that interpreter is made up of two parts:
+ Compiler
+ Virtual machine 
#### Compiler
Compiler compiles your source code (the statements in your file) into a format known as byte code. Compilation is simply a translation step. 

Roughly, each of your source statements is translated into a group of byte code instructions.
##### Parse source code into a parse tree
Based on grammar rules of Python programming language, the source code is converted to a parse tree. Every node of the parse tree contains a part of your code.

**`14 + 2 * 3 - 6 / 2` :**

![][parsetree]
##### Transform parse tree into an Abstract Syntax Tree
![][ast]
##### Transform AST into a Control Flow Graph
A control flow graph is a directed graph that models the flow of a program using basic blocks. Each block contains the bytecode representation of program code inside it.
##### Byte Code generation from CFG
CFGs are usually one step away from final code output. Code is directly generated from the basic blocks by doing a post-order depth-first search on the CFG following the edges.
#### Pyhton Virtual Machine
As soon as source code gets converted to byte code, it is fed into PVM (Python Virtual Machine).

It’s just a big loop that iterates through your byte code instructions, one by one, to carry out their operations. The PVM is the runtime engine of Python; it’s always present as part of the Python system, and is the component that truly runs your scripts. Technically, it’s just the last step of what is called the Python interpreter.
![][pyexec]
***
<sup>[1](#FN1) From "Learning Python, Mark Lutz"</sup>
<sup>[2](#FN1) [Indian Pythonista](https://indianpythonista.wordpress.com/2018/01/04/how-python-runs/)</sup>