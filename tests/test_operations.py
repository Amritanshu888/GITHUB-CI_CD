from src.math_operations import add,sub

## Test cases
def test_add():
    assert add(2,3)==5 ## This assert statement is basically going to check whatever output i will get what this particular function is it equal to this.
    ## If its equal its going to give me true.
    assert add(-1,1)==0

def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1 

## I want my pytest library to check this specific usecases and see whether its working fine w.r.t the functions that i have.    