#quiz koty b jan 3 2019
import sys
name="quiz.txt"
a=1


def open_file(file_name, mode):
    """open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("unable to open file, ending program")
        input("prees enter to finish shutdown")
        sys.exit
    else:
        return the_file
def next_line(the_file):
    line=the_file.readline()
    line=line.replace("/","\n")
    return line





the_file=open_file(name,"r")
while a<100:
    line = next_line(the_file)
    print(line)
    a=a+1
