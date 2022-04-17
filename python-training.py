

import platform

version = platform.python_version()

def main():
    message()


def message():
    print("This is python version {}".format(version))
    print(f'This is python version {version}')
    if False:
        print("4")
    else: 
        print(9)
    
    
print(3)

#This is comment!


if __name__ == '__main__': main()