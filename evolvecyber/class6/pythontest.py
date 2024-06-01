#!workspace/bin/python
import json


# Opening a file with python (reading)
# FILENAME = open("fruits.txt", "r")

# # Save into CONTENT variable 
# CONTENT = FILENAME.read()

# # Verify 
# print(CONTENT)
# print(type(CONTENT))  

# # manually close 
# FILENAME.close()

# with is a content manager
# with open("fruits.txt", "r") as FILENAME:
#     CONTENT = FILENAME.read()
#     print(CONTENT) 

with open("information.json", "r") as JSON_FILE:
    CONTENT = json.load(JSON_FILE)



print(type(CONTENT["class"]))

print(type(CONTENT["office"])) 

print(type(CONTENT["is_now_open"]))

print(type(CONTENT["instructors"]))

print(type(CONTENT["instructors"][0]))

# for items in CONTENT["instructors"]:
#     print(items) 

print("""
    At %s we do %s class. %s is located at %s %s. %s is %s 24/7. Current instructors are %s %s and %s %s 
    """ % (
    CONTENT["school"],
    CONTENT["class"],
    CONTENT["school"],
    CONTENT["office"],
    CONTENT["street"],
    CONTENT["school"],
    CONTENT["status"],
    CONTENT["instructors"][0]["instructor1"]["name"],
    CONTENT["instructors"][0]["instructor1"]["lastname"],
    CONTENT["instructors"][1]["instructor2"]["name"],
    CONTENT["instructors"][1]["instructor2"]["lastname"]
    ))

object = """
        At %s we do %s class. %s is located at %s %s. %s is %s 24/7. Current instructors are %s %s and %s %s 
    """ % (
    CONTENT["school"],
    CONTENT["class"],
    CONTENT["school"],
    CONTENT["office"],
    CONTENT["street"],
    CONTENT["school"],
    CONTENT["status"],
    CONTENT["instructors"][0]["instructor1"]["name"],
    CONTENT["instructors"][0]["instructor1"]["lastname"],
    CONTENT["instructors"][1]["instructor2"]["name"],
    CONTENT["instructors"][1]["instructor2"]["lastname"]
    )

with open("evolvesyber.txt", "w") as newfile:
    newfile.write(object)