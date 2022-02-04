import code_55_jump_game as c1

def test_example_1():
    s = c1.Solution()
    assert s.canJump([2,3,1,1,4]) == True

def test_example_2():
    s = c1.Solution()
    assert s.canJump([3,2,1,0,4]) == False

def test_first_failure():
    s = c1.Solution()
    assert s.canJump([1,2,3]) == True

def test_second_failure():
    s = c1.Solution()
    assert s.canJump([1,0,1,0]) == False

def test_currently_stuck():
    s = c1.Solution()
    assert s.canJump([1,0,2,2,0]) == False