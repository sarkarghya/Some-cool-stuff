"""
welcome to repl.it! click run > on the top to run the below program with the given inputs and output.

feel free to edit the program/inputs/output below; your changes won't be saved or seen by anyone except you.

the source code is to the left, called loopwhile.py. let me (CJ) know if there are any bugs :)

07-01: fixed LOOP 0
"""

from loopwhile import Program

program = """

P=0

LOOP X
P=P+1
END

X=X+1
Z=0
LOOP X
 LOOP Y
  A = 0
  LOOP X
   X = A
   A = A+1
  END
 END

 B=0
 LOOP X
  B=0
  B=B+1
 END

 LOOP B
  Z = Z+1
 END
END

R=0
LOOP Z
 LOOP Y
  R = R + 1
 END
END

LOOP R
 C = 0
 LOOP P
  P = C
  C = C+1
 END
END

Y=0
LOOP P
Y=Y+1
END

"""

inputs = {
  "X": 25,
  "Y": 15,
}

output = "P"

prog = Program(program)
print(prog.run(inputs, output))
