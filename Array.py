welcome_prompt = "========= WELCOME ========="
min_length = 6
max_length = 15
attempts = 0
max_attempts = 3

print(welcome_prompt)

while True:

    password = input("Enter a password (6-15 chars): ").strip() #Remove space
    if len(password) < min_length:

        attempts += 1
        remaining = max_attempts - attempts
        print(f"Password rejected, too short ({len(password)} characters). Minimum is {min_length}.")

        if attempts >= max_attempts:
            print("You are out of attempts. Bye")
            break

        attempts_word = "attempt" if remaining == 1 else "attempts"
        print(f"You have {remaining} {attempts_word} left. Try again!")

    elif len(password) > max_length:

        attempts += 1
        remaining = max_attempts - attempts
        print(f"Password rejected, too long ({len(password)} characters). Maximum is {max_length}.")

        if attempts >= max_attempts:
            print("You are out of attempts. Bye")
            break

        attempts_word = "attempt" if remaining == 1 else "attempts"
        print(f"You have {remaining} {attempts_word} left. Try again!")


    else:
        print("Password accepted ✅")
        break