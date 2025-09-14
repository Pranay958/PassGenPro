import random
import string
import math

# Moderate Enhancement
def moderate_password(password):
    if not password:
        return ""
    
    digits = string.digits
    symbols = "!@#$%&*?"
    chars = list(password)

    # Capitalize first letter
    chars[0] = chars[0].upper()

    # Replace letters with symbols/digits (leet-style)
    replace_map = {"a":"@", "s":"$", "i":"1", "o":"0", "e":"3", "t":"7"}
    for i, c in enumerate(chars):
        if c.lower() in replace_map and random.random() < 0.3:
            chars[i] = replace_map[c.lower()]

    # Ensure at least one digit and one symbol
    if not any(c.isdigit() for c in chars):
        chars.append(random.choice(digits))
    if not any(c in symbols for c in chars):
        chars.append(random.choice(symbols))

    # Add one extra random character
    chars.append(random.choice(digits + symbols))

    # Shuffle only extra characters
    core = chars[:len(password)]
    extras = chars[len(password):]
    random.shuffle(extras)

    return ''.join(core + extras)

# Strong Enhancement (Readable)
def strong_password_readable(password):
    """
    Enhances password based on user input, keeps it readable
    and related to the original, but adds moderate complexity.
    """
    if not password:
        return ""

    # Start with moderate enhancement
    enhanced = moderate_password(password)

    # Add 1-2 extra readable characters (letters or digits)
    pool = string.ascii_letters + string.digits
    enhanced += ''.join(random.choices(pool, k=2))

    return enhanced

# Password Strength
def password_strength(password):
    pool_size = 0
    if any(c.islower() for c in password): pool_size += 26
    if any(c.isupper() for c in password): pool_size += 26
    if any(c.isdigit() for c in password): pool_size += 10
    if any(c in string.punctuation for c in password): pool_size += len(string.punctuation)

    if pool_size == 0: return "Weak"
    entropy = len(password) * math.log2(pool_size)

    if entropy < 40: return "Weak"
    elif entropy < 60: return "Moderate"
    else: return "Strong"

# Menu System 
def main():
    print("=== Password Enhancer ===")
    password = input("Enter your password: ")

    print("\nChoose enhancement level:")
    print("1 - Moderate")
    print("2 - Strong (readable)")
    choice = input("Enter choice (1 or 2): ")

    if choice == "2":
        enhanced = strong_password_readable(password)
    else:
        enhanced = moderate_password(password)

    print("\nOriginal Password :", password)
    print("Enhanced Password :", enhanced)
    print("Password Strength :", password_strength(enhanced))

if __name__ == "__main__":
    main()
