import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke = response.json()
            print("\nHere's a joke for you :\n")
            print(f"{joke['setup']}")
            print(f"{joke['punchline']}")
        else:
            print(" Couldn't fetch joke. Try again later.")
    except Exception as e:
        print(" Error:", e)

# Run it
print(" Welcome to the Random Joke Generator!")
get_joke()
