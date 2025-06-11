from write_file import write_file


test1 = write_file("calculator", "loren.txt", "wait, this isn't lorem ipsum")
test2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
test3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

print(f"""
Test one: {test1}
Test two: {test2}
Test three: {test3}
""")
