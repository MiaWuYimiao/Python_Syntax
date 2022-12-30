def print_upper_words(words, must_start_with = {'e'}):
    """ print out word in a list on separate lines in all uppercase

        >>> print_upper_words(["Programming", "is", "pretty", "fun"])
 
        >>> print_upper_words(["eagle", "Edward", "Alfred"])
        EAGLE
        EDWARD

        >>> print_upper_words(["eagle", "Edward", "Alfred", "zope"],
        ...                   must_start_with=["A", "E"])
        EDWARD
        ALFRED
    """
    for word in words:
        for ltr in must_start_with:
            if word.lower().startswith(ltr):
                print(f"{word.upper()}")
                break

