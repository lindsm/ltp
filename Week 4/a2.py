def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    if len(dna1) > len(dna2):
        return True
    else:
        return False


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    count = 0
    for ntide in dna:
        if ntide == nucleotide:
            count += 1
    return count

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    if dna2 in dna1:
        return True
    else:
        return False

def is_valid_sequence(sequence):
    '''
    (str) -> bool

    Return true if sequence contains only uppercase letter sequences of A, T, C, or G

    >>>is_valid_sequence('ATCG')
    True
    >>>is_valid_sequence('atcg')
    False
    >>>is_valid_sequence('ATCGX')
    False
    '''

    valid = True
    for nucleotide in sequence:
        count = 0
        valid_ltide = ['A', 'T', 'C', 'G']
        for r in valid_ltide:
            if nucleotide == r:
                count += 1
        if count < 1:
            valid = False

    return valid



# The parameter is a potential DNA sequence. Return True if and only if the DNA sequence is valid 
# (that is, it contains no characters other than 'A', 'T', 'C' and 'G'). There are at least 2 ways
# to approach this. One way is to count the number of characters that are not nucleotides and then
# at the end check whether there were more than zero. Another way is to use a Boolean variable that
# represents whether you have found a non-nucleotide character; it would start off as True and would
# be set to False if you found something that wasn't an 'A', 'T', 'C' or 'G'. You should construct
# examples that contain only 'A's, 'T's, 'C's and 'G's, and you should also create examples that 
# contain other characters. A string is not a valid DNA sequence if it contains lowercase letters.
