def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    
    our_list = our_string.strip().split(" ")
    if len(our_list) < 2:
        return our_string[::-1]
    else:
        flip = [word[::-1] for word in our_list]
        
    
    return ' '.join(flip)
