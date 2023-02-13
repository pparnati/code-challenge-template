import os
import pyodbc


conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=localhost;'
    'Database=ESISDB;'
    'Trusted_connection=yes;'
    'Username=BigFish;'
    'Password=jkat7luxP;'
)

print("the files in the wx_data directory are ")
dir_list = os.listdir("../wx_data")
for wxFile in dir_list:
    print(wxFile)
    os.chdir("../wx_data")
    if os.path.isfile(os.path.join("../wx_data", wxFile)):
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
                ss= "insert into [dbo].[wx_data] values (" + \
                row[0] + ",'" + wxFile[0:11] + "'," + row[1] + "," + row[2] + "," + row[3] + ")"
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
