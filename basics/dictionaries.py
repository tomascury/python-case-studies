monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Set": "September",
    "Oct": "October",
    11: "November",
    12: "December"
}

print(monthConversion["Jan"])
print(monthConversion.get("Ads", "Not a valid Key"))
print(monthConversion.get(12, "Not a valid Key"))
