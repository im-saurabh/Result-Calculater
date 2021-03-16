print("-------------------!Welcome!------------------------")

Name = input(" Enter Your Name : ")
Rollno = input(" Enter your RollNo : ")

print("-------------------!MARKS!------------------------")

A = int(input(" Marks in INS : "))
B = int(input(" Marks in WS : "))
C = int(input(" Marks in GP : "))
D = int(input(" Marks in STQA : "))
E = int(input(" Marks in AI : "))

print("-------------------!GRADES!------------------------")

if A>=70 :
    print("You Have A Grade In INS")
elif A>=60:
    print("You Have B Grade In INS")
elif A>=50:
    print("You Have C Grade In INS")
elif A>=40:
    print("You Have D Grade In INS")
else :
    print("You Have KT In INS")
    
if B>=70 :
    print("You Have A Grade In WS")
elif B>=60:
    print("You Have B Grade In WS")
elif B>=50:
    print("You Have C Grade In WS")
elif B>=40:
    print("You Have D Grade In WS")
else :
    print("You Have KT In WS")

if C>=70 :
    print("You Have A Grade In GP")
elif C>=60:
    print("You Have B Grade In GP")
elif C>=50:
    print("You Have C Grade In GP")
elif C>=40:
    print("You Have D Grade In GP")
else :
    print("You Have KT In GP")

if D>=70 :
    print("You Have A Grade In STQA")
elif D>=60:
    print("You Have B Grade In STQA")
elif D>=50:
    print("You Have C Grade In STQA")
elif D>=40:
    print("You Have D Grade In STQA")
else :
    print("You Have KT In STQA")

if E>=70 :
    print("You Have A Grade In AI")
elif E>=60:
    print("You Have B Grade In AI")
elif E>=50:
    print("You Have C Grade In AI")
elif E>=40:
    print("You Have D Grade In AI")
else :
    print("You Have KT In AI")
    
print("-------------------!TOTAL-MARKS!------------------------")

Totalmarks =int(A)+int(B)+int(C)+int(D)+int(E)

print("Total Marks is : ",Totalmarks)

print("-------------------!PERCENTAGE!------------------------")

percentage =  int(Totalmarks)/350*100

print("percentage is : ",percentage)

print("-------------------!PERFORMANCE!------------------------")

if Totalmarks >= 350 :
    print(" Congratulations! ",Name)
    print(" Your Performance is outstanding ")
elif Totalmarks >= 300 :
    print(" Congratulations! ",Name)
    print(" Your Performance is Excellent ")
elif Totalmarks >= 250 :
    print(" Congratulations! ",Name)
    print(" Your Performance is Very Good ")
elif Totalmarks >= 200 :
    print(" Congratulations! ",Name)
    print(" Your Performance is Good ")
else:
    print(" You are Failed In Exam ")
    print(" We are really Sorry for You better luck next time!")
