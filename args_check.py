def check(arguments):
    #custum time interval
    if len(arguments) == 3:

        #throws error when arg is not int
        if isinstance(int(arguments[2]), int):

            if(int(arguments[2]) > 0):
                var = float(int(arguments[2]) * 60)

            else:
                raise ValueError("Time elapsed must be a positive value.")

    #default time interval (300 sec)
    elif len(arguments) == 2:
        var = float(300)
    
    #incorrect num of args
    else:
        raise Exception("Missing Gallery Name.")
    
    return var
 