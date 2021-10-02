#counties_dict = {"A":422829,"D":463353,"J":432438}
#for county,voters in counties_dict.items():
 #print (f"{county} county has {voters} registered voters")
voting_data =  [{"county":"A","voters":422829},{"county":"D","voters":413229},{"county":"J","voters":432438}]
for county_dict in voting_data:
  print(f"{county_dict['county']} county has {county_dict['voters']} registered voters")