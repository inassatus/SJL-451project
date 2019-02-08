import json
import types

def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

def attributes(s):
	attr = ""
	for k in s:
		if type(s[k]) is dict:
			attr += (attributes(s[k]))
		else:
			attr += str((k,s[k]))
	attr.replace("'", "")
	return attr
	
def hours(s):
	hrs = ""
	for k in s:
		hrs += str((k,s[k]))
	return hrs.replace("-", ",")

def time(s):
	tm = ""
	for k in s:
		tm += k + ":"
		for v in s[k]:
			tm += str((v,s[k][v])) + ","
		tm += "\t"
	return tm.replace("'","").replace(", ","-")

def parseBusinessData():
    #read the JSON file
    with open('.\yelp_business.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('business.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write(cleanStr4SQL(data['business_id'])+'\t') #business id
            outfile.write(cleanStr4SQL(data['name'])+'\t') #name
            outfile.write(cleanStr4SQL(data['address'])+'\t') #full_address
            outfile.write(cleanStr4SQL(data['state'])+'\t') #state
            outfile.write(cleanStr4SQL(data['city'])+'\t') #city
            outfile.write(cleanStr4SQL(data['postal_code']) + '\t')  #zipcode
            outfile.write(str(data['latitude'])+'\t') #latitude
            outfile.write(str(data['longitude'])+'\t') #longitude
            outfile.write(str(data['stars'])+'\t') #stars
            outfile.write(str(data['review_count'])+'\t') #reviewcount
            outfile.write(str(data['is_open'])+'\t') #openstatus
            outfile.write(str([item for item in  data['categories']])+'\t') #category list
            outfile.write('['+attributes(data['attributes'])+']\t') #attributes
            outfile.write('['+hours(data['hours'])+']\t') #hours
            outfile.write('\n')

            line = f.readline()
            count_line +=1
    print(count_line)
    outfile.close()
    f.close()

def parseUserData():
    #read the JSON file
	#all except compliment and elite
    with open('.\yelp_user.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('user.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write(str(data['average_stars'])+'\t') #average stars
            outfile.write(str(data['cool'])+'\t') #cool
            outfile.write(str(data['fans'])+'\t') #fans
            outfile.write(str([item for item in data['friends']])+'\t') #friends
            outfile.write(str(data['funny'])+'\t') #funny
            outfile.write(cleanStr4SQL(data['name']) + '\t')  #name
            outfile.write(str(data['review_count'])+'\t') #review count
            outfile.write(str(data['useful'])+'\t') #useful
            outfile.write(cleanStr4SQL(data['user_id'])+'\t') #user id
            outfile.write(cleanStr4SQL(data['yelping_since'])+'\t') #yelping since
            outfile.write('\n')

            line = f.readline()
            count_line +=1
    print(count_line)
    outfile.close()
    f.close()

def parseCheckinData():
    #read the JSON file
	#all keys
    with open('.\yelp_checkin.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('checkin.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write(time(data['time'])+'\t') #time
            outfile.write(cleanStr4SQL(data['business_id'])+'\t') #business id
            outfile.write('\n')

            line = f.readline()
            count_line +=1
    print(count_line)
    outfile.close()
    f.close()


def parseReviewData():
    #read the JSON file
	#all keys
    with open('.\yelp_review.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('review.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write(cleanStr4SQL(data['review_id'])+'\t') #review id
            outfile.write(cleanStr4SQL(data['user_id'])+'\t') #user id
            outfile.write(cleanStr4SQL(data['business_id'])+'\t') #business id
            outfile.write(str(data['stars'])+'\t') #stars
            outfile.write(cleanStr4SQL(data['date'])+'\t') #date
            outfile.write(cleanStr4SQL(data['text']) + '\t') #text
            outfile.write(str(data['useful'])+'\t') #useful
            outfile.write(str(data['funny'])+'\t') #funny
            outfile.write(str(data['cool'])+'\t') #cool
            outfile.write('\n')

            line = f.readline()
            count_line +=1
    print(count_line)
    outfile.close()
    f.close()

parseBusinessData()
parseUserData()
parseCheckinData()
parseReviewData()
