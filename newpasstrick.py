import datetime
import random
import math
import sys

def main():
    print("\n[!] ACCESS GRANTED. Welcome to the system.")
    sys.exit()

# --- 1-10: STRING MANIPULATION LOCKS ---
def lock1(): main() if input("1. Password: ") == "Password" else print("Fail")
def lock2(): main() if input("2. Case-Insensitive: ").lower() == "secret" else print("Fail")
def lock3(): main() if input("3. Reversed: ") == "drawssap" else print("Fail") # password backwards
def lock4(): main() if len(input("4. Length 10: ")) == 10 else print("Fail")
def lock5(): main() if input("5. Uppercase: ") == "SHOUT" else print("Fail")
def lock6(): p = input("6. Palindrome: "); main() if p == p[::-1] and p!="" else print("Fail")
def lock7(): main() if input("7. No Vowels (Hll): ") == "Hll" else print("Fail")
def lock8(): main() if input("8. Starts with 'A': ").startswith("A") else print("Fail")
def lock9(): main() if input("9. Ends with '!': ").endswith("!") else print("Fail")
def lock10(): main() if "key" in input("10. Must contain 'key': ") else print("Fail")

# --- 11-20: MATH & LOGIC LOCKS ---
def lock11(): main() if input("11. 15 + 27 = ") == "42" else print("Fail")
def lock12(): main() if int(input("12. Even number: ")) % 2 == 0 else print("Fail")
def lock13(): main() if int(input("13. Square root of 64: ")) == 8 else print("Fail")
def lock14(): main() if float(input("14. Pi (2 decimals): ")) == 3.14 else print("Fail")
def lock15(): main() if int(input("15. Multiples of 7: ")) % 7 == 0 else print("Fail")
def lock16(): main() if int(input("16. Negative number: ")) < 0 else print("Fail")
def lock17(): main() if input("17. Hex for 255: ") == "0xff" else print("Fail")
def lock18(): main() if len(set(input("18. 3 unique chars: "))) == 3 else print("Fail")
def lock19(): main() if input("19. Binary for 5: ") == "101" else print("Fail")
def lock20(): main() if int(input("20. Prime under 10: ")) in [2,3,5,7] else print("Fail")

# --- 21-30: LIST & MEMBERSHIP LOCKS ---
def lock21(): main() if input("21. Color of a banana: ") in ["yellow", "Yellow"] else print("Fail")
def lock22(): main() if input("22. Admin user: ") in ["admin", "root", "superuser"] else print("Fail")
def lock23(): main() if input("23. Type 'Empty' or 'None': ") in ["Empty", "None"] else print("Fail")
def lock24(): main() if input("24. Direction: ") in ["N", "S", "E", "W"] else print("Fail")
def lock25(): main() if input("25. Primary Color: ") in ["red", "blue", "yellow"] else print("Fail")
def lock26(): main() if input("26. Rock/Paper/Scissors: ") == "rock" else print("Fail")
def lock27(): main() if input("27. First 3 letters of Alphabet: ") == "abc" else print("Fail")
def lock28(): main() if input("28. Single Digit: ") in list("0123456789") else print("Fail")
def lock29(): main() if input("29. Yes or No: ").strip().capitalize() == "Yes" else print("Fail")
def lock30(): main() if len(input("30. Word count 2: ").split()) == 2 else print("Fail")

# --- 31-40: DYNAMIC & TIME LOCKS ---
def lock31(): main() if datetime.datetime.now().hour < 12 else print("PM Access Denied")
def lock32(): main() if datetime.date.today().weekday() < 5 else print("No Weekend Access")
def lock33(): main() if input("33. Today's Day (Number): ") == str(datetime.date.today().day) else print("Fail")
def lock34(): main() if input("34. Current Year: ") == "2026" else print("Fail")
def lock35(): 
    target = random.randint(1, 3)
    main() if input(f"35. Guess 1-3: ") == str(target) else print(f"Was {target}")
def lock36(): main() if not input("36. Don't type anything: ") else print("Fail")
def lock37(): 
    input("37. Press Enter then count to 2...")
    start = datetime.datetime.now()
    input("Now Press Enter: ")
    main() if (datetime.datetime.now() - start).seconds == 2 else print("Too fast/slow")
def lock38(): main() if input("38. Password is 'Hidden': ") == "\tHidden".strip() else print("Fail")
def lock39(): main() if input("39. 2^3 = ") == "8" else print("Fail")
def lock40(): main() if input("40. Enter 'None': ") != "" else print("Fail")

# --- 41-50: MISC & TRICKY LOCKS ---
def lock41(): main() if input("41. Say Please: ").lower() == "please" else print("How rude.")
def lock42(): main() if input("42. Type 'password' in 'quotes': ") == '"password"' else print("Fail")
def lock43(): main() if input("43. Space Bar 3 times: ") == "   " else print("Fail")
def lock44(): main() if input("44. Type 'Exit': ") == "Exit" else print("Fail")
def lock45(): 
    p = input("45. Multi-stage A: ")
    if p == "A":
        main() if input("Multi-stage B: ") == "B" else print("Fail B")
def lock46(): main() if input("46. ASCII 65: ") == "A" else print("Fail")
def lock47(): main() if sum(bytearray(input("47. Byte sum 200: "), 'utf-8')) > 200 else print("Too light")
def lock48(): main() if input("48. Input must be numeric: ").isdigit() else print("Fail")
def lock49(): main() if input("49. Input must be alpha: ").isalpha() else print("Fail")
def lock50(): 
    print("50. Final Boss: Type the name of this function.")
    main() if input("> ") == "lock50" else print("Fail")

# --- SELECTOR ---
if __name__ == "__main__":
    # Change the number below to test any of the 50 locks
    lock_to_test = 1 
    
    # Dynamic way to call the functions lock1() through lock50()
    func_name = f"lock{lock_to_test}"
    if func_name in locals():
        locals()[func_name]()
    else:
        print("Lock not found.")
