# py_beggie_projects

print("enter no 1: ")
inp1=int(input())
print("enter no 2: ")
inp2=int(input())
print("choose operation,*,+,/ : ")
operation=input()

if inp1 ==45 and inp2 ==3 and operation =='*':
    print(555)
elif operation =='*' and inp1!=45 and inp2!=3:
    print(inp1*inp2)

if inp1 ==56 and inp2 ==9 and operation =='+':
    print(77)
elif operation =='+' and inp1!=56 and inp2!=9:
    print(inp1+inp2)

if inp1 ==56 and inp2 ==6 and operation =='/':
    print(4)
elif operation == '/' and inp1!=56 and inp2!=6:
    print(inp1 / inp2)
