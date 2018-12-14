# "Service Name"   "Product Family"    "Observability/ Supportability"    "Quality"    "Cost Efficiency"
# "Compliance/ Privacy"    "Reliability/ Availability"    "Build/ Release"    "Security"
# "Scalability/ Performance"    "Common Architecture"    "Bronze Total"

import math


def bwf_dict():
    bwf_dictionary = {}

    for line in bwf_file:
        split_line = line.split(",")
        bwf_dictionary[split_line[0]] = {"Product Family": split_line[1],
                                         "MON": int(split_line[2].strip("%")),
                                         "QA": int(split_line[3].strip("%")),
                                         "COST": int(split_line[4].strip("%")),
                                         "COMP": int(split_line[5].strip("%")),
                                         "REL": int(split_line[6].strip("%")),
                                         "CICD": int(split_line[7].strip("%")),
                                         "SEC": int(split_line[8].strip("%")),
                                         "PERF": int(split_line[9].strip("%")),
                                         "ARCH": int(split_line[10].strip("%")),
                                         "TOTAL": int(split_line[11].strip("%\n"))}

    return bwf_dictionary


def bwf_average():
    total_svcs = 0
    total_total = 0

    for item in bwf_dictionary:
        total_total += bwf_dictionary[item]["TOTAL"]
        total_svcs += 1

    return "Total Services: " + str(total_svcs) + " " "Average BWF Score: " + str(total_total / total_svcs * 100)


bwf_file = open("bwf.csv", "r")

# create the dictionary
bwf_dictionary = bwf_dict()

print(bwf_dictionary)

# calculate the average
print(bwf_average())

# Always close the connections to your files :)
bwf_file.close()
