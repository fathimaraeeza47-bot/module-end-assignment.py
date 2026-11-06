





feedback_data = {
     'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                 
     'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
     'Feedback': [ 'Very GOOD Service!!!',
                   'poor support, not happy',
                  'GREAT experience! will come again.',
                  'Okay okay...',
                  'not BAD',
                  'Excellent care, excellent staff!!', 
                  'Good food and good ambience!',
                 'Poor response and poor handling of issue',
                  'Satisfied. But could be better.',
                 'Good support... quick service.' ], 
     'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4] }


# Ask how many feedbacks to add
n = int(input("How many more feedbacks do you want to add? "))

# Loop to collect feedback
for i in range(n):

    print("\nEnter Feedback Details")

    name = input("Enter your name: ")

    feedback = input("Enter your feedback: ")

    rating = int(input("Enter your rating (1-5): "))

    # Validate rating
    while rating < 1 or rating > 5:
        print("Invalid rating! Please enter between 1 and 5.")
        rating = int(input("Enter your rating (1-5): "))

    # Generate serial number automatically
    s_no = len(feedback_data['S_No']) + 1

    # Append new data
    feedback_data['S_No'].append(s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

print("\nFeedback added successfully!")

print(feedback_data)

#DATA CLEANING

import string

for i in range(len(feedback_data['feedback'])):
    text = feedback_data['feedback'][i]

    for mark in ".,!?":
        text = text.replace(mark, "")

    text = " ".join(text.split())
    text = text.strip()
    text = text.lower()

    feedback_data['feedback'][i] = text
print(feedback_data['feedback'])    

  # Function to count feedbacks containing a particular word

def count_word_in_feedbacks(word):
    count = 0

    for feedback in feedback_data["Written Feedback"]:
        if word.lower() in feedback.lower():
            count += 1

    return count

# Display word count insights

print("Number of feedbacks containing 'good':", count_word_in_feedbacks("good"))

print("Number of feedbacks containing 'poor':", count_word_in_feedbacks("poor"))

print("Number of feedbacks containing 'excellent':", count_word_in_feedbacks("excellent"))



# Step 5: Final Summary & Insights (12 Marks)
#1. Display Final Cleaned Feedback Data
print("Final Cleaned Feedback Data:")
print(feedback_data)


#2. Calculate Average Rating
# Calculate Average Rating
total_rating = sum(feedback_data["Rating"])
total_feedbacks = len(feedback_data["Rating"])
average_rating = total_rating / total_feedbacks
print("Average Rating:", average_rating)


#3. Find Feedback with the Longest Comment
# Find the Longest Feedback Comment
longest_feedback = max
(    feedback_data["Written Feedback"],  
     key=lambda x: len(x.split()))
print("Longest Feedback Comment:", longest_feedback)
print("Word Count:", len(longest_feedback.split()))


#4. Find Unique Words Across All Feedbacks
## Find Unique Words

unique_words = set()

for feedback in feedback_data["Written Feedback"]:
    words = feedback.lower().split()

    for word in words:
        unique_words.add(word)

print("Unique Words Used Across All Feedbacks:")

print(unique_words)

print("Total Unique Words:", len(unique_words))