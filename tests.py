from get_files_content import get_file_content


test1 = get_file_content('calculator', 'main.py')
test2 = get_file_content('calculator', 'pkg/calculator.py')
test3 = get_file_content('calculator', '/bin/cat')

print(f"""
Test one: {test1}
Test two: {test2}
Test three: {test3}
""")
