pub fn is_leap_year(year: u64) -> bool {
    match year {
        year if (year % 400 == 0) => return true,
        year if (year % 100 == 0) => return false,
        year if (year % 4 == 0) => return true,
        _year => return false
        
    }
}
