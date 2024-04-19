def badge_maker(name):
    return "Hello, my name is " + name + "."

def batch_badge_creator(names):
    badges = [badge_maker(name) for name in names]
    return badges

def assign_rooms(names):
    strings = ["Hello, " + name + "! You'll be assigned to room " + str(names.index(name) + 1) + "!" for name in names]
    return strings

def printer(names):
    messages = batch_badge_creator(names) + assign_rooms(names)
    for message in messages:
        print(f'{message}')
