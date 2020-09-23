import sqlite3

conn = sqlite3.connect('lolcalc.db')
c = conn.cursor()

# c.execute("""CREATE TABLE stats (
# 	           champname text,
#                hp_base real,
#                hp_lvl real,
#                mp_base real,
#                mp_lvl real,
#                arm_base int,
#                arm_lvl real,
#                mr_base real,
#                mr_lvl real,
#                hp5_base real,
#                hp5_lvl real,
#                mp5_base real,
#                mp5_lvl real,
#                dam_base real,
#                dam_lvl real,
#                as_base real,
#                as_lvl real,
#                as_ratio real
# 	           )""")


conn.commit()

conn.close()