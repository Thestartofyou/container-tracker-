import requests

# Replace with the actual API endpoint and API key
API_URL = "https://api.example.com/container-tracking"
API_KEY = "your_api_key_here"

def track_container(container_number):
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        params = {"container_number": container_number}

        response = requests.get(API_URL, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            display_container_data(data)
        elif response.status_code == 404:
            print("Container not found.")
        else:
            print(f"Failed to retrieve tracking data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def display_container_data(data):
    # Implement how you want to display container data here
    # Extract relevant information from the 'data' JSON response
    print("Container Tracking Information:")
    print(f"Container Number: {data['container_number']}")
    print(f"Current Location: {data['current_location']}")
    print(f"Transit History: {data['transit_history']}")
    print(f"Estimated Arrival Time: {data['estimated_arrival_time']}")

def main():
    print("Welcome to Container Tracker!")
    container_number = input("Enter the container number: ")
    track_container(container_number)

if __name__ == "__main__":
    main()
