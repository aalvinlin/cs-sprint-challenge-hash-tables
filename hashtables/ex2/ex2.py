#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

# use a doubly linked list instead?

def reconstruct_trip(tickets, length):
    
    # prepopulate an array with the same number elements as tickets
    # the last element of the route will be "NONE"
    route = [None] * length
    route[-1] = "NONE"
    
    # go through each ticket and store its immediate destination
    destinations = dict()

    for ticket in tickets:
        destiations[source] = destinations  
    
    # pick a random ticket and see what destinations both precede and come after it
    start_ticket = tickets[0]

    # initialize an array to work out preceding and following destinations
    # since we don't know the location of start_ticket in the overall route, make the array twice as big as necessary and put the starting destination in the middle
    destinations_holder = [None] * 2 - 1
    destinations_holder[length - 1] = start_ticket.source

    # previous_destination = destinations[start_ticket.source]

    # while previous_destination:
    #     destinations_before

    next_destination = destinations[start_ticket.destination]

    while next_destination:
        next_destinations
        next_destination = 

    return route
