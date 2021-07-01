# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def damages_conversion(damages):
  temp = []
  for record in damages:
    if "B" in record:
      temp.append(float(record.strip("B")) * conversion.get("B"))
    elif "M" in record:
      temp.append(float(record.strip("M")) * conversion.get("M"))
    else:
      temp.append("Damages not recorded")
  return temp

# test function by updating damages
damages = damages_conversion(damages)

# 2 
# Create a Table

def create_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricane_data = {}
  for i in range(len(names)):
    hurricane_data[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages[i], "Death": deaths[i]}
  return hurricane_data

# Create and view the hurricanes dictionary
hurricanes_by_name = create_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
#print(hurricanes_by_name)

# 3
# Organizing by Year
def organize_by_year(dict_table):
  table_by_year = {}
  for v in dict_table.values():
    current_year = v.get("Year")
    if current_year not in table_by_year:
      table_by_year[current_year] = [v]
    else:
      table_by_year[current_year].append(v)
  return table_by_year
# create a new dictionary of hurricanes with year and key
hurricanes_by_year = organize_by_year(hurricanes_by_name)
#print(hurricanes_by_year)

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def dict_of_areas(dict_table):
  hurricane_areas = {}
  y = 1
  for value in dict_table.values():
    list_of_areas = value.get("Areas Affected")
    #print(list_of_areas)
    for i in list_of_areas:
      if i not in hurricane_areas:
        hurricane_areas[i] = [1]
      else:
        y += 1
        hurricane_areas[i] = [y]
  return hurricane_areas

hurricane_areas_affected = dict_of_areas(hurricanes_by_name)
#print(hurricane_areas_affected)

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def most_hits(areas_dict):
  fk_you_in_particular = ["N/A", 0]
  for k, v in areas_dict.items():
    if v[0] > fk_you_in_particular[1]:
      fk_you_in_particular = [k, v[0]]
  return fk_you_in_particular

most_likely_to_get_hit = most_hits(hurricane_areas_affected)
#print(most_likely_to_get_hit)

# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths
def death_becomes(dict_table):
  current_cane = "N/A"
  current_death_count = 0
  for k in dict_table:
    sub_dict = dict_table[k]
    if sub_dict["Death"] > current_death_count:
      current_death_count = sub_dict["Death"]
      current_cane = k
  highest_death_count = [current_cane, current_death_count]
  return highest_death_count

most_deaths = death_becomes(hurricanes_by_name)
#print(most_deaths)

# 7
# Rating Hurricanes by Mortality


# categorize hurricanes in new dictionary with mortality severity as key
def mortality_rating(dict_table):
  mortality_dict = {}
  for i in range(0,6):
    mortality_dict[i] = []
  for k in dict_table:
    sub_dict = dict_table[k]
    if sub_dict["Death"] > 10000:
      mortality_dict[5].append(sub_dict)
    elif sub_dict["Death"] > 1000 and sub_dict["Death"] <= 10000:
      mortality_dict[4].append(sub_dict)
    elif sub_dict["Death"] > 500 and sub_dict["Death"] <= 1000:
      mortality_dict[3].append(sub_dict)
    elif sub_dict["Death"] > 100 and sub_dict["Death"] <= 500:
      mortality_dict[2].append(sub_dict)
    elif sub_dict["Death"] > 0 and sub_dict["Death"] <= 100:
      mortality_dict[1].append(sub_dict)
    else:
      mortality_dict[0].append(sub_dict)
  return mortality_dict

hurricanes_by_mortality_scale = mortality_rating(hurricanes_by_name)
#print(hurricanes_by_mortality_scale)

# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def damage_becomes(dict_table):
  current_cane = "N/A"
  current_damage_count = 0
  for k in dict_table:
    sub_dict = dict_table[k]
    #print(sub_dict)
    if type(sub_dict["Damage"]) == float:
      if sub_dict["Damage"] > current_damage_count:
        current_damage_count = sub_dict["Damage"]
        current_cane = k
  highest_damage_count = [current_cane, current_damage_count]
  return highest_damage_count

most_damage = damage_becomes(hurricanes_by_name)
#print("The hurricane that caused the most damage is: " + str(most_damage))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def damage_rating(dict_table, scale):
  damage_dict = {}
  for i in range(0,6):
    damage_dict[i] = []
  for k in dict_table:
    sub_dict = dict_table[k]
    if type(sub_dict["Damage"]) == float:
      if sub_dict["Damage"] > scale[4]:
        damage_dict[5].append(sub_dict)
      elif sub_dict["Damage"] > scale[3] and sub_dict["Damage"] <= scale[4]:
        damage_dict[4].append(sub_dict)
      elif sub_dict["Damage"] > scale[2] and sub_dict["Damage"] <= scale[3]:
        damage_dict[3].append(sub_dict)
      elif sub_dict["Damage"] > scale[1] and sub_dict["Damage"] <= scale[2]:
        damage_dict[2].append(sub_dict)
      elif sub_dict["Damage"] > 0 and sub_dict["Damage"] <= scale[1]:
        damage_dict[1].append(sub_dict)
      else:
        damage_dict[0].append(sub_dict)
    else:
      damage_dict[0].append(sub_dict)
  return damage_dict

hurricanes_by_damage_scale = damage_rating(hurricanes_by_name,damage_scale)
#print(hurricanes_by_damage_scale)

