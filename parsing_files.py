def read_and_compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        if len(lines1) < len(lines2):
            print("File name:", file1)
            print("Quantity of strings:", len(lines1))
            print("Strings:", lines1)
            print("\nFile name:", file2)
            print("Quantity of strings:", len(lines2))
            print("Strings:")
            print('\n'.join(map(str, lines2)))
        else:
            print("File name:", file2)
            print("Quantity of strings:", len(lines2))
            print("Strings:", lines2)
            print("\nFile name:", file1)
            print("Quantity of strings:", len(lines1))
            print('Stings:')
            print('\n'.join(map(str, lines1)))


file1 = "1.txt"
file2 = "2.txt"

read_and_compare_files(file1, file2)
