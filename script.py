

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

def update_damage(damage):
  converted = []
  for cost in damage:
    if 'B' in cost:
      x = float(cost[:-1])
      converted.append(int(x*1000000000))
    elif 'M' in cost:
      x = float(cost[:-1])
      converted.append(int(x*1000000))
    else:
      converted.append(0)
  return converted
# test function by updating damages
damages = (update_damage(damages))


# 2 
# Create a Table
def name_table(names, months, years, maxs, areas, deaths):
  table = {}
  for i in range(34):
    table.update({names[i]: {'name':names[i], 'month': months[i], 'year': years[i], 'max sustained winds': maxs[i], 'areas affected': areas[i], 'damage':damages[i], 'deaths': deaths[i]}})
  return table




# Create and view the hurricanes dictionary
hurricanes_names = name_table(names, months, years, max_sustained_winds, areas_affected, deaths)
# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key
def year_table(names, months, years, maxs, areas, deaths):
  table = {}
  for i in range(34):
    table.update({years[i]:{'Name ':names[i], 'Month':months[i], 'Year':years[i], 'Max Sustained Wind':maxs[i], 'Areas affected': areas[i], 'Damage':damages[i], 'Deaths':deaths[i] }})
  return table

year_hurricane = year_table(names, months, years, max_sustained_winds, areas_affected, deaths)
# 4
# Counting Damaged Areas
def areas_table(areas):
  table = {}
  for hurricane in areas:
    for area in hurricane:
      if area in table:
        table[area]+=1
      else:
        table.update({area:1})
  return table
# create dictionary of areas to store the number of hurricanes involved in
areas_times = areas_table(areas_affected)

# 5 
# Calculating Maximum Hurricane Count
def max_area(areas_times):
  
  max_area = max(areas_times, key = areas_times.get)
  return max_area
# find most frequently affected area and the number of hurricanes involved in
maximal_area =max_area(areas_times)

# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(names, deaths):
  dict = {}
  for i in range(34):
    dict.update({names[i]:deaths[i]})

  all = dict.values()
  deadliest_name = max(dict, key = dict.get)
  deadliest_num = max(all)
  return {deadliest_name: deadliest_num}
# find highest mortality hurricane and the number of deaths
deadliest = deadliest_hurricane(names, deaths)
print(deadliest)
# 7
# Rating Hurricanes by Mortality
def mortality_scale_hurricanes(names, deaths):
  dict = {}
  
  scale = [[], [], [], [], []]
  for i in range(34):
    if deaths[i] < 100:
      nested = scale[0]
      nested.append(names[i])
      scale[0] = nested
    elif deaths[i] < 500 and deaths[i] >= 100:
      nested = scale[1]
      nested.append(names[i])
      scale[1] = nested
      
    elif deaths[i] < 1000 and deaths[i] >=500:
      nested = scale[2]
      nested.append(names[i])
      scale[2] = nested
    elif deaths[i] < 10000 and deaths[i] >= 1000:
      nested = scale[3]
      nested.append(names[i])
      scale[3] = nested
    elif deaths[i] >=10000:
      nested = scale[4]
      nested.append(names[i])
      scale[4] = nested
    
  for i in range(4):
    dict.update({i:scale[i]})
  return dict


# categorize hurricanes in new dictionary with mortality severity as key
mortal_scale = mortality_scale_hurricanes(names, deaths)

# 8 Calculating Hurricane Maximum Damage
def biggest_damage(names, damages):
  dict = {}
  for i in range(34):
    dict.update({names[i]:damages[i]})

  all = dict.values()
  max_damage_name = max(dict, key = dict.get)
  max_damage_num = max(all)
  return {max_damage_name: max_damage_num}
# find highest damage inducing hurricane and its total cost
print(biggest_damage(names, damages))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
              
  
# categorize hurricanes in new dictionary with damage severity as key
def hurricanes_by_damage(names, damages):
  dict = {}
  
  scale = [[], [], [], [], []]
  for i in range(34):
    if damages[i] < 100000000:
      nested = scale[0]
      nested.append(names[i])
      scale[0] = nested
    elif deaths[i] < 100000000 and deaths[i] >= 100000000:
      nested = scale[1]
      nested.append(names[i])
      scale[1] = nested
      
    elif deaths[i] < 1000000000 and deaths[i] >=100000000:
      nested = scale[2]
      nested.append(names[i])
      scale[2] = nested
    elif deaths[i] < 100000000 and deaths[i] >= 50000000000:
      nested = scale[3]
      nested.append(names[i])
      scale[3] = nested
    elif deaths[i] >=50000000000:
      nested = scale[4]
      nested.append(names[i])
      scale[4] = nested
    
  for i in range(4):
    dict.update({i:scale[i]})
  return dict

print(hurricanes_by_damage(names, damages))