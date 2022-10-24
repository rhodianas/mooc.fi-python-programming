# Write your solution here
year = int(input("Year:"))
added_years = 1
while True:
    if (year+added_years) % 4 == 0:
        if ((year+added_years) % 100 == 0 and (year+added_years) % 400 == 0) or (year+added_years) % 100 != 0:
            print(f"The next leap year after {year} is {year+added_years}")
            break
    added_years += 1
