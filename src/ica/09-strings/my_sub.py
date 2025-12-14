def name_subst(name, text):
    """
    Replaces every occurrence of the string "ZZZ" in the given text
    with the provided name, and returns the resulting string.
    """
    new_text = text.replace("ZZZ", name)
    return new_text

sallie = name_subst("Sallie", "My friend, ZZZ, won an award.")
print(sallie)
print(name_subst("Fred", "Jamie and ZZZ flew over the trees."))
