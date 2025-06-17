class TravelItinerary:
    def __init__(self, destination, budget):
        self.destination = destination
        self.__budget = budget 
        self.activities = []
        self.total_duration = 0 

    def add_activity(self, activity, cost, duration):
        if cost > self.__budget:
            print(f"You don't have enough budget for {activity}.")
        else:
            self.activities.append((activity, cost, duration)) 
            self.__budget -= cost
            self.total_duration += duration 
            print(f"You added {activity} to your itinerary for ${cost}. Duration: {duration} day(s). Your remaining budget is: ${self.__budget}")

    def calculate_budget(self):
        return self.__budget

    def summarize_itinerary(self):
        print(f"\nYour Travel Itinerary for {self.destination}:")
        print(f"Total Duration: {self.total_duration} day(s)")
        print("Activities planned:")
        for activity, cost, duration in self.activities:
            print(f"  - {activity}: ${cost} (Duration: {duration} day(s))")
        print(f"Your remaining budget is: ${self.__budget}\n")

class BudgetTrip(TravelItinerary):
    def add_activity(self, activity, cost, duration):
        if cost > self.calculate_budget() * 0.5: # To help users plan responsibly
            print(f"{activity} is too expensive for a budget trip!")
        else:
            super().add_activity(activity, cost, duration)

class LuxuryTrip(TravelItinerary):
    def add_activity(self, activity, cost, duration):
        super().add_activity(activity, cost, duration)
        print(f"Added luxury activity {activity} for ${cost}.")

    # Determine trip type based on budget.
def create_trip(destination, budget):
    if budget >= 2000:
        return LuxuryTrip(destination, budget)
    else:
        return BudgetTrip(destination, budget)


# Available activities for each location with their cost and duration
activities_list = {
    "South Africa": [
        ("Table Mountain Hike", 100, 0.5),
        ("Shark Cage Diving", 300, 1),
        ("Whale Watching", 900, 1),
        ("Boulder's Beach Penguin Visit", 50, 0.5),
        ("Safari Excursion", 500, 1),
        ("Safari Game Drive", 250, 1),
        ("Cape Point Tour", 200, 1),
        ("Cultural Township Tour", 150, 0.5),
    ],
    "China": [
        ("Great Wall of China Tour", 300, 1),
        ("Peking Duck Dinner", 50, 0.5),
        ("Temple of Heaven Visit", 100, 0.5),
        ("Lama Temple Visit", 90, 0.5),
        ("Explore the Hutongs", 100, 0.5),
        ("Summer Palace Tour", 120, 1),
        ("Beijing Opera Performance", 80, 1),
        ("Traditional Tea Ceremony", 70, 0.5),
    ],
    "India": [
        ("Taj Mahal Visit", 100, 1),
        ("Rickshaw City Tour", 50, 0.5),
        ("Street Food Crawl", 25, 0.5),
        ("Red Fort (Lal Qila)", 70, 1),
        ("Lotus Temple Visit", 40, 0.5),
        ("Spiritual Yoga Retreat", 200, 1),
        ("Jaipur City Tour", 150, 1),
        ("Varanasi Boat Ride", 100, 1),
    ],
    "Maldives": [
        ("Private Yacht Cruise", 3000, 1),
        ("Overwater Villa Stay", 2000, 2),
        ("Scuba Diving and Snorkeling", 500, 1),
        ("Water Sports (Jet Skiing or Kayaking)", 300, 0.5),
        ("Fishing Expedition", 400, 1),
        ("Underwater Dining Experience", 700, 1),
        ("Dolphin Watching", 300, 1),
        ("Sunset Cruise", 350, 1),
    ],
}


# 
valid_destinations = list(activities_list.keys())
preferred_destination = ""
while preferred_destination not in valid_destinations:
    preferred_destination = input(f"Which country would you like to visit? ({', '.join(valid_destinations)}): ").strip()
    if preferred_destination not in valid_destinations:
        print(f"Invalid destination. Please choose from: {', '.join(valid_destinations)}")

# Ask user for their available budget
budget_amount = int(input("What is your total trip budget in USD? ").strip())

# Create the trip based on the budget
trip = create_trip(preferred_destination, budget_amount)

# Show the available activities for the user's selected destination
available_activities = activities_list.get(preferred_destination, [])

while True:
    print(f"\nAvailable Activities for {preferred_destination}:")
    if available_activities:  # Check if there are still activities available
        for idx, activity in enumerate(available_activities, 1):
            print(f"{idx}. {activity[0]} - ${activity[1]} (Duration: {activity[2]} day(s))")
    else:
        print("No more activities available to add.")

    # Ask user to choose an activity
    try:
        activity_choice = int(input("\nEnter the number of the activity you'd like to add, or 0 to finish: ").strip())
        
        if activity_choice == 0:
            break  

        if 1 <= activity_choice <= len(available_activities):  
            activity = available_activities.pop(activity_choice - 1)  # Remove the activity the user selected from the list
            trip.add_activity(activity[0], activity[1], activity[2])  # Add the selected activity to the user's itinerrary
        else:
            print("Invalid choice. Please choose a valid activity number.")

    except ValueError:
        print("Invalid input. Please enter a number.")

# Summarize the trip
trip.summarize_itinerary()
