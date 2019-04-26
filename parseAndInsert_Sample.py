import json
import psycopg2

def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

def int2BoolStr (value):
    if value == 0:
        return 'False'
    else:
        return 'True'

def insert2BusinessTable():
    #reading the JSON file
    with open('./business.JSON','r') as f:    #TODO: update path for the input file
        #outfile =  open('./yelp_business.SQL', 'w')  #uncomment this line if you are writing the INSERT statements to an output file.
        line = f.readline()
        count_line = 0

        #connect to yelpdb database on postgres server using psycopg2
        #TODO: update the database name, username, and password
        try:
            conn = psycopg2.connect("dbname='yelpdb' user='postgres' host='localhost' password='0815'")
        except:
            print('Unable to connect to the database!')
            return
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            # Generate the INSERT statement for the cussent business
            # TODO: The below INSERT statement is based on a simple (and incomplete) businesstable schema. Update the statement based on your own table schema and
            # include values for all businessTable attributes
            sql_str = "INSERT INTO businessTable (business_id, name, address, city, state, zipcode, latitude, longitude, stars, reviewrating, reviewcount, numCheckins, openStatus) " + \
                      "VALUES ('" + cleanStr4SQL(data['business_id']) + "','" + cleanStr4SQL(data["name"]) + "','" + cleanStr4SQL(data["address"]) + "','" + \
                      cleanStr4SQL(data["state"]) + "','" + cleanStr4SQL(data["city"]) + "','" + cleanStr4SQL(data["postal_code"]) + "'," + str(data["latitude"]) + "," + \
                      str(data["longitude"]) + "," + str(data["stars"]) + "," + "0.0" + "," + str(data["review_count"]) + ",0 ,"  + \
                      int2BoolStr(data["is_open"]) + ");\n"
            for item in data["categories"]:
            	sql_str += "INSERT INTO category(business_id, name) VALUES ('"+cleanStr4SQL(data["business_id"]) + "','" + cleanStr4SQL(item) + "');\n"
            for day in data["hours"]:
            	sql_str += "INSERT INTO hours(business_id, day, open, close) VALUES ('"+cleanStr4SQL(data["business_id"])+"','"+day+"','"
            	temp=data["hours"][day].split("-")
            	sql_str += temp[0]+"','"+temp[1]+"');\n"
            for att in data["attributes"]:
            	sql_str += "INSERT INTO attribute(business_id, name, value) VALUES ('"+cleanStr4SQL(data["business_id"])+"','"+att+"','"+cleanStr4SQL(str(data["attributes"][att]))+"');\n"
            try:
                cur.execute(sql_str)
            except:
                print("Insert to businessTABLE failed!")
                #outfile.write(sql_str)
            conn.commit()
            # optionally you might write the INSERT statement to a file.
            line = f.readline()
            count_line +=1

        cur.close()
        conn.close()

    print(count_line)
    #outfile.close()  #uncomment this line if you are writing the INSERT statements to an output file.
    f.close()
    return

def insert2userTable():
    with open('./user.JSON','r') as f:
        line = f.readline()
        count_line = 0
        try:
            conn = psycopg2.connect("dbname='yelpdb' user='postgres' host='localhost' password='0815'")
        except:
            print('Unable to connect to the database!')
            return
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            sql_str = "INSERT INTO userTABLE(user_id, name, stars, cool, funny, useful, fans, reviewcount, since) "+\
                      "VALUES ('"+data["user_id"]+"','"+cleanStr4SQL(data["name"])+"',"+str(data["average_stars"])+","+str(data["cool"])+","+str(data["funny"])+","+\
                      str(data["useful"])+","+str(data["fans"])+","+str(data["review_count"])+",'"+str(data["yelping_since"])+"');\n"
            for friend in data["friends"]:
                sql_str+="INSERT INTO friend(user_id, friend_id) VALUES ('"+data["user_id"]+"','"+friend+"');\n"
            try:
                cur.execute(sql_str)
            except:
                print("Insert to userTABLE failed!")
            conn.commit()
            line = f.readline()
            count_line +=1

        cur.close()
        conn.close()

    print(count_line)
    f.close()
    return

def insert2reviews():
    with open('./review.JSON','r', encoding='UTF8') as f:
        line = f.readline()
        count_line = 0
        try:
            conn = psycopg2.connect("dbname='yelpdb' user='postgres' host='localhost' password='0815'")
        except:
            print('Unable to connect to the database!')
            return
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            sql_str = "INSERT INTO review(review_id, user_id, business_id, stars, date, text, useful, funny, cool) "
            sql_str+="VALUES ('"+data["review_id"]+"','"+data["user_id"]+"','"+data["business_id"]+"',"
            sql_str+=str(data["stars"])+",'"+data["date"]+"','"+cleanStr4SQL(data["text"])+"',"+str(data["useful"])+","+str(data["funny"])+","+str(data["cool"])+");\n"
            try:
                cur.execute(sql_str)
            except:
                print("Insert to userTABLE failed!")
            conn.commit()
            line = f.readline()
            count_line +=1

        cur.close()
        conn.close()

    print(count_line)
    f.close()
    return

def insert2checkin():
    with open('./checkin.JSON','r') as f:
        line = f.readline()
        count_line = 0
        try:
            conn = psycopg2.connect("dbname='yelpdb' user='postgres' host='localhost' password='0815'")
        except:
            print('Unable to connect to the database!')
            return
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            sql_str=""
            for day in data["time"]:
                for time in data["time"][day]:
                    sql_str+="INSERT INTO checkins(business_id, day, count, time) "
                    sql_str+="VALUES ('"+data["business_id"]+"','"+day+"',"+data["time"][day][time]+",'"+time+"');\n"
            try:
                cur.execute(sql_str)
            except:
                print("Insert to userTABLE failed!")
            conn.commit()
            line = f.readline()
            count_line +=1

        cur.close()
        conn.close()

    print(count_line)
    f.close()
    return

#insert2BusinessTable()
#insert2userTable()
insert2reviews()
insert2checkin()