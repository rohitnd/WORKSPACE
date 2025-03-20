name = "Sasha"   #The usual print function for text

print(name)

name = "Sasha" #Slicing text / Substring
print(name[1:4])

name = "Sasha" #String Indexing(Character look up)
print(name[1])
print(name[-1])
print(name[-3])
print(name[0])

text = "This is a very looooooooooooooooong message"
print(len(text)) #len function to check message length in int format.

text = "Pineapple" 
print(text[:4])   #Including only one of the indexies - this is "Nothing to 4th Index(3 character)"
print(text[4:])   # This is "4th Character to the last one."

message = "Such a kong boring day"  #Type error in string, we would like to change the word "kong" to "long"
#if we use the indexing feature to change the character it will show ERROR, because strings in Pythong are immutable.
#hence we do the following steps:
new_message = message[:7] + "l" + message[8:]
print(new_message) #prints "Such a long boring day"

def replace_email(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
replace_email("rohit@narrys.com","narrys.com","narryswholesale.com")

name = "Manny"
number = len(name) * 3
print("Hello {}. Your lucky number is {}".format(name, number))

name = "Manny"
number = len(name) * 3
print("Hello {}. Your lucky number is {}.".format(name, number))
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))


def to_celsius(x):
    return (x-32) * 5/9
for x in range (0,101,10):
    print("{:>3} F | {:>6.1f} C".format(x, to_celsius(x)))

basket = [ 
("Peaches", 3.0, 2.99),
("Pears", 5.0, 1.66),
("Plums", 2.5, 3.99)
]

subtotal = 0.00
for item in basket:
    fruit, weight, unit_price = item
    subtotal += (weight * unit_price)
    tax_rate = 0.06625
    tax_amt = subtotal*tax_rate
    total = subtotal + tax_amt
print("Subtotal:      ${:5,.2f}".format(subtotal))
print("Sales Tax:     ${:5,.2f}".format(tax_amt))
print("Total:         ${:5,.2f}".format(total))  


def mirrored_string(my_string):
    forwards = ""
    backwards = ""
    for character in my_string:
        if character.isalpha():
            forwards += character
            backwards = character + backwards
    if forwards.lower() == backwards.lower():
        return True
    return False

print(mirrored_string("12 Noon"))
print(mirrored_string("Nice person to have met"))
print(mirrored_string("'eve, Madam Eve"))


def convert_ounces(ounces):
    pounds = ounces/16
    result = "{} ounces equals {:.2f} pounds".format(ounces, pounds)
    return result
print(convert_ounces(12.5))
print(convert_ounces(12))
print(convert_ounces(50.5))
print(convert_ounces(16))

def username(last_name, birth_year):
    return ("{}{}".format(last_name[3:], birth_year[2:]))
print(username("Daryanani", "1991"))
print(username("Padania", "1992"))

def replace_date(schedule, old_date, new_date):
    if schedule.endswith(old_date):
        p = len(old_date)
        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)
    return new_schedule

print(replace_date("Last years annual report will be relased in March 2023", "2023", "2024"))

multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples) 

multiples = [x*7 for x in range(1,11)]
print(multiples)
    
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

z = [x for x in range (0,101) if x % 3 == 0]
print(z)
