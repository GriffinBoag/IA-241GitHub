'''
lab4 dict and tuple
'''

#4.1
my_dict = {
'name':' Tom',
'id': 123
}

print(my_dict) 

#4.2
print(my_dict.values())
print(my_dict.keys())

#4.3
my_dict['id']=321
print(my_dict)

#4.4
my_dict.pop('name',None) 
print(my_dict) 

#4.5
my_tweet = {
"tweet_id":1138,
"coordinates": (-75, 40),
"visited_countries": ["GR", "HK", "MY"]
}

print(my_tweet) 

#4.6
print(len(my_tweet["visited_countries"]))

#4.7
my_tweet["visited_countries"].append("CH") 
print(my_tweet) 

#4.8
print("US" in my_tweet["visited_countries"]) 

#4.9
#(-81,45)
my_tweet["coordinates"]=(-81,45)
print(my_tweet) 