class Solution:
    def reformatDate(self, date: str) -> str:
        year = date.split()[-1]
        day = ''.join([d for d in date.split()[0] if d in '0123456789'])
        months_calendar = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        return f"{year}-{months_calendar.index(date.split()[1]) + 1:02}-{int(day):02}"
