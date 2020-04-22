import csv

with open('name.csv','r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)           # SKIP the firtst line which is header
    for line in csv_reader:
        #print(line)
        #print(line[1:3])
        pass

print('### CSV writer' )
with open('name.csv','r') as r:
    csv_reader = csv.reader(r)
    
    with open('name_copy.csv','w',newline='') as w:
        csv_writer = csv.writer(w,delimiter='\t')
        
        for line in csv_reader:
            print(line)
            csv_writer.writerow(line)

print('### READ <tab> delimiter file')
with open('name_copy.csv','r') as r:
    csv_reader = csv.reader(r,delimiter='\t')
    for line in csv_reader:
        print(line)

print('### USE DICTIONARY READER')
with open('name_copy.csv','r') as r:
    csv_reader = csv.DictReader(r,delimiter='\t')
    for line in csv_reader:
        print(line['last_name'])



