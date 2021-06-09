integer_list = [1,3,1,2,3,8,2,4,0,5,8,9,2,8]
def CirclePair(integer_list):
    first = 0
    second = 1
    pair = 0
    length_list = len(integer_list)
    loop_iterate = (int(length_list/2))

    for i in range(loop_iterate):
        sum_int = integer_list[first]+integer_list[second]
        if sum_int%2==0:
            pair=pair+1
            first=first+2
            second=second+2
        else:
            first=first+2
            second=second+2
    print("cicle pair even is ",pair)
CirclePair(integer_list)
  
