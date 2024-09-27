class MyCalendarTwo:
    def __init__(self):
        self.single_bookings = []
        self.double_bookings = []

    def book(self, start: int, end: int) -> bool:
        for dbl_start, dbl_end in self.double_bookings:
            if max(start, dbl_start) < min(end, dbl_end):  
                return False
        for sng_start, sng_end in self.single_bookings:
            overlap_start = max(start, sng_start)
            overlap_end = min(end, sng_end)
            if overlap_start < overlap_end: 
                self.double_bookings.append((overlap_start, overlap_end))
        self.single_bookings.append((start, end))
        
        return True


