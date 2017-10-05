from datetime import datetime

import requests
from bs4 import BeautifulSoup

from SchoolInfoBringer import SchoolInfoBringer
region = {
    1: 'stu.sen.go.kr',#서울
    2: 'stu.pen.go.kr',#부산
    3: 'stu.dge.go.kr',#대구
    4: 'stu.ice.go.kr',#인천
    5: 'stu.gen.go.kr',#광주
    6: 'stu.dje.go.kr',#대전
    7: 'stu.use.go.kr',#울산
    8: 'stu.sje.go.kr',#세종
    10: 'stu.goe.go.kr',#경기
    11: 'stu.kwe.go.kr',#강원
    12: 'stu.cbe.go.kr',#충북
    13: 'stu.cne.go.kr',#충남
    14: 'stu.jbe.go.kr',#전북
    15: 'stu.jne.go.kr',#전남
    16: 'stu.gbe.go.kr',#경북
    17: 'stu.gne.go.kr',#경남
    18: 'stu.jje.go.kr'#제주
}
#edited from tanbang-cafeteria https://github.com/w3bn00b/tanbang-cafeteria/
def parseCafeteria(classcode,sccode,areacode,destday=datetime.today()):
    global region
    params={"schulCrseScCode":classcode,
            "schulCode":sccode}
    r = requests.get("http://" + region[areacode] + "/sts_sci_md00_001.do",params=params)
    soup = BeautifulSoup(r.text, "html.parser")

    allofcafe = soup.find(id="contents")
    table = soup.find("table")
    tbody = table.find("tbody")
    td = tbody.find_all("td")
    div = td[destday.day-1].find_all("div")
    res = str(div[0])
    res = res.replace("<div>", "")
    res = res.replace("</div>", "")
    res = res.replace("<br/>", "\n")
    if '\n' not in res:
        res=""
    return str(res[res.find('\n')+1:])

if __name__ == '__main__':
    c=SchoolInfoBringer()
    c.getSchoolInfo(input("학교이름을 주세요\n"))
    print(c.result[0])
    destschool=c.result[0]
    destday=datetime.strptime(input("dd 형식으로 날짜를 주세요\n"), "%d")
    print("이번달 "+str(destday.day)+"일의 급식정보입니다")
    print(parseCafeteria(destschool.schooltype,destschool.schoolcode,destschool.schoolarea,destday=destday))