Developer_Tester_Project/
│
├── developer.py      # Code written by developer
def add(a,b)
return a+b
def subtract(a,b)
return a-b
if_name_="main":
print("add 5+3:",add(5,3))
print("sub 5-3:",sub(5,3))
├── tester.py         # Code written by tester
from src.app.import add,sub
def test_add():
assert add(5,3)==8
deftest_sub():
assert sub(5,3)==-2

└── README.md         # Description of the project
