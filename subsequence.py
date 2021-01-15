num_list = [1, 2, 3, 4, 5]

# use length of subsequence to validate that it exists in larger sequence

# iterate over subsequecne first(?) then larger sequence
# if subseq[i] in list then ok
# if subseq[i + 1] in list after subseq[subseq[i]] then ok

subsequence = [5, 2, 3, 4]

# if the position of subseq[i] in array[j] > array[new j] false


def isValidSubsequence(array, sequence):
    # looping over the sequence as that is what i am checking
    for i in range(len(sequence)):
        # checking to see if current num is in array we're cross checking
        if sequence[i] in array:
            # if so, set oldj = index as it occurs in array
            old_ind = array.index(sequence[i])
        else:
            return False
        # checking to see if next numer in sequence is in array
        if sequence[i + 1] in array:
            # if so, set newj = index as it occurs in array again + 1 is because it is next number in sequence 
            new_ind = array.index(sequence[i + 1])
            # if the old position is greater than the new one - number must have occured later in the sequence so it is false
            if old_ind > new_ind:
                return False
            else:
                return True
        else:
            return False


print(isValidSubsequence(num_list, subsequence))