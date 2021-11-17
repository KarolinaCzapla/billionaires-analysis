import psycopg2
import matplotlib.pyplot as plt
from billionairesPackage.billionaires import *

con = psycopg2.connect(
    host='localhost',
    database='billionaires_db',
    user='karolina',
    password='123456',
    port=5432
)

cur = con.cursor()
cur.execute('select * from people')
rows = cur.fetchall()
cur.close()
con.close()


class person:
    def __init__(self, user_name, user_surname, net_worth, country, source, age, industry):
        self.user_name = user_name
        self.user_surname = user_surname
        self.net_worth = net_worth
        self.country = country
        self.source = source
        self.age = age
        self.industry = industry


data_person = []
for r in rows:
    data_person.append(person(r[1], r[2], r[3], r[4], r[5], r[6], r[7]))
    # print(f'{r[0]},{r[1]}')

surname = surname(data_person[:10])
worth = worth(data_person[:10])
plt.figure(figsize=(12, 5))
plt.bar(surname, worth)
plt.xlabel("Billionaire")
plt.ylabel("Networth")
plt.title("The top 10 billionaires according to their Net Worth", fontsize=20)
# plt.savefig('top_ten.png')
plt.show()


tech_name = technology(data_person).keys()
number = technology(data_person).values()
custom_colors = ["skyblue", "yellowgreen", 'tomato', "blue", "red"]
plt.figure(figsize=(12, 5))
plt.pie(number, labels=tech_name, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Top 5 Industries with Most Number of Billionaires", fontsize=20)
plt.savefig('top_five_industries.png')
plt.show()


country_name = country(data_person).keys()
number = country(data_person).values()
custom_colors = ["skyblue", "yellowgreen", 'tomato', "blue", "red"]
plt.figure(figsize=(12, 5))
plt.pie(number, labels=country_name, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Top 5 Countries with Most Number of Billionaires", fontsize=20)
plt.savefig('top_five_countries.png')
plt.show()

