import requests

def get_random_fact():
    """Fetches a completely random useless fact in English."""
    url = "https://jsph.pl"
    params = {"language": "en"}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        print("\n🎲 [Random Fact]")
        print(data.get("text"))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching random fact: {e}")

def get_fact_of_the_day():
    """Fetches the useless fact designated for today."""
    url = "https://jsph.pl"
    params = {"language": "en"}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        print("\n📅 [Fact of the Day]")
        print(data.get("text"))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching today's fact: {e}")

if __name__ == "__main__":
    print("--- Project 1: Random Useless Facts Endpoints ---")
    get_random_fact()
    get_fact_of_the_day()
