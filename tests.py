from run_python_file import run_python_file


test1 = run_python_file("calculator", "main.py")
test2 = run_python_file("calculator", "tests.py")
test3 = run_python_file("calculator", "../main.py")
test4 = run_python_file("calculator", "nonexistent.py")

print(f"""
Test one: {test1}
Test two: {test2}
Test three: {test3}
Test four: {test4}
""")
