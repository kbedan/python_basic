#unordered collection of items
#dictionary are mutable
#use {} to create a dictionary
#items are stored in key:value pairs
#each key:value pair is separated by a comma

"""
NB:
*keys should be of immutable data type ie int ,float,boolean,tuple
* values can be of any datatype

"""

a= {
    1:"one",
    1.2:(1,2,3),
    True:{
        "name":"John"
    },
    (1,2,3) :[1,2,3]
}
print(type(a))


#access items from a dictionary
print(a[True])
print(a.get(1))



my_details= {
    "first_name":"Kivuti",
    "last_name": "Brian",
    "age":34,
    "interest":["cooking","swimming","soccer"],
    "school1_details":{
        "primary":{
            "school1":{
                "name":"Wendani Junior",
                "founded":2000,
                "director":{
                    "first_name":    "Mark",
                    "Lastname":     "Kariuki",
                    "religion":     "christian",
                    "gender":       "male"
                }
            }
        }
    },
    "secondary":{},
    "University":{}
}

print(my_details["school1_details"]["primary"]["school1"]["director"]["first_name"])