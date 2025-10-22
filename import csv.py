# Name: LooLu Wiltse
# Student Id: 9311 3760
# Email: looluwi@umich.edu
# AI Usage Statement: I mainly use AI Overview on Google to try to help explain coding concepts I need to refamiliarize myself with.
#   I also referenced UM-GPT to help give me ideas for test cases for my functions after showing it my functions. 
#   I did NOT ask UM-GPT to write my code for me.

import csv
import unittest

def load_data():
    #opening the penguins.csv file
    file_obj = open("penguins.csv")
    data = [] #initializing list of dictionaries, storing data from penguins.csv
    for line in file_obj: #iterating through line, adding each to data
        line = line.rstrip()
        line = line.split(",")
        data.append(line)
    print(data) #displaying what data now contains
    data2 = data #creating a new copy of data to modify
    data2[0][0] = data[0][0] = "number" #changing first column and first row to "number"
    print(data2[0]) #displaying new modified copy
    data2[0][1] = data[0][1] = "species"
    data2[0][2] = data[0][2] = "island"
    data2[0][3] = data[0][3] = "bill_length_mm"
    data2[0][4] = data[0][4] = "bill_depth_mm"
    data2[0][5] = data[0][5] = "flipper_length_mm"
    data2[0][6] = data[0][6] = "body_mass_g"
    data2[0][7] = data[0][7] = "sex"
    data2[0][8] = data[0][8] = "year"
    
    head = data2[0] #isolating general labels for information of penguins
    info = data2[1:] #creating nested list of just penguin data, no header

    fdata = [] #initializing list, creating list of dictionaries
    for item in info: #aiming to create list of dictionaries, keys being categories, values being individual data
        d = {}
        for i in range(len(head)):
            d[head[i]] = item[i]
        fdata.append(d)
    #fdata is final list of dictionaries, including missing values

    return fdata

#Below will be working on calculations

#First calculation: Determining sex ratios of penguins per island, per species

def sex_ratio(fdata, newfile):
    #D is a triple-nested dictionary, with keys being island names, inner dictionaries as species breakdowns, and inner dictionaries
    # as a sex-binary initialized to zeroes
    d = {
        '"Torgersen"': {'"Adelie"': {"Male": 0, "Female": 0}, '"Gentoo"': {"Male": 0, "Female": 0}, '"Chinstrap"': {"Male": 0, "Female": 0}},
        '"Dream"': {'"Adelie"': {"Male": 0, "Female": 0}, '"Gentoo"': {"Male": 0, "Female": 0}, '"Chinstrap"': {"Male": 0, "Female": 0}},
        '"Biscoe"': {'"Adelie"': {"Male": 0, "Female": 0}, '"Gentoo"': {"Male": 0, "Female": 0}, '"Chinstrap"': {"Male": 0, "Female": 0}},
    }
    num = 0
    for item in fdata:
        if item["sex"] == '"male"':
            d[item["island"]][item["species"]]["Male"] +=1
        elif item["sex"] == '"female"':
            d[item["island"]][item["species"]]["Female"] += 1
    
    newfile.write("Ratios of Males to Female, by Island, by Species: \n")
    newfile.write("Torgersen: \n")
    newfile.write(f"     Adelie: {d['"Torgersen"']['"Adelie"']["Male"]}:{d['"Torgersen"']['"Adelie"']["Female"]}, Gentoo: {d['"Torgersen"']['"Gentoo"']["Male"]}:{d['"Torgersen"']['"Gentoo"']["Female"]}, Chinstrap: {d['"Torgersen"']['"Chinstrap"']["Male"]}:{d['"Torgersen"']['"Chinstrap"']["Female"]} \n")
    newfile.write("Dream: \n")
    newfile.write(f"     Adelie: {d['"Dream"']['"Adelie"']["Male"]}:{d['"Dream"']['"Adelie"']["Female"]}, Gentoo: {d['"Dream"']['"Gentoo"']["Male"]}:{d['"Dream"']['"Gentoo"']["Female"]}, Chinstrap: {d['"Dream"']['"Chinstrap"']["Male"]}:{d['"Dream"']['"Chinstrap"']["Female"]} \n")
    newfile.write("Biscoe: \n")
    newfile.write(f"     Adelie: {d['"Biscoe"']['"Adelie"']["Male"]}:{d['"Biscoe"']['"Adelie"']["Female"]}, Gentoo: {d['"Biscoe"']['"Gentoo"']["Male"]}:{d['"Biscoe"']['"Gentoo"']["Female"]}, Chinstrap: {d['"Biscoe"']['"Chinstrap"']["Male"]}:{d['"Biscoe"']['"Chinstrap"']["Female"]} \n")
    return d

   
class test_sex_ratio(unittest.TestCase):
   
   #General cases
   #Testing if function can write to csv and txt files successfully
    def testWritingTo_txt_or_csv_file(self):
        sampleCSV = load_data()

        file = open("file1.csv", "w")
        file2 = open("file2.txt", "w")

        d1 = {
        '"Torgersen"': {'"Adelie"': {"Male": 0, "Female": 0}, '"Gentoo"': {"Male": 0, "Female": 0}, '"Chinstrap"': {"Male": 0, "Female": 0}},
        '"Dream"': {'"Adelie"': {"Male": 0, "Female": 0}, '"Gentoo"': {"Male": 0, "Female": 0}, '"Chinstrap"': {"Male": 0, "Female": 0}},
        '"Biscoe"': {'"Adelie"': {"Male": 0, "Female": 0}, '"Gentoo"': {"Male": 0, "Female": 0}, '"Chinstrap"': {"Male": 0, "Female": 0}},
        }

        return self.assertEqual(sex_ratio(sampleCSV, file), sex_ratio(sampleCSV, file2))
        
    #Testing to see if dictionary values from sex_ratio() can be accessed and compared to
    def testCountSame(self):
        csvFile = load_data()
        file = open("f3.txt", "w")
        dic1 = sex_ratio(csvFile, file)
        self.assertNotEqual(dic1['"Torgersen"']['"Adelie"']["Male"], dic1['"Torgersen"']['"Adelie"']["Female"])

    
    #edge cases
    #Testing if changing all values to NA will lead to a value in the dictionary being zero, since no males nor females are counted
    def testNAValues(self):
        csvFile = load_data()
        testFile = open("filefile.txt", "w")

        for dic in csvFile:
            for key, values in dic.items():
                dic[key] = 'NA'

        test = sex_ratio(csvFile, testFile)
        self.assertEqual(test['"Dream"']['"Adelie"']["Male"], 0)
    
    def testDifferentNAValues(self):
        csvFile2 = load_data()
        testFile2 = open("same.txt", "w")
        

        for dic2 in csvFile2:
            for key, values in dic2.items():
                dic2[key] = 'NA'
        allMaleValues = sex_ratio(csvFile2, testFile2)
        self.assertEqual(allMaleValues['"Torgersen"']['"Adelie"']["Male"], allMaleValues['"Dream"']['"Adelie"']["Female"])


#This next function calculates averages for body mass, bill length, and flipper length of penguins by year
def average_by_year(fdata, newfile):
    year = {
        2007: {'"body_mass_g"': 0, '"bill_length_mm"': 0, '"flipper_length_mm"': 0, "count": 0},
        2008: {'"body_mass_g"': 0, '"bill_length_mm"': 0, '"flipper_length_mm"': 0, "count": 0},
        2009: {'"body_mass_g"': 0, '"bill_length_mm"': 0, '"flipper_length_mm"': 0, "count": 0},

    }
    for line in fdata:
        year[int(line["year"])]["count"] += 1

        if line["body_mass_g"] != 'NA':
            year[int(line["year"])]['"body_mass_g"'] += float(line["body_mass_g"])

        if line["bill_length_mm"] != 'NA':
            year[int(line["year"])]['"bill_length_mm"'] += float(line["bill_length_mm"])
        
        if line["flipper_length_mm"] != 'NA':
            year[int(line["year"])]['"flipper_length_mm"'] += float(line["flipper_length_mm"])

    for key, items in year.items():
        items['"body_mass_g"'] = items['"body_mass_g"'] / items["count"]
        items['"bill_length_mm"'] = items['"bill_length_mm"'] / items["count"]
        items['"flipper_length_mm"'] = items['"flipper_length_mm"'] / items["count"]
    

    newfile.write("Average Body Mass (g), Bill Length (mm), and Flipper Length (mm) by Year: \n")
    newfile.write("Year 2007 \n")
    newfile.write(f"    Avg. Body Mass (g), {year[2007]['"body_mass_g"']}\n")
    newfile.write(f"    Avg. Bill Length (mm), {year[2007]['"bill_length_mm"']}\n")
    newfile.write(f"    Avg. Flipper Length (mm), {year[2007]['"flipper_length_mm"']}\n")
    newfile.write("Year 2008 \n")
    newfile.write(f"    Avg. Body Mass (g), {year[2008]['"body_mass_g"']}\n")
    newfile.write(f"    Avg. Bill Length (mm), {year[2008]['"bill_length_mm"']}\n")
    newfile.write(f"    Avg. Flipper Length (mm), {year[2008]['"flipper_length_mm"']}\n")
    newfile.write("Year 2009 \n")
    newfile.write(f"    Avg. Body Mass (g), {year[2009]['"body_mass_g"']}\n")
    newfile.write(f"    Avg. Bill Length (mm), {year[2009]['"bill_length_mm"']}\n")
    newfile.write(f"    Avg. Flipper Length (mm), {year[2009]['"flipper_length_mm"']}\n")

    return year

class testAverageByYear(unittest.TestCase):
    #Two general cases

    #Testing to make sure two year's worth of penguin counts are not equal
    def testOne(self):
        csvFile = load_data()
        file = open("testfile5.txt", "w")

        d = average_by_year(csvFile, file)


        self.assertNotEqual(d[2007]["count"], d[2008]["count"])

    #testing to see that all the penguins are counted for, the total being 344 penguins
    def testTwo(self):
        csvFile2 = load_data()
        file4 = open("known.txt", "w")

        d = average_by_year(csvFile2, file4)

        self.assertEqual((d[2009]["count"] + d[2008]["count"] + d[2007]["count"]), 344)

    #Edge cases:
    #Setting all values to a string, "NA", excluding year, expecting zeroes, 
    def testThree(self):
        csvFile3 = load_data()
        file5 = open("filefile.txt", "w")
        for item in csvFile3:
            for key, values in item.items():
                if key != "year":
                    item[key] = "NA"
        test = average_by_year(csvFile3, file5)
        self.assertEqual(test[2009]['"body_mass_g"'], 0)
    
    #testing to see what will happen if all values are set to zero except for the penguin's year    
    def testFour(self):
        csvFile4 = load_data()
        file6 = open("camel.txt", "w")
        for lst in csvFile4:
            for key, values in lst.items():
                if key != "year":
                    lst[key] = "0"
        f = average_by_year(csvFile4, file6)
        self.assertEqual(f[2008]['"body_mass_g"'], 0)





if __name__ == "__main__":
    unittest.main()

def main():
    fdata = load_data()
    f = open("newfile.txt", "w")
    sex_ratio(fdata, f)
    average_by_year(fdata, f)
    for line in f:
        print(line)
    f.close()
    


main()