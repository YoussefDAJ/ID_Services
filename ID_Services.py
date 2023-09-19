is_egyptian = input("Are you Egyptian? Type 'Yes' or ''No' ").lower()
if is_egyptian == "yes":
    print("Good that's the first step")
    is_18 = input("Are you above 18? Type 'Yes' or 'No' ").lower()
    if is_18 == "yes":
        print("You can have and ID")
    else:
        print("Sorry, you have to be 18 or older")
        print("Please try again when you are 18")
else:
    print("Sorry, an Egyptian ID is give only to Egyptians")
