import datetime
import calendar
from canteen_modal import Canteen, Stall
class MainWindowController():

    def __init__(self):
        self.currentDatetime=self.getCurrentSystemTime()
        self.selectedDateTime=self.currentDatetime
        #self.selectedDateTime=datetime.fromtimestamp(self.currentDatetime.)
        self.canteen=Canteen.all()[0]
        self.all_stalls=[]
        self.curr_stalls=self.getStalls(self.selectedDateTime)
        print(len(self.curr_stalls))
        print(self.curr_stalls[0].name)

    def getCurrentSystemTime(self):
        return datetime.datetime.now()
    
    def getDayIdByDateTime(self,datetime):
        #monday is 0, but in database is 1 so plus 1
        return datetime.weekday()+1
    def getTimeByDateTime(self,datetime):
        return datetime.strftime('%H:%M:%S')

    def getStalls(self,datetime):
        return Stall.fetchStalls(self.getDayIdByDateTime(datetime),self.getTimeByDateTime(datetime))


    
        