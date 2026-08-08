class Solution(object):
    def haveConflict(self, event1, event2):
        start1= self.conversion(event1[0])
        end1 = self.conversion(event1[1])
        start2 = self.conversion(event2[0])
        end2 = self.conversion(event2[1])

        return (start1 <= start2 <= end1) or (start2 <= start1 <= end2) 

    def conversion(self, time_str):
        hours, minutes = time_str.split(":")
        h = int(hours)
        m = int(minutes)
        return h*60 + m

sol = Solution()
print(sol.haveConflict(["01:15","02:00"], ["02:00","03:00"]))
print(sol.haveConflict(["01:00","02:00"], ["01:20","03:00"]))
print(sol.haveConflict(["10:00","11:00"], ["14:00","15:00"]))