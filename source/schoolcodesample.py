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
'''
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
'''
#2018.03.27

import requests, re
from bs4 import BeautifulSoup

'''
mealcode={1:조식,2:중식,3:석식}
referenced from M4ndU 's code https://github.com/M4ndU/school_meal_parser_python
modified by P4B on 2018-03-28
'''
def parseCafeteria(classcode,sccode,areacode,destday=datetime.today(),mealcode=2):#(code, sccode, areacode, ymd,weekday):
    schMmealScCode = mealcode
    schYmd = destday.strftime("%Y.%m.%d") #str 요청할 날짜 yyyy.mm.dd
    weekday = destday.weekday()
    if weekday == 5 or weekday == 6: #토요일,일요일 버림
        element = " " #공백 반환
    else:
        num = weekday + 1 #int 요청할 날짜의 요일 0월1화2수3목4금5토6일 파싱한 데이터의 배열이 일요일부터 시작되므로 1을 더해줍니다.
        URL = (
                "http://"+
                region[areacode]+
                "/sts_sci_md01_001.do?"+
                "schulCode="+sccode+
                "&schulCrseScCode=%d"%classcode+
                "&schulKndScCode=%02d"%classcode+
                "&schMmealScCode=%d&schYmd=%s" % (schMmealScCode, schYmd)
            )
        #http://stu.AAA.go.kr/ 관할 교육청 주소 확인해주세요.
        #schulCode= 학교고유코드
        #schulCrseScCode= 1유치원2초등학교3중학교4고등학교
        #schulKndScCode= 01유치원02초등학교03중학교04고등학교

        #기존 get_html 함수부분을 옮겨왔습니다.
        html = ""
        resp = requests.get(URL)
        if resp.status_code == 200 : #사이트가 정상적으로 응답할 경우
            html = resp.text
        soup = BeautifulSoup(html, 'html.parser')
        element_data = soup.find_all("tr")
        element_data = element_data[2].find_all('td')
        element = "나이스 홈페이지에 문제가 있습니다. 나중에 다시 시도해주세요." #사이트에 문제가 있을 경우 출력
        try:
            element = str(element_data[num])

            #filter
            element_filter = ['[', ']', '<td class="textC last">', '<td class="textC">', '</td>', '&amp;', '(h)', '.']
            for element_string in element_filter :
                element = element.replace(element_string, '')
            #줄 바꿈 처리
            element = element.replace('<br/>', '\n')
            #모든 공백 삭제
            element = re.sub(r"\d", "", element)

        #급식이 없을 경우
        except:
            element = " " # 공백 반환
    return element

if __name__ == '__main__':
    c=SchoolInfoBringer()
    c.getSchoolInfo(input("학교이름을 주세요\n"))
    print(c.result[0])
    destschool=c.result[0]
    destday=datetime.today()
    destday=destday.replace(day=int(input("dd 형식으로 날짜를 주세요\n")))
    print("이번달 "+str(destday.day)+"일의 급식정보입니다")
    print(parseCafeteria(destschool.schooltype,destschool.schoolcode,destschool.schoolarea,destday=destday))