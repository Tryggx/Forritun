def get_data(file_name):
    try:
        file_object = open(file_name, 'r')
        return file_object
    except:
        print("Filename {} not found!".format(file_name))

def get_data_list(file_object):
    data_list=[]
    for line_str in file_object:
        data_list.append(line_str.strip().split(','))
    data_list.pop(0)
    return data_list

def get_monthly_averages(data_list):
    datelist=[data_list[0][0][0:7]]
    avglist=[]
    bottomsum = 0
    topsum = 0
    prev=data_list[0][0][5:7]
    for i in data_list:
        dummy=i[0][5:7]

        if not dummy==prev:
            avglist.append(topsum / bottomsum)
            datelist.append(i[0][0:7])
            bottomsum = 0
            topsum = 0

        topsum += (float(i[6])*float(i[5]))
        bottomsum += float(i[6])

        prev=dummy
    avglist.append(topsum / bottomsum)
    return avglist,datelist

def printfunc(avglist,datelist):
    for i in range(len(avglist)):
        print('{:<7}{:>10.2f}'.format(datelist[i],avglist[i]))
    return

def highest(data_list):
    high= data_list[0]
    for i in data_list:
        if float(i[5]) >= float(high[5]):
            high=i
    return high



file_name=input("Enter filename: ")
file_object = (get_data(file_name))
if not file_object == None:
    data_list=(get_data_list(file_object))
    avglist,datelist=(get_monthly_averages(data_list))
    print('Month       Price')
    printfunc(avglist,datelist)
    high=highest(data_list)
    print("Highest price {:.2f} on day {}".format(float(high[5]),high[0]))