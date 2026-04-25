

# lock 1
def lock1():
    main() if input("Password: ")=="Password" else print("bye")

# lock 2
def lock2():
    password = input("Password:")
    if password=="Pasword":
        main()
    else :print("Bye")

def main():
    print("hi")

if __name__ == "__main__":
    lock1() #   or lock2() 


