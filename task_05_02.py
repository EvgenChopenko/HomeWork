"""
2                                  1


___________________________________________



3                                 4
"""

def get_quadrant_number(x,y):

        if x>0 and y>0:
            return 1
        elif x>0 and y<0:
            return 4
        elif x<0 and y>0:
            return 2
        elif x<0 and y<0:
            return 3
        else:
            raise ValueError





if(__name__=="__main__"):
    print(get_quadrant_number(1,1),"=",1)
    print(get_quadrant_number(-1, 1),"=", 2)
    print(get_quadrant_number(-1, -1), "=", 23)
    print(get_quadrant_number(1, -1), "=", 4)
    print(get_quadrant_number(0, 0), "=", 'valueError')
    print(get_quadrant_number(0, 1), "=", 'valueError')
    print(get_quadrant_number(1, 0), "=", 'valueError')
