import requests

URL = "https://zenquotes.io/api/random"

def fetch_quote():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data[0]
    else:
        print("Failed to fetch quote. Status code:", response.status_code)
        return None

def display_quote(quote):
    print("\n💬", quote["q"])
    print("   —", quote["a"])
    print()

def main():
    quote = fetch_quote()
    if quote:
        display_quote(quote)

def fetch_multiple_quotes(n):
    for i in range(n):
        quote = fetch_quote()
        if quote:
            print(f"Quote {i+1}:")
            display_quote(quote)

def main():
    print("=== Quote of the Day Bot ===\n")
    choice = input("How many quotes do you want? (1-5): ")
    fetch_multiple_quotes(int(choice))

def main():
    print("=== Quote of the Day Bot ===\n")
    try:
        choice = int(input("How many quotes do you want? (1-5): "))
        if choice < 1 or choice > 5:
            print("Please enter a number between 1 and 5.")
        else:
            fetch_multiple_quotes(choice)
    except ValueError:
        print("Invalid input! Please enter a number.")

main()