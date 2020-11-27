# Python 3 code to demonstrate 
# SHA hash algorithms. 
  
import hashlib 
import sys

  
def get_SHA1(string):
    result = hashlib.sha1(string.encode())
    return result.hexdigest()

def example1():
    string="GeeksGod"
    # printing the equivalent hexadecimal value. 
    print("The hexadecimal equivalent SHA1 of ",string," is : ",get_SHA1(string)) 

def get_system_arguments():
    for args in sys.argv:
        print(args)

if __name__ == "__main__":
    print(get_SHA1(str(sys.argv[1])))

