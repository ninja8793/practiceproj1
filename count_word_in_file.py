python_count = 0
total_word_in_f = 0
with open("C:\\Users\\prasad\\Desktop\\test1.txt",'r')as file:
    lines = file.readlines()
    len_lines = len(lines)
    print("#########################################################")
    print("Total no of lines:",len_lines)

    for line in lines:
        words_in_line = line.strip().split(" ")
        print("Words in line:",words_in_line)
        for word in words_in_line:
            total_word_in_f += 1
            if word.lower() == 'python':
                python_count+=1
    print("#######################################################")
    print("Total word in file:",total_word_in_f)
    print("#######################################################")
    print("Total Python word in file:",python_count)