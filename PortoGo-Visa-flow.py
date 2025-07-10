def start_chat():
    print("\n🇵🇹 Welcome to the PortoPal Visa Eligibility Assistant!\n")
    input("Press Enter to begin...")

    # Question 1: Reason for relocating
    print("\nQ1. Why are you relocating to Portugal?")
    print("1. I am a digital nomad")
    print("2. I am retired")
    print("3. Family reunion")

    while True:
        choice1 = input("Select 1, 2, or 3: ").strip()
        if choice1 in ["1", "2", "3"]:
            break
        else:
            print("Please choose 1, 2, or 3.")

    # Question 2: Income level
    print("\nQ2. What is your monthly income or savings? (USD)")
    print("1. Below $1,000")
    print("2. $1,000 - $3,000")
    print("3. Above $3,000")

    while True:
        choice2 = input("Select 1, 2, or 3: ").strip()
        if choice2 in ["1", "2", "3"]:
            break
        else:
            print("Please choose 1, 2, or 3.")

    # Decision logic
    print("\n📝 Result:")

    if choice1 == "1":  # Digital nomad
        if choice2 == "3":
            print("You may qualify for the D8 Digital Nomad Visa. Start gathering proof of remote income.")
        else:
            print("Digital Nomad visa usually requires proof of higher income. You might need a co-sponsor or alternative path.")
    elif choice1 == "2":  # Retired
        if choice2 in ["2", "3"]:
            print("You may qualify for the D7 Retirement Visa. Savings and pension documents will be needed.")
        else:
            print("You may need to show additional financial resources or apply with a co-signer.")
    elif choice1 == "3":  # Family reunion
        print("You may qualify for a Family Reunification Visa. Your sponsor in Portugal must provide documents.")

    print("\n✅ This is a general guide. Consult the Portuguese consulate for official requirements.")
    print("Thank you for using PortoPal!\n")

if __name__ == "__main__":
    start_chat()
