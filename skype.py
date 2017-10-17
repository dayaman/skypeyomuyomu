import sqlite3
import os
from operator import itemgetter

dbname = 'main.db'

conn = sqlite3.connect(dbname)
c = conn.cursor()

try:
    with open('log.txt') as fp:
        pass
except:
    with open('log.txt', 'w') as fp:
        pass
    
sql = "SELECT timestamp__ms, from_dispname, body_xml \
       FROM Messages \
       WHERE NOT body_xml LIKE '<%' \
       ORDER BY timestamp DESC \
       LIMIT 10"

query = conn.execute(sql)
timesort = sorted(query, key=itemgetter(0))
for row in timesort:
    with open('log.txt') as f:
        lines = f.readlines()
        is_read = False
        for line in lines:
            if line == str(row[0])+'\n':
                is_read = True

    if is_read == False:
        with open('log.txt', 'at') as log:
            log.write(str(row[0])+'\n')
        num_lines = sum(1 for line in open('log.txt'))
        if num_lines > 11:
            os.system('sed -i -e \'1d\' log.txt')
        os.system('say -v Kyoko "{}" さん'.format(row[1]))
        os.system('say -v Kyoko "{}"'.format(row[2]))


conn.close()
