import csv
userlocation = "Wien"
useredu = "Uni"
userfield = "IT"


#jobs = find_jobs(userfield, useredu, userfield)

def find_jobs(userlocation, useredu, userfield):
  with open('data.csv', 'rb') as csvfile:
    jobreader = csv.reader(csvfile, delimiter=',', quotechar= '"')

    jobs = []
    for row in jobreader:
      if str(row[1]).lower() == userlocation.lower():
        if str(row[3]).lower() == str(useredu).lower():
          if str(row[2]).lower() == str(userfield).lower():
            jobs.append(row[0] + " " +row[-1])
    return len(jobs)     
    #return jobs.length

    #return jobs
    #print '\n'.join(row)

length = find_jobs(userlocation, useredu, userfield)
print length
#if str(row[2]) == str(text)