#-*- coding: utf-8 -*-
from bs4 import *
from urllib import parse
import json
import requests
import re
from datetime import datetime as dt
from collections import namedtuple


class SchoolInfoBringer:
    def __init__(self):
        self.si = namedtuple('SchoolInfo', ['schoolname', 'schoolcode', 'schooltype','schoolarea'])
        self.result=[]
    '''        
    def getSchoolCode(schoolname):
        if type(schoolname)!=str:
            raise TypeError("Need schoolname as string!")
    
        payload = {'criteria': "pageIndex=1&bsnmNm=%s"%parse.quote(schoolname)}
        req=requests.post("http://www.meatwatch.go.kr/biz/bm/sel/schoolListPopup.do",data=payload)
    
        soup=BeautifulSoup(req.text,'html.parser')
        keyword="사용자목록 테이블로 번호,아이디,사용자명,그룹명,기관명,사용자구분,가입일자,회원상태,인증,첨부 순으로 보여줍니다."
        table = soup.find("table", attrs={"summary": keyword})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
    
        data=[]
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        return [data[i][1:3] for i in range(len(data))]
    '''
    #사실 위쪽메서드가 아래 메서드보다 더 많은 학교코드를 검색할수있지만 아직 학교의 지역이나
    #학년 종류들이 나오지않아서 사용하지 않습니다.
    def getSchoolInfo(self,schoolname):
        try:
            payload={"SEARCH_SCHUL_NM":schoolname.encode('euc-kr'),
                     "SEARCH_GS_HANGMOK_CD":None,
                     "SEARCH_KEYWORD":schoolname.encode('euc-kr'),
                     "SEARCH_GS_HANGMOK_NM":None,
                     "SEARCH_GS_BURYU_CD":None}
            req=requests.post("http://www.schoolinfo.go.kr/ei/ss/Pneiss_f01_l0.do",data=payload)
        
            soup=BeautifulSoup(req.text,'html.parser')
            areareg = re.compile('mapD_Area _[0-9][0-9]')#지역코드 정규식
            classreg = re.compile('mapD_Class _[0-9][0-9]')#초/중/고/특수학교 정규식
            at=soup.find_all("span",{"class":areareg})
            ct=soup.find_all("span",{"class":classreg})
            rs=soup.select(".School_Name > a")
            datalist=[]
            for i in range(len(rs)):
                self.result.append(self.si._make((
                    rs[i].text,
                    re.findall("[A-Z][0-9]{9}",rs[i].attrs["onclick"])[0],
                    int(ct[i].attrs['class'][1][1:]),
                    int(at[i].attrs['class'][1][1:])
                )))
            return True
        except:
            return False
