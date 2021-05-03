from BIO439_Exam4 import *

def test_find_possible():
    #test from assignment pdf
    expected = [4,8,7,6,5,4,3,2,1]
    actual = find_possible("ATTTGGATT")
    assert expected == actual

    #test small
    expected = [4,3,2,1]
    actual = find_possible("AGCG")
    assert expected == actual

    #test large 
    expected = [4,16,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
    actual = find_possible("TTCTCTATTGACCGTTTACTTGCC")
    assert expected == actual 

    #test all the same
    expected = [4,4,3,2,1]
    actual = find_possible("TTTTT")
    assert expected == actual

def test_find_observed():
    #test from assignment pdf
    expected = 6
    actual = find_observed("ATTTGGATT", 4)
    assert expected == actual

    #test small
    expected = 3
    actual = find_observed("AGCG", 1)
    assert expected == actual

    #test large 
    expected = 1
    actual = find_observed("TTCTCTATTGACCGTTTACTTGCC", 24)
    assert expected == actual

    #test all the same
    expected = 1
    actual = find_observed("TTTTT", 3)
    assert expected == actual

def test_comp_complexity():
    #test from assignment pdf
    expected = 35/40
    actual = comp_complexity([3,5,6,6,5,4,3,2,1], [4,8,7,6,5,4,3,2,1])
    assert expected == actual

    #test small
    expected = 9/10
    actual = comp_complexity([3,3,2,1], [4,3,2,1])
    assert expected == actual

    #test large
    expected = 267/273
    actual = comp_complexity([4,12,20,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1], [4,16,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1])
    assert expected == actual

    #test all the same
    expected = 5/14
    actual = comp_complexity([1,1,1,1,1], [4,4,3,2,1])
    assert expected == actual


    
