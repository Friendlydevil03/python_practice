# String Inbuilt Methods Demo
text = "  hello world  "
sample = "Python123"
alpha = "Python"
num = "12345"
title_str = "Hello World"
mixed = "PyThOn"
lines = "Hello\nWorld\nPython"

print("=== CASE CONVERSION ===")
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(mixed.swapcase())

print("\n=== SEARCHING & FINDING ===")
print("find:", "banana".find("na"))
print("rfind:", "banana".rfind("na"))
print("index:", "banana".index("na"))
print("rindex:", "banana".rindex("na"))
print("count:", "banana".count("a"))
print("startswith:", "hello".startswith("he"))
print("endswith:", "hello".endswith("lo"))

print("\n=== VALIDATION / CHECK ===")
print("isalpha:", alpha.isalpha())
print("isdigit:", num.isdigit())
print("isalnum:", sample.isalnum())
print("islower:", "hello".islower())
print("isupper:", "HELLO".isupper())
print("istitle:", title_str.istitle())
print("isspace:", "  ".isspace())
print("isnumeric:", "Ⅻ".isnumeric())
print("isdecimal:", num.isdecimal())
print("isidentifier:", "name".isidentifier())
print("isascii:", "Hello".isascii())

print("\n=== MODIFICATION & REPLACEMENT ===")
print("replace:", "apple".replace("p", "b"))
print("strip:", text.strip())
print("lstrip:", text.lstrip())
print("rstrip:", text.rstrip())
print("join:", " ".join(["I", "love", "Python"]))
print("split:", "a,b,c".split(","))
print("rsplit:", "a,b,c".rsplit(",", 1))
print("splitlines:", lines.splitlines())
print("center:", "hi".center(10, "*"))
print("ljust:", "hi".ljust(10, "."))
print("rjust:", "hi".rjust(10, "."))
print("zfill:", "42".zfill(5))

print("\n=== ENCODING & TRANSLATION ===")
table = str.maketrans("aeiou", "12345")
print("maketrans + translate:", "apple".translate(table))
print("encode:", "hello".encode())

print("\n=== FORMATTING ===")
print("format:", "{} is {}".format("Python", "fun"))
print("format_map:", "{name} is {age}".format_map({"name": "Bob", "age": 20}))
name, age = "Alice", 25
print(f"f-string: {name} is {age}")

print("\n=== ALL DONE ===")
