#pyWorkingDays

Python module for dealing with bussiness days

##Description

This module implements the BusinessCalendar class, witch implements methods for dealing with business days

##Methods implemented

###BusinessCalendar.isBusinessDay(day)

###BusinessCalendar.isWeekendDay(day)

###BusinessCalendar.setWeekend(weekend_type)

###BusinessCalendar.setCalendar(days)

###BusinessCalendar.diff_days(start, end)

###BusinessCalendar.add_days(start, days)

##Examples
###Finding the numbre of business days between two dates

<pre><code>>>>from pyWorkingDays import BusinessCalendar
>>>from datetime import date
>>>
>>>cal = BusinessCalendar()
>>>start = date(2012,10,1)
>>>end = date(2012,10,8) 
>>>cal.diff_days(start, end) 
5
</code></pre>

###Adding N business days to a date

<pre><code>>>>from pyWorkingDays import BusinessCalendar
>>>from datetime import date
>>>
>>>start = BusinessDay()
>>>cal.add_days(start,5)
datetime.date(2012,10,8)
</code></pre>

##TODOs
* Dealing with business hours