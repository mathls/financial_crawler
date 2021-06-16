"""
과제2

"""

import pywinmacro as pw
import time

location1 = (158, 65)  # 주소창
location2 = (217, 122) # 검색창
location3 = (324, 526) # history data
location4 = (631, 698) # 다운로드

# 조회 대상 종목의 티커 코드를 기록한 리스트

stocks = ["FB", "MSFT", "RIOT"]


# 역대 주가 정보를 다운반든 함수

def price(ticker):
    #검색창 클릭
    pw.click(location2)
    time.sleep(3)
    # 티커코드 입력
    pw.type_in(ticker)
    time.sleep(3)
    #엔터
    pw.key_press_once("enter")
    time.sleep(3)
    # history data
    pw.click(location3)
    time.sleep(5)
    # download 클릭
    pw.click(location4)
    time.sleep(5)


# stocks 리스트에 저장된 종목들의 주가 조회
def get_price_data(stocks):
    # 반복문
    for stock in stocks:
        #개별 종목 주가 조회
        price(stock)
        time.sleep(3)


# 야후 파이낸스에 접속하는 함수
def go_to_yfinance():
    # 주소창 클릭
    pw.click(location1)
    time.sleep(1)
    # 야후 파이낸스 주소입력
    pw.type_in("https://finance.yahoo.com")
    time.sleep(1)
    # 엔터키 입력
    pw.key_press_once("enter")


# 야휴파이낸스 접속
go_to_yfinance()

# 주가들을 검색하는 작업

get_price_data(stocks)

