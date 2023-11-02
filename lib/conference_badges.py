def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    room_assigments = []
    for i in range(len(names)):
         room_assigments.append(f"Hello, {names[i]}! You'll be assigned to room {i+1}!")
    return room_assigments

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room_assignment in assign_rooms(names):
        print(room_assignment)
