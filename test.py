work_file_name = "work_file_example"
work_file = __import__(work_file_name)

def add_commas(string):
    if isinstance(string,str):
        return("'" + string + "'")
    return(string)

def test_func(func,func_name,test_cases):
    # func is the function it should use
    # func_name is the name it should use in the printed text
    #
    # test_cases is a list composed of two smaller lists. The arguments and the answers
    # test_cases = [ [arguments] , [answers] ]
    # arguments consists of lists, each list being a set of arguments to pass on to the function
    # 
    #
    #
    for i in range(len(test_cases[0])):
        variables = test_cases[0][i]
        answer = test_cases[1][i]
        try:
            got_answer = func(*variables)
            nice_print = "{}({})".format(func_name,",".join(str(add_commas(h)) for h in variables))
            if got_answer == answer:
                print("V - '{}' returned '{}' as expected".format(nice_print,str(answer)))
            else:
                print("X - '{}' returned '{}', but expected {}".format(nice_print,str(got_answer),str(answer)))
        except Exception as e:
            print("X - Got Exception {} while trying to execute '{}'".format(str(e),nice_print))  
    
def test_add():
    test_func(work_file.add,"add",[[[1,2],[-1,3],["foo","bar"],[[1,3],[21,3]]],[3,2,"foobar",[1,3,21,3]]])
    # Explanation in test_func
    
        
