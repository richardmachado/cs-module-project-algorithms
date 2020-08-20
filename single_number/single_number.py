'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    
    # create a set
    s = set()
    
    # loop through the numbers
    for i in arr:
        #if this is in the set already, remove it
        if i in s :
            s.remove(i)
        #otherwise, it's a single, so add it
        else:
            s.add(i)
    #find the nonduplicate

    return list(s)[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")