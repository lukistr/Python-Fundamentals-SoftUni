class FitnessData:
    def __init__(self, name, weight, height, duration):
        self.name = name
        self.weight = weight
        self.height = height
        self.duration = duration
        self.bmi = weight / height ** 2
        self.calories = duration * 5

def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)."""
    # Complete the implementation of this function
    return weight / (height ** 2)

def calculate_calories_burned(duration):
    """Calculate the estimated number of calories burned during exercise."""
    # Complete the implementation of this function
    return duration * 5

def filter_overweight_people(people_data):
    """Filter overweight people based on BMI."""
    # Fix and complete the implementation of this function
    overweight_people = []
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi >= 25:
            overweight_people.append(person)
    return overweight_people

# Main program
if __name__ == '__main__':
    people_data = []

    print("Enter fitness data for each person (Enter a blank name to finish):")
    while True:
        name = input("Enter person's name: ").strip()
        if not name:
            break
        weight = float(input("Enter person's weight in kilograms: "))
        height = float(input("Enter person's height in meters: "))
        duration = float(input("Enter exercise duration in minutes: "))
        people_data.append(FitnessData(name, weight, height, duration))
        # person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
        # people_data.append(person)

    print("\nFitness Analysis:")
    for person in people_data:
        # bmi = calculate_bmi(person['weight'], person['height'])
        # calories_burned = calculate_calories_burned(person['duration'])
        print(f"{person.name}: BMI = {person.bmi:.2f}, Calories burned = {person.calories:}")

    # overweight_people = filter_overweight_people(people_data)
    print("\nOverweight People:")
    for person in people_data:
        # bmi = calculate_bmi(person['weight'], person['height'])
        if person.bmi >= 25:
            print(f"{person.name}: BMI = {person.bmi:.2f}")
