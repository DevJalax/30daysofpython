import sqlite3
import json
conn = sqlite3.connect('test.db')
c = conn.cursor();
c.execute("CREATE TABLE DT(id varchar(9),data json)")
c.execute("insert into DT values(?,?)",(1,json.dumps({"Name":"john","doe":20})),(2,json.dumps(["Amala","Dany"])),(3,json.dumps(("Carolina","Matt"))),(4,json.dumps("Elena")),(5,json.dumps(80)),(6,json.dumps(25.1)),(7,json.dumps(True)),(8,json.dumps(False)),(9,json.dumps(None)))
c.execute("SELECT * FROM DT")
rows = c.fetchall()
for row in rows:
    print(row)
