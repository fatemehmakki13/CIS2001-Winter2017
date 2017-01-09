names = [ "Eric", "Robert", "Susan", "Aya", "Mike" ]
fixedNames = ( "Eric", "Robert", "Susan", "Aya", "Mike" )

print(names)

if "Mike" in names:
    names.remove("Mike")

print(names)

students = { 70761049 : "Eric",  1234567 : "Matt", 234567 : "Robert"  }

if 70761049 in students:
    print(students[70761049])
if 70761149 in students:
    print(students[70761149])
else:
    print("not found")

print(students.get(70761049,"not found"))
print(students.get(707671149,"not found"))

students[70761149] = "Eric"

print( students.keys() )
print( students.values() )
print( students.items() )

for id, name in students.items():
    print ("ID:", id, "name:",name)

for id in students.keys():
    print( "ID:", id, "name:",students[id])

for name in students.values():
    print( "Name:", name)