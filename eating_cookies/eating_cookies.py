'''
Input: an integer
Returns: an integer
'''
# goes really slow after 20 cookies, likely O(n^3)
def eating_cookies(n):
    # Your code here

    # Check that input is negative
    if n < 0:
        # Can't eat negative cookies!
        return 0
    # Check if input is 0
    elif n == 0:
        return 1 
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
       

        


        

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 100

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")