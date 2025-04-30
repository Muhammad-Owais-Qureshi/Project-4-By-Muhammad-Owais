def mad_libs():
    # Prompt the user for inputs
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    
    story = f"Today I went to {place}. It was a very {adjective} day. I saw a {noun} that decided to {verb}!"

    
    print("\nHere is your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    mad_libs()