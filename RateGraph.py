from pylab import *
import dateutil, pylab,random
import codecs
import csv
import time
from datetime import datetime,timedelta
import matplotlib.dates as mdate
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def draw_graph(curname, cendat, rate_list,rate_time):
    #for rec in rate_time:
    #    rec_t = time.strptime(cendat+' '+rec,'%Y-%m-%d %H:%M:%S')
        #print(datetime.datetime(*rec_t[:6]))
    rate_time_num=[date2num(datetime(*time.strptime(cendat+' '+rec,'%Y-%m-%d %H:%M:%S')[:6])) for rec in rate_time]
    #plot(rate_time_num,rate_list,)

    plot_date(rate_time_num,rate_list,linestyle='-')
    text(17, 277, u'Daily Rate')
    xtext = xlabel(u'Time (s)')
    ytext = ylabel(u'Rate')
    ttext = title(u'Daily Rate')
    grid(True)
    setp(ttext, size='large', color='r')
    #setp(text, size='medium',  weight='bold',color='b')
    setp(xtext, size='large', weight='bold', color='g')
    setp(ytext, size='large', weight='light', color='b')
    #savefig('simple_plot.png')
    #保存图片
    savefig('simple_plot')
    show()
    #fig    = plt.figure() #Figure()
    #canvas = FigureCanvas(fig)
    #ax1=fig.add_subplot(111)
    #ax1.


def main(curname, cendat, rateType):
    rate_list=[]
    rate_time=[]
    rate_time_sub =7
    for row in csvReader:
        if row[0] == curname and row[6] == cendat:
            #print(row[rate_time_sub],row[rateType])
            rate_list.append(row[rateType])
            rate_time.append(row[rate_time_sub])

    rateFile.close()
    draw_graph(curname,cendat,rate_list,rate_time)


if __name__ == '__main__':
    rateFile = codecs.open('DailyRates.csv','rb',encoding='utf-8')
    csvReader = csv.reader(rateFile,delimiter=',',dialect='excel')

main('美元','2017-02-27',2)

def test_graph():
    today = datetime.now()
    dates = [today + timedelta(days=i) for i in range(10)]
    #values = [random.randint(1, 20) for i in range(10)]
    values = [3,2,8,4,5,6,7,8,11,2]
    pylab.plot_date(pylab.date2num(dates), values, linestyle='-')
    text(17, 277, u'瞬时流量示意')
    xtext = xlabel(u'时间time (s)')
    ytext = ylabel(u'单位 (m3)')
    ttext = title(u'xx示意图')
    grid(True)
    setp(ttext, size='large', color='r')
    #setp(text, size='medium', name='courier', weight='bold',color='b')
    setp(xtext, size='medium', name='courier', weight='bold', color='g')
    setp(ytext, size='medium', name='helvetica', weight='light', color='b')
    #savefig('simple_plot.png')
    savefig('simple_plot')
    show()
