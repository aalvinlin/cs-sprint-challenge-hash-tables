def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    needed_weights = dict()

    print("\nlooking in weights", weights, "\n")

    for current_weight_index in range(len(weights)):

        current_weight = weights[current_weight_index]

        # if the key is found, then that means the counterpart to this weight was inserted previously
        if current_weight in needed_weights:

            # get index of other weight
            previously_seen_weight_index = weights[current_weight]

            return (current_weight_index, previously_seen_weight_index)
        
        else:
            # store info about this current weight
            # key: other weight needed to add up to the limit
            # value: the current weight's index
            needed_weights[limit - current_weight] = current_weight_index

        print('current needed weights:', needed_weights)

    return None
