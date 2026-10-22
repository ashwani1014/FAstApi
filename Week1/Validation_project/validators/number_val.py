def validate_number(number: int | float )-> int | float :
    if isinstance(number , bool) or not isinstance(number ,(int ,float)):
        raise TypeError("Number must be an integer or float")
    

    if number < 0  :
        raise ValueError("Number must be non-negative")




    return number
