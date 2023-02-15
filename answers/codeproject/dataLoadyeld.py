import os
import sqlite3


conn = sqlite3.connect("db.sqlite3")

print("the files in the wx_data directory are ")
dir_list = os.listdir("../yld_data")
for wxFile in dir_list:
    print(wxFile)
    os.chdir("../yld_data")
    if os.path.isfile(os.path.join("../yld_data", wxFile)):
        file = open(wxFile, mode='r', encoding='utf-8-sig')
        lines = file.readlines()
        file.close()

        for line in lines:
            line = line.split("\t")
            row = []
            for i in range(0, len(line), 1):
                s = line[i].strip()
                row.append(s)
            print(row)
            try:
                coxn = conn.cursor()
                year=row[0]
                ss= "insert into codeapp_yielddata(theyear,yieldoftheyear) values (" + \
               year + "," + row[1] + ")"
                print("Passed "+ss)
                coxn.execute(ss)
                print("Passed 3")
                #for i in coxn:
                #    print(i)


            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)
conn.commit()
conn.close()