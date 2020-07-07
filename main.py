"""
welcome to repl.it! click run > on the top to run the below program with the given inputs and output.

feel free to edit the program/inputs/output below; your changes won't be saved or seen by anyone except you.

the source code is to the left, called loopwhile.py. let me (CJ) know if there are any bugs :)

07-01: fixed LOOP 0
"""

from loopwhile import Program

program = """
N =0
LOOP X
 N=N+1
END

Y=0
Y=Y+1
Y=Y+1

X = X + 1
Z = 0
LOOP X
 LOOP Y
  A = 0
  LOOP X
   X = A
   A = A + 1
  END
 END
 
 B = 0
 LOOP X
  B = 0
  B = B + 1
 END
 
 LOOP B
  Z = Z + 1
 END
END


M=0
LOOP Z
 M=M+1
 M=M+1
END
LOOP M
 A = 0
 LOOP N
  N = A
  A = A+1
 END
END


A = 0
B=0
A=A+1
LOOP Z
 LOOP A
  B=B+1
 END
 LOOP B
  A=A+1
 END
END

R=0
LOOP B
 R=R+1
END

LOOP N
 R=0
 LOOP A
  R=R+1
 END
END
"""

inputs = {
  "X": 0,
  "Y": 15,
}

output = "R"

prog = Program(program)
print(prog.run(inputs, output))
