def badge_maker(name):
    return(f"Hello, my name is {name}.")

def batch_badge_creator(names):
    badge_messages = list()
    for name in names:
        badge_messages.append(f"Hello, my name is {name}.")

    return badge_messages

def assign_rooms(names):
    room_nums = list()
    num = 1
    for name in names:
        room_nums.append(f"Hello, {name}! You'll be assigned to room {num}!")
        num += 1
    return room_nums

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badges:
        print(badge)

    for assignment in room_assignments:
        print(assignment)
