"""
welcome to repl.it! click run > on the top to run the below program with the given inputs and output.

feel free to edit the program/inputs/output below; your changes won't be saved or seen by anyone except you.

the source code is to the left, called loopwhile.py. let me (CJ) know if there are any bugs :)

07-01: fixed LOOP 0
"""

from loopwhile import Program

program = """
A = 0
B = 0
C = 0

A = A + 1
B = B + 1
B = B + 1
LOOP X
 C = 0
 LOOP A
  LOOP B
   C= C + 1
  END
 END
 A = 0
 LOOP C
  A = A + 1
 END
END
"""

inputs = {
  "X": 6,
  "Y": 15,
}

output = "A"

prog = Program(program)
print(prog.run(inputs, output))
