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

# test function by updating damages
def updated_damages(damages):
  float_damages = []
  for damage in damages:
    if ("not recorded" in  damage):
      float_damages.append(damage)
    elif("M" in damage):
      float_damages.append(float(damage.replace("M","")) * 1000000)
    elif("B" in damage):
      float_damages.append(float(damage.replace("B","")) * 1000000000)
  return float_damages

# 2 
# Create a Table
damages = updated_damages(damages)
# print(damages)
# Create and view the hurricanes dictionary

def constructor (Name, Month, Year, Max_Sustained_Wind, Areas_Affected, Damage, Death):
  dictionary = {}
  for i in range(len(names)):
    dictionary.update({Name[i]:{"Name": Name[i],"Month": Month[i],"Year": Year[i],"Max Sustained Wind": Max_Sustained_Wind[i],"Areas Affected": Areas_Affected[i],"Damage": Damage[i],"Deaths": Death[i]}})
  return dictionary
hurricanes = (constructor(names, months, years, max_sustained_winds, areas_affected, damages, deaths))


# 3
# Organizing by Year
def organizing_by_year(dictionary):
  organized_by_year = {}

  for key, value in hurricanes.items():
    organized_by_year.update({value["Year"]:value})
  return organized_by_year

# create a new dictionary of hurricanes with year and key
organized_by_year = organizing_by_year(hurricanes)
# 4
# Counting Damaged Areas
def counting_damaged_areas(hurricanes):

  nums_of_disasters_by_area = {}
  for value in hurricanes.values():
    for area in value["Areas Affected"]:
      if(area not in nums_of_disasters_by_area):
        nums_of_disasters_by_area[area] = 1
      else:
        nums_of_disasters_by_area[area] += 1
  return nums_of_disasters_by_area
# print(counting_damaged_areas(organized_by_year))
# create dictionary of areas to store the number of hurricanes involved in

hurricanes_count = counting_damaged_areas(organized_by_year)
# 5 
# Calculating Maximum Hurricane Count
def max_count_areas(hurricanes_count):
  bigger = 0
  key_ = 0
  for key,value in hurricanes_count.items():
    if(value > bigger):
      maior = value
      key_ = key
  return key_,bigger

# find most frequently affected area and the number of hurricanes involved in


# print(max_count_areas(hurricanes_count))

# 6
# Calculating the Deadliest Hurricane
def deadliest(names, deaths):
  deaths_by_hurricane = list(zip(names, deaths))
  more_deaths = 0
  hurricane = "Brazil"
  for name, deaths in deaths_by_hurricane:
    if(deaths > more_deaths):
      more_deaths = deaths
      hurricane = name
  return hurricane, more_deaths



# find highest mortality hurricane and the number of deaths

#print(deadliest(names, deaths))

# 7
# Rating Hurricanes by Mortality
def mortality_scale(hurricanes):
  new_dict = {}
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[]}
  mortality_scale_dict = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  for hurricane in hurricanes:
    temp = hurricanes[hurricane]
    for graduation in mortality_scale_dict:
      if temp["Deaths"] <= mortality_scale_dict[graduation] and temp["Deaths"] >mortality_scale_dict[graduation - 1]:
        hurricanes_by_mortality[graduation].append(temp)
  return hurricanes_by_mortality

# categorize hurricanes in new dictionary with mortality severity as key

# print(mortality_scale(hurricanes))

# 8 Calculating Hurricane Maximum Damage
def greatest_damage(names, damages):
  damages_by_hurricane = list(zip(names, damages))
  greatest_damage = 0
  hurricane = "Brazil"
  for name, damage in damages_by_hurricane:
    try:
      if(damage > greatest_damage):
        greatest_damage = damage
        hurricane = name
    except TypeError:
      continue;
  return hurricane, greatest_damage
# find highest damage inducing hurricane and its total cost
print(greatest_damage(names, damages))
# 9
# Rating Hurricanes by Damage
def damage_severity(hurricanes):
  new_dict = {}
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[]}
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  for hurricane in hurricanes:
    temp = hurricanes[hurricane]
    for graduation in damage_scale:
      if temp["Damage"] <= damage_scale[graduation] and temp["Damage"] >damage_scale[graduation - 1]:
        hurricanes_by_mortality[graduation].append(temp["Name"])
  return hurricanes_by_mortality
# print(mortality_scale(hurricanes))
