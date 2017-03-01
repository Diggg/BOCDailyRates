from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from datetime import datetime,timedelta
import time
import codecs
import csv
from matplotlib import pyplot
from matplotlib import dates
fig    = Figure()
canvas = FigureCanvas(fig)

# first axes
#ax1    = fig.add_axes([0.1, 0.1, 0.2, 0.2])
#line,  = ax1.plot([0,1], [0,1])
#ax1.set_title("ax1")
#
## second axes
#ax2    = fig.add_axes([0.4, 0.3, 0.4, 0.5])
#sca    = ax2.scatter([1,3,5],[2,1,2])
#ax2.set_title("ax2")


def main(curname, cendat, rateType):
    rate_list=[[] for i in curname]
    rate_list_dict={i:[] for i in curname}
    print(rate_list_dict)
    rate_time=[[] for i in curname]
    rate_time_dict={i:[] for i in curname}
    #第几列货币
    rate_time_sub =7
    cendat_sub = 6
    for row in csvReader:
        if row[0] in curname and row[6] == cendat:
            #print(row[rate_time_sub],row[rateType])
            rate_list_dict[row[0]].append(row[rateType])
            rate_time_dict[row[0]].append(row[rate_time_sub])
#            if row[0] == curname[1]:
#                rate_list[1].append(row[rateType])
#                rate_time[1].append(row[rate_time_sub])
#            elif row[0] == curname[2]:
#                rate_list[2].append(row[rateType])
#                rate_time[2].append(row[rate_time_sub])

#    print(rate_list_dict)
#    print(rate_time_dict)
    rateFile.close()
    rate_time_num=[[] for i in curname]
    rate_time_num_dict={i:[dates.date2num(datetime(*time.strptime(cendat+' '+rec,'%Y-%m-%d %H:%M:%S')[:6])) for rec in rate_time_dict[i]] for i in curname}
#    print(rate_time_num_dict)
#    rate_time_num[1]=[dates.date2num(datetime(*time.strptime(cendat+' '+rec,'%Y-%m-%d %H:%M:%S')[:6])) for rec in rate_time[1]]
#    rate_time_num[2]=[dates.date2num(datetime(*time.strptime(cendat+' '+rec,'%Y-%m-%d %H:%M:%S')[:6])) for rec in rate_time[2]]


    pyplot.style.use('ggplot')
    pyplot.grid()
    #图片分辨率800*600
    fig    = pyplot.figure(figsize=(8,6))
    #canvas = FigureCanvas(fig)

    # first axe
    ax0    = fig.add_subplot(1,1,1)
    #设置标题
    #ax0.set_title(cendat+ ' '+" Rates")
    #ax0.plot_date([1],[datetime.now()],linestyle='-',color='g')
    #ax0.xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
    #在数据点旁边显示数值,如果数据点很密集的时候，会出现重叠
    #ax0.xaxis.
    ax_list={i:None for i in curname}
    for cur in curname:
        ax_list[cur] = ax0.twiny()
        ax_list[cur].plot_date(rate_time_num_dict[cur],rate_list_dict[cur],linestyle='-',color='g')
        ax_list[cur].xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))

    print(len(curname))
    for num,rate in zip(rate_time_num,rate_list):
        print(num)
        for a,b in zip(num,rate):
            pyplot.text(float(a)+0.001,float(b)+0.001,b)
    pyplot.show(fig)


if __name__ == '__main__':
    rateFile = codecs.open('DailyRates.csv','rb',encoding='utf-8')
    csvReader = csv.reader(rateFile,delimiter=',',dialect='excel')

curname=['美元','欧元']
main(curname,'2017-02-27',2)
