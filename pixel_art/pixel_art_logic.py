import sys
from datetime import datetime

class CommitList():
   def __init__(self, c_list):
        self.c_list = []
   def add_to_list(self, num):
        self.c_list.append(num)

class CommitSolver():
    def solve_datetime(self, num):
        num.rjust(3 + len(num), '0')
        curr_year = "2023"
        res = datetime.strptime(curr_year + "-" + num, "%Y-%j").strftime("%Y-%m-%d")
        str_res = str(res) + " 20:00"
        return str_res

    #def make_commit(self):