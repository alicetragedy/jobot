import csv
with open('data.csv', 'rb') as csvfile:
  jobreader = csv.reader(csvfile, delimiter=',', quotechar= '|')
  all_jobs = []
  single_job = []
  userlocation = "Wien"
  useredu = "Uni"
  userfield = "Marketing"
  for row in jobreader:
    for column in row:
      single_job.append(column)
    all_jobs.append(row)
  # example: print first item (job title) for second row (first job)
  #print(all_jobs[1][0])
  
  saved_jobs = []
  saved_job = []

  for each_item in all_jobs:
    if str(userlocation) in each_item[1]:
      if str(useredu) in each_item[3]:
        if str(userfield) in each_item[2]:
          print(each_item[0] + "\n" + each_item[-1])
        else:
          continue
    else:
      continue


    #print '\n'.join(row)



#if str(row[2]) == str(text)