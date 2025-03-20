import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Yash1012108@",
    database="train"
)

mycursor = mydb.cursor()

# Create table if it doesn't exist
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS trains (
        train_no VARCHAR(10) PRIMARY KEY, 
        train_name VARCHAR(100),
        source VARCHAR(50), 
        destination VARCHAR(50), 
        seat_2s VARCHAR(10), 
        seat_sl VARCHAR(10), 
        seat_ac VARCHAR(10), 
        departure_time VARCHAR(20), 
        arrival_time VARCHAR(20)
    )
""")

# List of train records to insert
train_data = [
    ('12019', 'Shatabdi Express', 'Howrah', 'Ranchi', '1170', '1780', '2000', '06:05 AM', '01:15 PM'),
    ('12130', 'Azad Hind Express', 'Howrah', 'Pune', '1120', '1865', '2690', '07:20 AM', '10:10 PM'),
    ('12277', 'Shatabdi Express', 'Howrah', 'Puri', '1070', '1120', '1860', '02:15 PM', '09:50 PM'),
    ('12860', 'Gitanjali Express', 'Howrah', 'Mumbai', '1740', '1840', '2655', '02:05 PM', '09:20 PM'),
    ('12839', 'Chennai Mail Express', 'Howrah', 'Chennai', '1630', '2520', '4185', '03:15 AM', '11:55 PM'),
    ('20822', 'Pune Humsafar Express', 'Howrah', 'Pune', '400', '750', '2000', '02:45 AM', '07:25 PM'),
    ('12129', 'Azad Hind Express', 'Pune', 'Howrah', '1120', '1865', '2690', '01:45 AM', '06:35 PM'),
    ('20821', 'Pune Humsa far Express', 'Pune', 'Howrah', '400', '750', '2000', '10:40 AM', '11:25 PM'),
    ('22201', 'Duronto Express', 'Kharagpur', 'Puri', '240', '400', '1085', '03:55 AM', '10:15 PM'),
    ('22202', 'Duronto Express', 'Puri', 'Howrah', '330', '630', '1585', '03:55 AM', '12:15 PM'),
    ('12837', 'HWH PURI SF Express', 'Howrah', 'Puri', '145', '645', '960', '12:18 AM', '08:15 AM'),
    ('18409', 'Jagannath Express', 'Howrah', 'Puri', '165', '295', '980', '04:30 AM', '08:55 PM'),
    ('12887', 'SHM Puri SF Express', 'Kharagpur', 'Puri', '145', '275', '705', '05:10 AM', '10:30 PM'),
    ('12821', 'Dhahuli Express', 'Kharagpur', 'Puri', '145', '210', '375', '10:55 AM', '06:00 PM'),
    ('12278', 'Shatabdi Express', 'Puri', 'Kharagpur', '465', '935', '1450', '05:45 AM', '11:37 AM'),
    ('12838', 'PURI HWH SF Express', 'Puri', 'Howrah', '145', '645', '960', '02:15 AM', '08:15 PM'),
    ('15643', 'PURI KYQ Express', 'Kharagpur', 'Puri', '150', '245', '660', '04:30 AM', '11:10 AM'),
    ('12882', 'Garib Rath Express', 'Puri', 'Howrah', '200', '350', '600', '06:10 AM', '01:50 PM'),
    ('18410', 'Jagannath Express', 'Puri', 'Howrah', '165', '295', '980', '08:10 AM', '05:20 PM'),
    ('12665', 'HWH Cape SF Express', 'Howrah', 'Chennai', '635', '1665', '2390', '04:15 PM', '09:38 PM'),
    ('12663', 'HWH TPJ SUF Express', 'Howrah', 'Chennai', '700', '1840', '2580', '05:40 PM', '09:38 PM'),
    ('12840', 'MAS HWH Mail Express', 'Chennai', 'Howrah', '635', '1665', '2390', '04:15 PM', '09:38 PM'),
    ('12842', 'Coromandal Express', 'Chennai', 'Howrah', '323', '635', '1650', '06:15 AM', '07:10 PM'),
    ('12664', 'TPJ HWH EXP', 'Chennai', 'Howrah', '700', '1840', '2580', '06:10 PM', '11:55 PM'),
    ('12301', 'Rajdhani Express', 'Howrah', 'New Delhi', '2770', '3775', '4710', '10:50 AM', '09:50 PM'),
    ('12303', 'Poorva Express', 'Howrah', 'New Delhi', '405', '600', '1570', '08:50 AM', '07:50 PM'),
    ('12302', 'Rajdhani Express', 'New Delhi', 'Howrah', '2770', '3775', '4710', '04:50 PM', '09:55 AM'),
    ('12304', 'Poorva Express', 'New Delhi', 'Howrah', '405', '600', '1570', '03:50 PM', '06:50 AM'),
    ('12280', 'HWH Duronto Express', 'New Delhi', 'Howrah', '2000', '3000', '4800', '12:00 PM', '06:00 AM'),
    ('22807', 'Santragachi Chennai SF', 'Santragachi', 'Chennai', '450', '890', '2000', '12:10 PM', '04:55 AM'),
    ('12622', 'Tamil Nadu Express', 'New Delhi', 'Chennai', '550', '1200', '2300', '10:30 PM', '06:00 AM'),
    ('12615', 'Grand Trunk Express', 'New Delhi', 'Chennai', '450', '1100', '2100', '06:30 PM', '03:30 AM')
]

# Insert multiple records at once using executemany
sql = """
    INSERT INTO trains (train_no, train_name, source, destination, seat_2s, seat_sl, seat_ac, departure_time, arrival_time) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
mycursor.executemany(sql, train_data)

# Commit the transaction
mydb.commit()

print("Data inserted successfully.")

# Close the database connection
mycursor.close()
mydb.close()
