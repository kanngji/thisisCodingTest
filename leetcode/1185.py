import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date = datetime.date(year,month,day)

        # 요일 계산
        day_index = date.weekday()

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        return days[(day_index)%7]