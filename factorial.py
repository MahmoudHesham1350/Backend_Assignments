
""""
Example:

    if we have number 5
    then factorial ( 5 ) = 5 * factorial ( 4 )      
    then factorial ( 4 ) = 4 * factorial ( 3 )      
    then factorial ( 3 ) = 3 * factorial ( 2 )      
    then factorial ( 2 ) = 2 * factorial ( 1 )      
    then factorial ( 1 ) = 1  * factorial ( 0 )     
    then factorial ( 0 ) = 1

    Reversing from the bottom to the top to answer 
    on the previous formula until it reaches the final result
"""


def factorial(n):
    # Base case
    if(n==0):
        return 1
    else: 
        return n * factorial(n-1)  # Recursive call



if __name__ == "__main__":
    # Testing the function
    x = int(input("Enter a number: "))
    print(factorial(x))
