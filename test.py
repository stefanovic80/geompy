# test.py

# Import the necessary module to run scripts
import subprocess

# Run main.py
subprocess.run(["python", "main.py"])

s1 = segment()
s2 = segment()
s1.erase()
s2.erase()
s1.grid()

s1.angCoeff = 1.2
s2.angCoeff = -.8
s1.intercept = .2
s2.intercept = -2

s1.draw("s1")
s2.draw("s2")

