"""
welcome to repl.it! click run > on the top to run the below program with the given inputs and output.

feel free to edit the program/inputs/output below; your changes won't be saved or seen by anyone except you.

the source code is to the left, called loopwhile.py. let me (CJ) know if there are any bugs :)

07-01: fixed LOOP 0
"""

from loopwhile import Program

program = """

Y=0
Y=Y+1

I=0
J=0
LOOP X
 I=I+1
 J=J+1
END

K=0
S=0

LOOP X
 Y=Y+1

 G=0
 LOOP Y
  G=G+1
 END 
 G=G+1

 LOOP I
  H = 0
  LOOP G
   G = H
   H = H + 1
  END
 END
 
 F=0
 LOOP G
  F=0
  F=F+1
 END


 LOOP F
  V = 0
  V=V+1
  LOOP V
   H = 0
   LOOP Y
    Y = H
    H = H + 1
   END
  END
 END
 
 X=0
 LOOP I
  X=X+1
 END

 P = 0
 
 LOOP X
 P = P + 1
 END
 
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

 R = 0
 LOOP Z
  LOOP Y
   R = R + 1
  END
 END
 
 LOOP R
  C = 0
  LOOP P
   P = C
   C = C + 1
  END
 END
 

 S=0
 LOOP P
  S=0
  S=S+1
 END
 
 LOOP S
  K=K+1
 END
END

LOOP K
 A = 0
 LOOP J
  J = A
  A = A+1
 END
END

E=0
LOOP J
 E=0
 E=E+1
END

"""

inputs = {
  "X": 8,
  "Y": 0,
}

output = "E"

prog = Program(program)
print(prog.run(inputs, output))
