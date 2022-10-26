
def is_two(x):
    """
    Return True if the passed input is either the number
        or the string 2, False otherwise.
    Args: str
    Output: bool
    """
    return True if int(x)==2 else False

def is_vowel(x):
    """
    Return True if the passed string is a vowel,
    False otherwise.
    Args: str
    Output: bool
    """
    return True if x.lower() in [c for c in 'aeiou'] else False


def is_cons(x):
    """
    Return True if the passed string is a consonant,
    False otherwise.
    Args: str
    Output: bool
    """
    return True if x.lower() in [c for c in \
     'qwrtypsdfghjklzxcvbnm'] else False

def capital_cons(x):
    """
    Capitalize the first letter of the word if the word
    starts with a consonant.
    Args: str
    Output: str
    """
    return x.capitalize() if is_cons(x[0]) else x

def calculate_tip(tip, bill):
    """
    Accept a tip percentage between 0 and 1 and the
    bill total, and return the amount to tip.
    Args: float, float
    Output: float
    """
    return "$"+str(tip*bill)

def discount(discount, price):
    """
    Accept a original price, and a discount percentage,
    and return the price after the discount is applied.
    Args: float, float
    Output: float
    """
    return price*(1-discount)

def no_commas(s):
    """
    Accept a string that is a number that contains commas
    in it as input, and return a number as output.
    Args: str
    Output: float
    """
    return int(s.replace(',',''))

def letter_grade(n):
    """
    Accept a number and return the letter grade associated
    with that number (A-F).
    Args: int
    Output: str
    """
    return 'A' if n >= 90 else 'F'

def no_vowels(s):
    """
    Accepts a string and returns a string with all the
    vowels removed.
    Args: str
    Output: str
    """
    return ''.join([c for c in s if c not in 'aeiou'])

def norm_name(s):
    """
    Accept a string and return a valid python identifier:
    First Name will become first_name
    Args: str
    Output: str
    """
    return '_'.join(s.split()).lower().strip()

def cumsum(n):
    """
    Accepts a list of numbers and returns a list that
    is the cumulative sum of the numbers in the list.
    Args: list
    Output: list
    """
    return [sum(n[:ix+1]) for ix,_ in enumerate(n)]


if __name__ == "__main__":
    print(is_two('2'))
    print(is_vowel('a'))
    print(is_vowel('L'))
    print(is_cons('L'))
    print(capital_cons('library'))
    print(capital_cons('apple'))
    print(calculate_tip(.15,565.))
    print(discount(.15,565.))
    print(letter_grade(90))
    print(no_commas('1,002'))
    print(no_vowels('My little horse must think it queer'))
    print(norm_name(' Nathaniel Hawthorne'))
    print(cumsum([1,1,2,3,5]))


