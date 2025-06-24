print(" Welcome to the Mad Libs Game!\n")

# Collect words from the user
name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
food = input("Enter a food item: ")
verb = input("Enter a verb ending in -ing: ")

# Create the story
story = f"""
Once upon a time, {name} went to {place} with a very {adjective} {animal}.
They were {verb} while eating {food}, and everyone around was amazed!
From that day, {name} became famous across all of {place}.
"""

print("\n Here's your story:\n")
print(story)
