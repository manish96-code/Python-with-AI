import re

pattern = "^a...e$"
test_str = "apple"
result = re.match(pattern, test_str)
if result:
    print("Matched.")
else:
    print("Not matched.")


# Mobile no. validation
mob_pattern = "^[6-9][0-9]{9}$"
mob = int(input("Enter your mobile number: "))
check_mob = re.match(mob_pattern, str(mob))
if check_mob:
    print("Valid mobile number")
else:
    print("Invalid mobile number")
