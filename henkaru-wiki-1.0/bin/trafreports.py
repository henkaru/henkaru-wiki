#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Generates the traffic reports in wiki page format based on flow.py
"""

__author__ = "Alexey Alexashin (alexashin.a.n@yandex.ru)"
__version__ = "$Revision: 1.0 $"
__copyright__ = "Copyright (c) 2014 Alexey Alexashin"
__license__ = "Python "


import sys
from  datetime import date, timedelta

sys.path.append('/opt/flow/bin')
import flow

monthdict = flow.monthdict

def reportpage(month,year):
    '''Returns list of  month internet traffic report wiki page'''

    rep = flow.main_csv(month,year).split('\n')
    page = []
    page.append('===%s===' % rep[0])
    page.append('^%s^' % rep[1].replace(';','^'))
    for line in rep[2:-1]:
        page.append('|%s|' % line.replace(';','|'))
    page.append('||%s|' % rep[-1].replace(';','|'))
    return page

def previousmonthpage():
    '''Writes a previous month traffic statistics to wiki page file'''

    month = (date.today() - timedelta(days=(date.today().day + 1))).month
    year = date.today().year
    pagepath = '/usr/share/dokuwiki/data/pages/'
    reportpath = pagepath + 'reports/'
    reportfile = pagepath + 'reports.txt'
    filename = reportpath + 'stats_%d-%d.txt' % (month, year)

    page = reportpage(month,year)
    f = open(filename,'w')
    try:
        for line in page:
            f.write(line + '\n')
    except:
        print "Something wrong with %s" % filename
        raise
    finally:
        f.close()

    f2 = open(reportfile,'a')
    try:
        f2.write('  * [[reports/%s|%s %s]]\n' % (filename.split('/')[-1].split('.')[0],monthdict[month],year))
    except:
        print "Something wrong with %s" % reportfile
    finally:
        f2.close()


def main():
    '''Writes a current traffic statistics to wiki page file'''
    
    day = date.today().day
    month = date.today().month
    year = date.today().year

    page = reportpage(month,year)
    page.pop(0)
    page.insert(0,'===Актуальная статистика по входящему трафику. Сегодня: %d %s %d===' % (day,monthdict[month],year))
    
    f = open('/usr/share/dokuwiki/data/pages/trafnow.txt','w')
    try:
        for line in page:
            f.write(line + '\n')
    except:
        print "Something wrong with /usr/share/dokuwiki/data/pages/trafnow.txt"
        raise
    finally:
        f.close()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    elif sys.argv[1] == 'prev':
        previousmonthpage()
