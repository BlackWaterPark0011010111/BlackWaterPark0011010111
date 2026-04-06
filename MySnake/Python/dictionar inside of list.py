shopping_list =[
    {
 "products": "potato",
 "number" :1, 
 "price" :"2$"
 }, 

 {
  "products": "tomato",
  "number" :1, 
  "price" :"3$"
 },
                        
{
  "products": "pomegranate",
  "number" : 3,
  "price" : "4$"
 },

{                    
  "products" : "pumpkin",
  "number" : 7, 
  "price" : 6,

 },

 {
  "products" : "vanilla",
  "number" : 2,
  "price" : "6$",
 }
]

add_list = [
    {
        "products": "carrot",
        "number" :5, 
        "price" :"2.5$"
    },

    {
        "products": "onion",
        "number" :3, 
        "price" :"3.9$"
    } ]

shopping_list.extend(add_list)


shopping_list.pop(1)
shopping_list[3]["number"] = 3

print(shopping_list)


 