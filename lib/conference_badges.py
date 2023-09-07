def badge_maker(name):
    return f"Hello, my name is {name}."

#test
speaker_name = "Arel"
badge_message = badge_maker(speaker_name)
print(badge_message)  

def batch_badge_creator(speakers):
    return [f"Hello, my name is {name}." for name in speakers]

# test
speaker_names = ["Clive", "David"]
badge_messages = batch_badge_creator(speaker_names)
print(badge_messages) 

def assign_rooms(speakers):
    room_assignments = []
    
    # Iterate through the list of speakers and assign rooms
    for index, speaker in enumerate(speakers, start=1):
        room_assignment = f"Hello, {speaker}! You'll be assigned to room {index}!"
        room_assignments.append(room_assignment)
    
    return room_assignments

# test
speaker_names = ["Clive", "David","Mike", "Emma", "Stacy","Joseph", "Bill"]
room_assignments = assign_rooms(speaker_names)
print(room_assignments)



def printer(speakers):
    # Get badge messages
    badge_messages = batch_badge_creator(speakers)
    
    # Print badge messages
    for message in badge_messages:
        print(message)
    
    # Get room assignments
    room_assignments = assign_rooms(speakers)
    
    # Print room assignments
    for assignment in room_assignments:
        print(assignment)

# test
speaker_names = ["Clive", "David"]
printer(speaker_names)

