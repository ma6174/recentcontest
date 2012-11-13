#!/usr/bin/env python
#coding=utf-8
import json
import urllib
import datetime
txt = urllib.urlopen("http://contests.acmicpc.info/contests.json").read()
#txt=open("contests.json").read()
out = json.loads(txt)
tr_odd = '<tr class="odd"><td>%s</td><td><a href="%s" target="_blank" >%s</a></td><td>%s</td><td>%s</td><td>%s</td><td>%sdays</td></tr>'
tr = '<tr><td>%s</td><td><a href="%s" target="_blank" >%s</a></td><td>%s</td><td>%s</td><td>%s</td><td>%sdays</td></tr>'
tr_odd_1 = '<tr class="odd"><td>%s</td><td><a href="%s" target="_blank" >%s</a></td><td>%s</td><td>%s</td><td>%s</td><td>%sday</td></tr>'
tr_1 = '<tr><td>%s</td><td><a href="%s" target="_blank" >%s</a></td><td>%s</td><td>%s</td><td>%s</td><td>%sday</td></tr>'
tab=""
for i in range(len(out)-1):
	da= out[i]["start_time"].split()[0].split("-")
	dd=datetime.date(int(da[0]),int(da[1]),int(da[2]))
	db= datetime.date.today()
	cast=(dd-db).days
	if i%2==0:
		if cast==0 or cast ==1:
			tab+=tr_1%(out[i]["oj"],out[i]["link"],out[i]["name"],out[i]["start_time"],out[i]["week"],out[i]["access"],cast)
		else:
			tab+=tr%(out[i]["oj"],out[i]["link"],out[i]["name"],out[i]["start_time"],out[i]["week"],out[i]["access"],cast)
	else:
		if cast==0 or cast ==1:
			tab+=tr_odd_1%(out[i]["oj"],out[i]["link"],out[i]["name"],out[i]["start_time"],out[i]["week"],out[i]["access"],cast)
		else:
			tab+=tr_odd%(out[i]["oj"],out[i]["link"],out[i]["name"],out[i]["start_time"],out[i]["week"],out[i]["access"],cast)

model = open("model.html").read()
#print model
#print tab.encode("utf-8")
#print "</table></body></html>"
final = "%s\n%s\n</table></body></html>"%(model,tab.encode("utf-8"))
fi = open("recentcontests.html","w")
fi.write(final)
fi.close()
