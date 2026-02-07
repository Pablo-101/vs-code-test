done = False

while True:
    new_pass = input("Enter your new password: ")

    if len(new_pass) < 6:
        print("Password can't be less than 6 characters.")
        continue
    if len(new_pass) > 12:
        print("Password can't be more than 12 characters.")
        continue
    if not new_pass.isalpha():
        print("Password can contain only letters.")
        continue

    # Confirmation loop with option to re-enter the new password
    while True:
        confirm_pass = input("Confirm your new password: ")
        if new_pass == confirm_pass:
            print("Password set successfully!")
            done = True      # mark success
            break            # break inner loop
        print("Passwords don't match.")
        choice = input("Type 'c' to try confirming again or 'n' to enter a new password: ").lower()
        if choice == 'n':
            break            # break inner loop and go back to outer loop

    if done:
        break                # break outer loop because password was set
