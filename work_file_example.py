def add(x,y):
    return(x+y)

def merge(x,y):
    return({**x,**y})

def digit_sum(x):
    return(sum(int(i) for i in list(str(abs(x)))))

def new_tuple(*args):
    return(tuple([*args]))

def sqrt(x):
    return(x**0.5)

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return(abs(a))

def lcm(a,b):
    return((a*b)/gcd(a,b))

def distance_2d(a,b):
    x_len = abs(a[0]-b[0])
    y_len = abs(a[1]-b[1])
    return(sqrt(x_len**2+y_len**2))
    # I created an sqrt function earlier in this file, that I use here

def distance_3d(a,b):
    x_len = abs(a[0]-b[0])
    y_len = abs(a[1]-b[1])
    z_len = abs(a[2]-b[2])
    xy_len = sqrt(x_len**2+y_len**2)
    return(sqrt(xy_len**2+z_len**2))
    # I created an sqrt function earlier in this file, that I use here

def is_prime(x):
    if x in [0,1]:
        return(False)
    for i in range(2,int(sqrt(x))+1):
        if x%i==0:
            return(False)
    return(True)

def robot_position(starting_position,instructions):
    instruction_to_pos = {"up":[0,1],"right":[1,0],"down":[0,-1],"left":[-1,0]}
    robot_pos = starting_position
    for instruction in instructions:
        direction = instruction_to_pos[instruction.lower()]
        robot_pos = (robot_pos[0]+direction[0],robot_pos[1]+direction[1])
    return(robot_pos)
        
