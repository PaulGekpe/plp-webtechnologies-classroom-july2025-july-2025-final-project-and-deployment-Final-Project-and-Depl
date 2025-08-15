#greeting app
def prompt_nonempty(message):
    while True:
        text = input(message).strip()
        if text:
            return text
        print("Please type something🤗")
name = prompt_nonempty("What's your name?")
color = prompt_nonempty("What's your favorite color")

name = name.title()
color = color.capitalize()

print(f"Hello, {name}! Your favorite color, {color}, is awesome! 🎉")