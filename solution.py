def is_acceptable_password(stero):
    """ check multiple conditions on a given string, return True if it passes"""
    
    stero = stero.lower()
    l = len(stero)

    # check if substring 'password' is not in the string
    if 'password' not in stero:
        if l > 6 and l <= 9:  # check length condition
            if any(char.isalpha() for char in stero):  # make sure string is not only numbers
                if any(char2.isdigit() for char2 in stero):  # make sure there are numbers in string
                    return True

        elif l > 9:  # if length is bigger than 9, skip conditions.
            return True            

    return False
