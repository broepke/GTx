# "Service Name"   "Product Family"    "Observability/ Supportability"    "Quality"    "Cost Efficiency"
# "Compliance/ Privacy"    "Reliability/ Availability"    "Build/ Release"    "Security"
# "Scalability/ Performance"    "Common Architecture"    "Bronze Total"

import math

bwf_dictionary = {}
counter = 0

bwf_file = open("bwf.csv", "r")

for line in bwf_file:
    split_line = line.split(",")
    bwf_dictionary["Service Name"] = split_line[0]
    bwf_dictionary["Product Family"] = split_line[1]
    bwf_dictionary["MON"] = int(split_line[2].strip("%"))
    bwf_dictionary["QA"] = int(split_line[3].strip("%"))
    bwf_dictionary["COST"] = int(split_line[4].strip("%"))
    bwf_dictionary["COMP"] = int(split_line[5].strip("%"))
    bwf_dictionary["REL"] = int(split_line[6].strip("%"))
    bwf_dictionary["CICD"] = int(split_line[7].strip("%"))
    bwf_dictionary["SEC"] = int(split_line[8].strip("%"))
    bwf_dictionary["PERF"] = int(split_line[9].strip("%"))
    bwf_dictionary["ARCH"] = int(split_line[10].strip("%"))
    bwf_dictionary["TOTAL"] = int(split_line[11].strip("%\n"))
    # print(bwf_dictionary)

    counter += 1

print(counter)

bwf_file.close()

# Service Name,Product Family,Observability/ Supportability,Quality,Cost Efficiency,Compliance/ Privacy,
# Reliability/ Availability,Build/ Release,Security,Scalability/ Performance,Common Architecture,Bronze Total
