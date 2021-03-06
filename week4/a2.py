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

    return len(dna1) > len(dna2)
    # if len(dna1) > len(dna2):
    #     return True
    # else:
    #     return False


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return len([ntide for ntide in dna if ntide == nucleotide])
    # count = 0
    # for ntide in dna:
    #     if ntide == nucleotide:
    #         count += 1
    # return count

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1
    # if dna2 in dna1:
    #     return True
    # else:
    #     return False

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

    for nuc in sequence:
        if nuc not in 'ATCG':
            return False
    
    return True

    # valid = True
    # for nucleotide in sequence:
    #     count = 0
    #     valid_ltide = ['A', 'T', 'C', 'G']
    #     for r in valid_ltide:
    #         if nucleotide == r:
    #             count += 1
    #     if count < 1:
    #         valid = False

    # return valid

def insert_sequence(str1, str2, str_index):
    '''
    (str, str, int) -> str
    
    Return str2 inserted into str1 at str_index.

    >>>insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>>insert_sequence('CCGG', 'AT', 1)
    CATCGG
    '''

    return str1[:str_index] + str2 + str1[str_index:]


def get_compliment(nucleotide):
    '''
    (str) -> str

    Return nucleotide's compliment given that A & T are complimentary and C & G are complimentary.

    >>>get_compliment('A')
    T    
    >>>get_compliment('C')
    G
    '''
    compliment = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return compliment.get(nucleotide)
    # if nucleotide == 'A':
    #     return 'T'
    # elif nucleotide == 'T':
    #     return 'A'
    # elif nucleotide == 'C':
    #     return 'G'
    # elif nucleotide == 'G':
    #     return 'C'

def get_complementary_sequence(str1):
    '''
    (str) -> str

    Return the complimentary DNA sequence of str1.

    # The parameter is a DNA sequence. Return the DNA sequence that is complementary to the given DNA sequence.
    # For exmaple, if you call this function with 'AT' as the argument, it should return 'TA'.
    
    >>>get_complementary_sequence('ATCG')
    'TAGC'
    >>>get_complementary_sequence('AC')
    'TG'
    '''

    c_seq = ''
    for nuc in str1:
        c_seq += get_compliment(nuc)
    return c_seq