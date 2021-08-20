monthConversions = {
    #key  : value                       #keys need to be unique
    "jan": "january",
    "feb" : "february",
    "mar" : "march",
    "apr" : "april",
    "may" : "may",
    "jun" : "june",
    "jul": "july",
    "aug": "august",
    "sep": "september",
    "oct": "august",
    "nov": "november",
    "dec": "december",
}

print(monthConversions["jul"])          #refer to the key and get the value back
monthConversions.get("dec")     
monthConversions.get("ahdhsyhshw")      #doesnt give error if its not in the dict
monthConversions.get("ahsghhahwghs", "not a valid key")     #this is the default response if the key isnt in the dict        