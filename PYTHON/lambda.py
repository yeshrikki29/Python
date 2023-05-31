people = [
    {"name":"virat","team":"RCB"},
    {"name":"dhoni","team":"CSK"},
    {"name":"rohit","team":"MI"}
]

def y(person):
    return person["name"]

people.sort(key=y)

print(f"without using lambda {people}")



#anothe way to do by using lambda function

people.sort(key=lambda person: person["name"])

print(f"with using lambda  {people}")

