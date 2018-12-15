# "Service Name"   "Product Family"    "Observability/ Supportability"    "Quality"    "Cost Efficiency"
# "Compliance/ Privacy"    "Reliability/ Availability"    "Build/ Release"    "Security"
# "Scalability/ Performance"    "Common Architecture"    "Bronze Total"

import math


def bwf_dict():
    bwf_dictionary = {}

    for line in bwf_file:
        split_line = line.split(",")
        bwf_dictionary[split_line[0]] = {"Family": split_line[1],
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
    total_total = 0

    for item in bwf_dictionary:
        total_total += bwf_dictionary[item]["TOTAL"]

    return "Total Services: " + str(len(bwf_dictionary)) + " " "Average BWF Score: " + str(
        round((total_total / len(bwf_dictionary)), 2)) + "%"


def bwf_stddev():
    total = 0
    sum_of_diffs = 0

    # Find the mean of the list
    for item in bwf_dictionary:
        total += bwf_dictionary[item]["TOTAL"]
        total += 1

    mean = total / len(bwf_dictionary)

    # calculate the std. deviation
    for item in bwf_dictionary:
        diff = bwf_dictionary[item]["TOTAL"] - mean
        diff = diff ** 2
        sum_of_diffs += diff

    # get the mean of the total
    sum_of_diffs = sum_of_diffs / len(bwf_dictionary)

    # Get the sqr. root
    std_dev = math.sqrt(sum_of_diffs)

    return "The standard deviation is: " + str(std_dev)


def bwf_bronze_complete():
    total = 0

    for item in bwf_dictionary:
        if bwf_dictionary[item]["TOTAL"] == 100:
            total += 1

    return "There are " + str(total) + " services that have met bronze"


def bwf_percentiles():
    low_range = 0
    mid_range = 0
    high_range = 0
    audit_range = 0

    for item in bwf_dictionary:
        if bwf_dictionary[item]["TOTAL"] < 50:
            low_range += 1
        elif 50 < bwf_dictionary[item]["TOTAL"] < 75:
            mid_range += 1
        elif 75 < bwf_dictionary[item]["TOTAL"] < 90:
            high_range += 1
        elif bwf_dictionary[item]["TOTAL"] >= 90:
            audit_range += 1

    return str(low_range) + " services are less than 50%, " + str(mid_range) + " services are 51%-75% and " + str(
        high_range) + " are 75% or higher and " + str(audit_range) + " services are 90%+ complete"


# open the file and create an ojbect
bwf_file = open("bwf.csv", "r")

# create the dictionary
bwf_dictionary = bwf_dict()

# calculate the average
print(bwf_average())

# Get Standard Deviation
print(bwf_stddev())

# Get the total number of services at 100%
print(bwf_bronze_complete())

# Get BWF Percentile Ranges
print(bwf_percentiles())

# Always close the connections to your files :)
bwf_file.close()
