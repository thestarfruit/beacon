CSV格式的HTML展示
seg1 = '''
<!DOCTYPE HTML>\n<html>\n<body>\n<meta charset=gb2312>
<h2 align=center>二维表格样式数据</h2>
<table border='1' align="center" width=70%>
<tr bgcolor='orange'>\n'''
seg2 = "</tr>\n"
seg3 = "</table>\n</body>\n</html>"
def fill_data(locls):
    seg = '<tr><td align="center">{}</td><td align="center">{}</td><td align="center">{}</td><td align="center">{}</td></tr>\n'.format(*locls)
    return seg
fr = open("price2016.csv", "r")
ls = []
for line in fr:
    line = line.replace("\n","")
    ls.append(line.split(","))
fr.close()
fw = open("price2016.html", "w")
fw.write(seg1)
fw.write('<th width="25%">{}</th>\n<th width="25%">{}</th>\n<th width="25%">{}</th>\n<th width="25%">{}</th>\n'.format(*ls[0]))
fw.write(seg2)
for i in range(len(ls)-1):
    fw.write(fill_data(ls[i+1]))
fw.write(seg3)
fw.close()

CSV格式向JSON格式的转换
import json
fr = open("price2016.csv", "r")
ls = []
for line in fr:
    line = line.replace("\n","")
    ls.append(line.split(','))
fr.close()
fw = open("price2016.json", "w")
for i in range(1,len(ls)):
    ls[i] = dict(zip(ls[0], ls[i]))
json.dump(ls[1:],fw, sort_keys=True, indent=4, ensure_ascii=False)
fw.close()

JSON格式向CSV格式的转换
import json
fr = open("price2016.json", "r")
ls = json.load(fr)
data = [ list(ls[0].keys()) ]
for item in ls:
    data.append(list(item.values()))
fr.close()
fw = open("price2016_from_json.csv", "w")
for item in data:
    fw.write(",".join(item) + "\n")
fw.close()
