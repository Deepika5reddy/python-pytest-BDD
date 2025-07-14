import json

#string variable
person = ''' {
  "name": "Deepika",
  "age": 30,
  "languages": ["Python", "JavaScript", "TypeScript"]
}'''

#load method parse json and returns dictionary

dict_person=json.loads(person)
type(dict_person)
print(type(dict_person))

print(dict_person["name"])
print(dict_person["age"])
print(dict_person["languages"][0])
#list data type
list_languages = dict_person["languages"]
print(type(list_languages))
print(list_languages[0])


#read from json file and parse

with open('C:\\Users\\Deepika\\OneDrive\\Desktop\\Deepika\\pytest\\course.json.txt') as file:
  data = json.load(file)
  #print(type(data))
  #print(data)
  #print(data["employee"]["name"])
  dist_contact =data["employee"]["contact"]
  #print(dist_contact)
  #print(dist_contact["email"])
  dist_skills = data["employee"]["skills"]
  #print(dist_skills) #output is list ['Python', 'JavaScript', 'Playwright', 'SQL']
  #print(dist_skills[3]) #sql

#read nested json
with open('C:\\Users\\Deepika\\OneDrive\\Desktop\\Deepika\\pytest\\nested.json.txt') as file:
  data1 = json.load(file)
  print(data1)
  items = data1["cart"]["items"]
  print(type(items))
  print(items)
  for itemname in items:
    print(itemname)
    if itemname["name"] == "Mouse":
      print(itemname["price"])
      assert itemname["price"] == 25.5

#compare 2 json file
 # assert data == data1

