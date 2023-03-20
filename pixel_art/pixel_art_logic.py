import sys
from datetime import datetime, timedelta
#need to consider threading since there might be a decent amount of loops
#can also possibly improve on how long it'd take since we can theoretically have up to 365 threads running
# don't care about the order since each day theoretically should be added

class CommitList():
   def __init__(self, c_list):
        self.c_list = []
   def add_to_list(self, num):
        self.c_list.append(num)
   def build_list(self, loop, btn):
       temp_solve = CommitSolver()
       temp_list = []
       temp_list.append(btn.toolTip())
       for i in loop:
           temp_solve.increase_time(btn.toolTip())
           
       self.c_list.append(temp_list)
   def make_commits(self):
       pass
    

class CommitSolver():
    def solve_datetime(self, num):
        num.rjust(3 + len(num), '0')
        curr_year = "2023"
        res = datetime.strptime(curr_year + "-" + num, "%Y-%j").strftime("%Y-%m-%d")
        str_res = str(res) + " 20:00"
        # print(str_res)
        return str_res
    def increase_time(self, str_num):
        add_date = datetime.strptime(str_num, "%Y-%m-%d %H:%M")
        add_date = add_date + timedelta(hours=1)
        return add_date

