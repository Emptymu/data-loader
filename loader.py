import random
import string
import sqlite3

# Build connection with db
conn = sqlite3.connect('D:/sqlite/db/my_db')
c = conn.cursor()

# Data holder
stats = []
stats_shuffle = []

# generate data
def generator_a():
	''' GENERATE DATA '''
	stats = [(i, random.randint(1, 5000000), random.randint(1, 5000000), ''.join([random.choice(string.ascii_lowercase) for i in range(8)])) for i in range(5000000)]
	return stats

stats = generator_a()
#stats_shuffle = random.shuffle(stats)

# The Wisconsin benchmark
def generator_b():
	''' GENERATE DATA '''
	ht = [i for i in range(0, 100000)] * 10
	tt = [i for i in range(0, 10000)]  * 100
	ot = [i for i in range(0, 1000)]   * 1000

	stats = [(i + 1, ht[i], tt[i], ot[i], ''.join([random.choice(string.ascii_lowercase) for i in range(8)])) for i in range(1000000)]
	return stats

# Clear previous data; 
c.execute('DROP TABLE IF EXISTS benchmark')
c.execute('DROP TABLE IF EXISTS benchmark_rand')

# Create Tables
c.execute('''CREATE TABLE IF NOT EXISTS benchmark(
				theKey NUMBER PRIMARY KEY,
				columnA NUMBER,
				columnB NUMBER,
				filler CHAR(247)
			 )''')

c.execute('''CREATE TABLE IF NOT EXISTS benchmark_rand(
				theKey NUMBER PRIMARY KEY,
				columnA NUMBER,
				columnB NUMBER,
				filler CHAR(247)
			 )''')

# Insert stats into benchmark
c.executemany('INSERT INTO benchmark(theKey, columnA, columnB, filler) VALUES (?,?,?,?)', stats)
c.executemany('INSERT INTO benchmark_rand(theKey, columnA, columnB, filler) VALUES (?,?,?,?)', stats_shuffle)

# Save execute and close connection
conn.commit()
conn.close()





	                                                                                                                                                                                                   

