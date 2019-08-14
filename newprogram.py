print ("Welcome to the Natural Hair Directory!")

name = input("What's your name?")
print ("Hello! Nice to meet you,", name)

print ("The purpose of this program is to help you determine the best products for your hair type.")
print ("Natural hair is extremely diverse, so not everyone will have the same needs.  Let's get started!")

hair = input("What is your curl type: 2, 3, or 4?")
hair = int(hair)
if hair == 3:
    print ("You might want to try a light moisture milk by Shea Moisture.")
elif hair > 3:
    print ("You have a tighter curl pattern.  Try some whipped shea butter.")
elif hair < 3:
    print ("Your hair is probably wavy.  Lighter oils, like grapeseed oil, would be best for you.")

porosity = input("What is your porosity: low, medium, or high?")
if porosity == "high":
    print ("Try protein to strengthen your strands.")
elif porosity == "low":
    print ("Low porosity needs heat to absorb moisture. Use a steamer or hooded dryer.")
elif porosity == "medium":
    print ("You won the hair lottery! Alternate between heat and protein regularly.")

dry = input("Does yor hair feel dry if you wash it once a week?")
if frequency =- "yes"
    print ("Consider washing yor hair every two weeks instead. Washing too frequently strips it of moisture."
)