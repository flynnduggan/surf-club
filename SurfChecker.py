# -*- coding: utf-8 -*-

def extract_names(raw_data):
    
    # Split the raw data by new lines
    lines = raw_data.splitlines()

    # Filter out unwanted lines
    names = []
    for line in lines:
        if ("Unchecked" not in line and
            "Board hire" not in line and
            "Wetsuit hire" not in line and
            "Surf membership" not in line and 
            "-" not in line and 
            not line.isdigit()):
            names.append(line.strip())  # Add the cleaned name to the list

    return names

def check_non_members(members, ticket_holders):
    
    # Convert both lists to sets for easier comparison
    members_set = set(members)
    ticket_holders_set = set(ticket_holders)

    # Find the difference: ticket holders who are not members
    non_members = list(ticket_holders_set - members_set)

    # Return the number of non-members and their names
    return len(non_members), non_members

def check():
    # Predefined list to store members
    names_members = []

    # Ask if the user wants to update the members list
    update_members = input("Update members list? (yes/no): ").strip().lower()

    if update_members == "yes":
        # Request the user to input/paste the new members list
        raw_members_data = input("Please input/paste the new members list:\n")
        new_members = extract_names(raw_members_data)

        # Append new members to the list, ignoring duplicates
        for member in new_members:
            if member not in names_members:
                names_members.append(member)

        print(f"Updated members list: {names_members}")

    # Reset the names_trip list for each run
    names_trip = []

    # Request the user to input/paste the surf trip data
    raw_trip_data = input("Please input/paste surf trip data:\n")
    names_trip = extract_names(raw_trip_data)

    # Run the check for non-members
    num_non_members, non_members_list = check_non_members(names_members, names_trip)

    # Output the results
    print(f"\nNumber of non-members: {num_non_members}")
    print(f"Non-members: {non_members_list}")

# Call the main function to run the program
    if __name__ == "__main__":
        check()