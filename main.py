from sweepstakes import Sweepstakes


def function_one():
    months = ('January','February','March','April','May','June','July','August','September','October','November','December')
    print(months[2])
    print("_____________End of 1A_____________")
    birthday_locals = ["Columbia","Sandy","Niles","North Vernon","Austin","San Jose"]
    birthday_locals.append("Layton")
    birthday_locals.append("Disneyland")
    birthday_locals.append("Lake Powell")
    for x in birthday_locals:
        print(x)
    print("_____________End of 1B_____________")
    customer_one = {
        'first_name':"Asuna",
        'last_name':"Yuuki"
    }
    customer_two = {
        'first_name': "Fred",
        'last_name': "Flintstone"
    }
    customer_three = {
        'first_name': "James",
        'last_name': "Bond"
    }
    customer_four = {
        'first_name': "Alfred",
        'last_name': "Hitchcock"
    }
    customer_five = {
        'first_name': "Sherlock",
        'last_name': "Holmes"
    }
    sweep = Sweepstakes()

    i = 1
    for x in [customer_one,customer_two,customer_three,customer_four,customer_five]:
        sweep.add_contestant(i, x)
        i += 1
    winner = sweep.select_winner()
    print(f"Congrats to {winner['first_name']} {winner['last_name']} for winning the sweepstakes")
    print("_____________End of 1C_____________")
    function_two()

def function_two():
    family_members = []
    mother = {
        'first_name': "Elaine",
        'last_name': "Peterson",
        'relationship': "Mother"
    }
    family_members.append(mother)
    father = {
        'first_name': "Paul",
        'last_name': "Peterson",
        'relationship': "Father"
    }
    family_members.append(father)
    sister = {
        'first_name': "Angela",
        'last_name': "Weil",
        'relationship': "Sister"
    }
    family_members.append(sister)
    middle_sister = {
        'first_name': "Michelle",
        'last_name': "Johnson",
        'relationship': "Sister"
    }
    family_members.append(middle_sister)

def test_method():
    function_one()

if __name__ == '__main__':
    test_method()
