# The objective of this program is to allow users to input multiple pairs of course IDs and
# course names. Each pair consists of a course ID (e.g., "COS 2005") and a corresponding course
# name (e.g., "Python Programming"). The program will store these pairs and display them upon
# completion of the input process.

# Pseudocode
# Initialize an empty list to store course IDs and names
# Loop indefinitely to accept user input
# Prompt the user to enter a course ID and course name separated by a comma
# Read user input
# Check if the input is empty
# If empty, break the loop
# Split the input string into course ID and course name using the comma as a delimiter
# Store course ID in variable course_id
# Store course name in variable course_name
# Append a tuple (course_id, course_name) to the list of courses
# After exiting the loop, print the list of courses
# Optionally, return the list of courses for further processing

def main():
    courses = {}

    while True:
        course_id = input("Enter course ID (or type 'exit' to finish): ")
        if course_id.lower() == 'exit':
            break
        course_name = input("Enter course name: ")
        courses[course_id] = course_name

    print("\nCourse List:")
    for cid, cname in courses.items():
        print(f"{cid}: {cname}")


if __name__ == "__main__":
    main()

# Caleb Saari 3/20/25 Wk8 Program 4: Course Info