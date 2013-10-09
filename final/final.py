def count_max_letters(s1, s2, letter):
    '''(str, str, str) -> int

    s1 and s2 are strings, and letter is a string of length 1.  Count how many
    times letter appears in s1 and in s2, and return the bigger of the two
    counts.

    >>> count_max_letters('hello', 'world', 'l')
    2
    >>> count_max_letters('cat', 'abracadabra', 'a')
    5
    '''

    return max(s1.count(letter), s2.count(letter))


def both_start_with(s1, s2, prefix):
    '''(str, str, str) -> bool

    Return True if and only if s1 and s2 both start with the letters in prefix.
    '''
    # if s1.startswith(prefix) and s2.startswith(prefix):
    #     return True
    # else:
    #     return False

    return 

def gather_every_nth(L, n):
    '''(list, int) -> list

    Return a new list containing every n'th element in L, starting at index 0.

    Precondition: n >= 1

    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)
    [0, 3]
    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
    ['a', 'c', 'e', 'g', 'i']
    '''

    result = []
    i = 0
    while i < len(L):
        result.append(L[i])
        i = i + n

    return result    

def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    '''

    result = []
    for k in L:
        if k in d:
            result.append(k)

    return result

def are_lengths_of_strs(L1, L2):
    '''(list of int, list of str) -> bool

    Return True if and only if all the ints in L1 are the lengths of the strings
    in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    '''

    result = True
    for i in range(len(L1)):
        if L1[i] != len(L2[i]):
            result = False

    return result

def double_values(collection):
    for v in range(len(collection)):
        collection[v] = collection[v] * 2

def get_diagonal_and_non_diagonal(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):

            if row == col:
                diagonal.append(L[row][col])

            non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)


def count_chars(s):
    '''(str) -> dict of {str: int}

    Return a dictionary where the keys are the characters in s and the values
    are how many times those characters appear in s.

    >>> count_chars('abracadabra')
    {'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
    '''
    d = {}

    for c in s:
        if not (c in d):
            d[c] = 1
        else:
            d[c] = d[c] + 1

    return d