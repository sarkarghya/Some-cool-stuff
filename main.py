"""
welcome to repl.it! click run > on the top to run the below program with the given inputs and output.

feel free to edit the program/inputs/output below; your changes won't be saved or seen by anyone except you.

the source code is to the left, called loopwhile.py. let me (CJ) know if there are any bugs :)

07-01: fixed LOOP 0
"""

from loopwhile import Program

program = """
B=0
LOOP X
 X=B
 B=B+1
 LOOP Y
  A = 0
  LOOP X
   X = A
   A = A+1
  END
 END
END
"""

inputs = {
  "X": 80,
  "Y": 9,
}

output = "X"

prog = Program(program)
print(prog.run(inputs, output))
