work_file_name = "work_file_example"
try:
    work_file = __import__(work_file_name)
except Exception as e:
    print("Got error:\n{}\nWhile trying to import work_file.py".format(e))


def add_commas(the_input):
    # Adds high commas ('') around strings, to make it clear when printed that it's a string
    if isinstance(the_input,str):
        # Tests if it's a string
        return("'" + the_input + "'")
        # Returns a string with high commas if it's a string
    return(the_input)
    # Otherwise just returns the_input without high commas


def test_func(func,func_name,test_cases):
    # func is the function it should use
    # func_name is the name it should use in the printed text
    #
    # test_cases is a list composed of two smaller lists. The arguments and the answers
    # test_cases = [ [arguments] , [answers] ]
    # Arguments consists of lists, each list being a set of arguments to pass on to the function
    # Answers is a list of all the answers
    #
    # I didn't use dictionaries because you can't use a list as a key in a dictionary
    for i in range(len(test_cases[0])):
        # Loops trough the list
        # I used 'for i in range(len(list))' instead of 'for i in list' because I need to get the current index anyway to get the answers
        variables = test_cases[0][i]
        # Gets the current list of arguments
        answer = test_cases[1][i]
        # Gets the answer to the arguments
        nice_print = "{}({})".format(func_name,",".join(str(add_commas(h)) for h in variables))
        # Creates a string that looks like the function that can be added to strings, so 'work_file.add(*[1,3])' turns into 'add(1,3)'
        try:
            # Tries to execute the function, and then tests if the answer is correct
            got_answer = func(*variables)
            # Executes the function with the arguments, and stores the answer in got_anwer
            if got_answer == answer:
                print("V - '{}' returned '{}' as expected".format(nice_print,str(answer)))
                # Prints that it is correct if it works and returns the right answer
            else:
                print("X - '{}' returned '{}', but expected {}".format(nice_print,str(got_answer),str(answer)))
                # Prints that it does work but doesn't return the right answer
        except Exception as e:
            # If an exception occurs, it stores it in 'e'
            print("X - Got Exception {} while trying to execute '{}'".format(str(e),nice_print))
            # Prints that it got an exception, and which exceptions


def test_add():
    # Tests the 'add' function
    test_cases = [[[1,2],[-1,3],["foo","bar"],[[1,3],[21,3]]],[3,2,"foobar",[1,3,21,3]]]
    test_func(work_file.add,"add",test_cases)
    # Explanation in test_func

def test_merge():
    # Tests the 'merge' function
    test_cases = [[[{1:2,4:6},{532:23,53:3}],[{"foo":{1:2,3:4}},{"bar":[1,3,4]}]],[{1:2,4:6,532:23,53:3},{"foo":{1:2,3:4},"bar":[1,3,4]}]]
    test_func(work_file.merge,"merge",test_cases)
    # Explanation in test_func

def test_digit_sum():
    # Tests the 'digit_sum' function
    test_cases = [[[43],[-43],[10001],[1233]],[7,7,2,9]]
    test_func(work_file.digit_sum,"digit_sum",test_cases)
    # Explanation in test_func

def test_new_tuple():
    # Tests the 'new_tuple' function
    test_cases = [[[1,2,3],["a"," ","text"]],[(1,2,3),("a"," ", "text")]]
    test_func(work_file.new_tuple,"new_tuple",test_cases)
    # Explanation in test_func

def test_sqrt():
    # Tests the 'sqrt' function
    test_cases = [[[9],[25],[14],[3]],[3,5,14**0.5,3**0.5]]
    test_func(work_file.sqrt,"sqrt",test_cases)
    # Explanation in test_func

def test_gcd():
    # Tests the 'gcd' function
    test_cases = [[[12,32],[-12,32],[-12,-32],[33,18]],[4,4,4,3]]
    test_func(work_file.gcd,"gcd",test_cases)
    # Explanation in test_func

def test_lcm():
    # Tests the 'lcm' function
    test_cases = [[[3,4],[1924,212],[707,708]],[12,101972,500556]]
    test_func(work_file.lcm,"lcm",test_cases)
    # Explanation in test_func

def test_distance_2d():
    # Tests the 'distance_2d' function
    test_cases = [[[(-4,-3),(8,2)],[(-132,-32),(84,32)],[(0.4,0.3),(0.1,0.7)]],[13,225.28204544525957,0.5]]
    test_func(work_file.distance_2d,"distance_2d",test_cases)
    # Explanation in test_func
    
def test_distance_3d():
    # Tests the 'distance_3d' function
    test_cases = [[[(1,1,1),(2,2,2)],[(12,-32,-12),(-32,-23,43)]],[1.7320508075688774,71.00704190430693]]
    test_func(work_file.distance_3d,"distance_3d",test_cases)
    # Explanation in test_func

def test_is_prime():
    # Tests the 'is_primed' function
    test_cases = [[[9],[1],[0],[7],[11],[28]],[False,False,False,True,True,False]]
    test_func(work_file.is_prime,"is_prime",test_cases)
    # Explanation in test_func

id_to_func = {'add':test_add,
              'merge':test_merge,
              'digit_sum':test_digit_sum,
              'new_tuple':test_new_tuple,
              'sqrt':test_sqrt,
              'gcd':test_gcd,
              'lcm':test_lcm,
              'distance_2d':test_distance_2d,
              'distance_3d':test_distance_3d,
              'is_prime':test_is_prime}

def main_loop():
    tested_func = 0
    while tested_func == 0:
        try:
            print("What is the id of the challenge you did?")
            challenge_id = input()
            id_to_func[challenge_id]()
            tested_func = 1
        except:
            print("id not recognised, please try again")
    input()


main_loop()
