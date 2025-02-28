def multiply_even_numbers_in_interval (start, stop):
    
    """ A program to multiply even numbers between two input
    values, start and stop (INCLUSIVE). For example, 
    
        multiply_even_numbers_in_interval (5, 20)
    
    should multiply: 
    
        6 x 8 x 10 x 12 x 14 x 16 x 18 x 20
    
    """

    # Set initial value of product
    product = 1

    # Create a string representation of the multiplication.
    string_representation = "1"

    # Initialise a counter
    i = start
    
    while i < stop:
        if i % 2 == 0:
            product *= i
            string_representation += (f" x {i}")
        i += 1
    print (string_representation)
    return product

def multiply_even_numbers_in_interval_fixed (start, stop):
    
    """ A program to multiply even numbers between two input
    values, start and stop (INCLUSIVE). For example, 
    
        multiply_even_numbers_in_interval (5, 20)
    
    should multiply: 
    
        6 x 8 x 10 x 12 x 14 x 16 x 18 x 20
    
    """

    # Set initial value of product
    product = 1

    # Create a string representation of the multiplication.
    string_representation = "1"

    # Initialise a counter
    i = start
    while i <= stop:
        if i % 2 == 0:
            product *= i
            string_representation += (f" x {i}")
        i += 1
    print (string_representation)
    return product


if __name__ == '__main__':
    print(multiply_even_numbers_in_interval_fixed(5, 20))
    print(multiply_even_numbers_in_interval_fixed(1, 6))
    print(multiply_even_numbers_in_interval_fixed(2, 10))
    