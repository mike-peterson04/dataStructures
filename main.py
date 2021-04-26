from sweepstakes import Sweepstakes
from linkedlist import LinkedList
from tree import Tree


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

def function_three():
    list = LinkedList()
    list.prepend_node(9999)
    list.append_node(55)
    list.append_node(9001)
    list.append_node(2)
    list.append_node(1024)
    list.prepend_node(9998)
    print(list.contains(9999))
    print("_____________End of 3 _____________")

def function_four():
    t = Tree()
    t.insert(35)
    t.insert(13, t.root)
    t.insert(11, t.root)
    t.insert(15, t.root)
    t.insert(19, t.root)
    t.insert(99, t.root)
    t.insert(9001, t.root)
    t.insert(8263, t.root)
    t.insert(35, t.root)
    t.insert(9001, t.root)
    print(t.search(99))
    print("pre-ordered")
    t.pre_order(t.root)
    print("in order")
    t.in_order(t.root)


def test_method():
    function_one()
    function_two()
    function_three()
    function_four()

if __name__ == '__main__':
    test_method()
