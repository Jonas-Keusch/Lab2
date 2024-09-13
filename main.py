import random



step = 5
max_people = 50

File_object = open(r"results", "C:\Users\jonas\OneDrive\Desktop\data structures\Lab2")

for num_people in range(5, max_people + 1, step):
    duplicates_count = 0
    
    
    for _ in range(num_people):
       
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        
        
        if len(birthdays) != len(set(birthdays)):
            duplicates_count += 1
    
   
    probability = duplicates_count / num_people
    
    print(f"Number of people: {num_people}, Probability of shared birthday: {probability:.2f}")
    File_object.write(f"Number of people: {num_people}, Probability of shared birthday: {probability:.2f}")
print("results have been saved to 'results.txt'.")
