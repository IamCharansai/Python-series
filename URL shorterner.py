import pyshorteners

def shorten_url():
    print(" URL Shortener\n")

    long_url = input("Enter the long URL: ").strip()
    
    if not long_url.startswith("http"):
        print(" Please enter a valid URL starting with http or https.")
        return

    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(long_url)
        print(f"\n Shortened URL: {short_url}")
    except Exception as e:
        print(" Error occurred:", e)

shorten_url()
