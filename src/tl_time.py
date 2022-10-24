# ===============================================
# ===============================================
# *\src\py\com_serial.py
# ===============================================
# ===============================================
#
# tool to show local time now

#import tensorflow as tf
# tensorflow is no longer used

import argparse

import time
import datetime
import sxtwl


Gan    = ["甲" , "乙" , "丙" , "丁" , "戊" , "己" , "庚" , "辛" , "壬" , "癸"]
# 天干

Zhi    = ["子" , "丑" , "寅" , "卯" , "辰" , "巳" , "午" , "未" , "申" , "酉" , "戌" , "亥"]
# 地支

ShX    = ["鼠" , "牛" , "虎" , "兔" , "龙" , "蛇" , "马" , "羊" , "猴" , "鸡" , "狗" , "猪"]
# 生肖

numCn  = ["零" , "一" , "二" , "三" , "四" , "五" , "六" , "七" , "八" , "九" , "十"]
# 中文数字

jqmc   = ["冬至" , "小寒" , "大寒" , "立春" , "雨水" , "惊蛰" , "春分" , "清明" , "谷雨" , "立夏" ,
          "小满" , "芒种" , "夏至" , "小暑" , "大暑" , "立秋" , "处暑" , "白露" , "秋分" , "寒露" ,
          "霜降" , "立冬" , "小雪" , "大雪"]
# 节气

MonCn  = ["正月" , "二月" , "三月" , "四月" , "五月" , "六月" , "七月" , "八月" , "九月" , "十月" , "十一月" , "腊月"]
# 农历月

DayCn  = ["初一" , "初二" , "初三" , "初四" , "初五" , "初六" , "初七" , "初八" , "初九" , "初十" , 
          "十一" , "十二" , "十三" , "十四" , "十五" , "十六" , "十七" , "十八" , "十九" , "二十" , 
          "廿一" , "廿二" , "廿三" , "廿四" , "廿五" , "廿六" , "廿七" , "廿八" , "廿九" , "三十" ,
          "卅一"]
# 农历日

WeekCn = ["星期日" , "星期一" , "星期二" , "星期三" , "星期四" , "星期五" , "星期六"]
# 星期

# tensorflow is no longer used to decode shell-command
#\code
#
# tf.app.flags.DEFINE_bool( 'system_time' , False , 'show system_time' )
# tf.app.flags.DEFINE_bool( 'chinese_calendar' , False , 'show chinese_calendar' )
#
# FLAGS = tf.app.flags.FLAGS
#
#\endcode

parser = argparse.ArgumentParser( description = 'manual to this script' )

parser.add_argument( '--system_time' , type = bool , default = False )
parser.add_argument( '--chinese_calendar' , type = bool , default = False )
# add args definition

args = parser.parse_args()
# save read-in args to val args

print()
# print begin NULL line

print( "> 现在时间:" , time.strftime( '%Y-%m-%d %H:%M:%S' , time.localtime() ) )
# print local time in format "Y-M-D H:M:S"

if args.chinese_calendar:
    today = datetime.datetime.today()

#   CC_today = sxtwl.fromSolar( 2020 , 6 , 20 )
    # debug line, test CC_month (测试农历闰月 2020.6.20为农历庚子年闰四月廿九)

    CC_today = sxtwl.fromSolar( today.year , today.month , today.day ) # chinese_calendar today

    CC_year = CC_today.getYearGZ( True ) # chinese_calendar year

    CC_month = "%s%s" % ( '闰' if CC_today.isLunarLeap() # 判断闰月
                                    else '' , 
                           MonCn[CC_today.getLunarMonth()-1] )
    # chinese_calendar month
    # this is a bit complex, therefore here creates direct one string

    CC_day = CC_today.getLunarDay() # chinese_calendar day

#   print( Gan[CC_year.tg] + Zhi[CC_year.dz] + "年" + CC_month + DayCn[CC_day-1] )
    # debug line

    print( "> 农历" + Gan[CC_year.tg] + Zhi[CC_year.dz] + "年" + CC_month + DayCn[CC_day-1] )

if args.system_time:
    print( "> 系统时间戳:" , time.time() )

print()
# print end NULL line