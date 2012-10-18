#PyBusinessDays

Python module for dealing with bussiness days

##Description

This module implements the BusinessDay class, witch inherits from the date standard class and implements methods for dealing with business days

##Methods implemented
###BusinessDay.fromdate(date)
*Class Method*<br/>
Creates a new BusinessDay object from a [datetime.date](http://docs.python.org/library/datetime.html#date-objects) obj
###BusinessDay.isBusinessDay()
Returns *__True__* if the given date is a business day. Return *__False__* otherwise
###BusinessDay.diff(date)
Returns an integer that represents the amount of business days between _self_ and _date_

Date can be a BusinessDay object or a [datetime.date](http://docs.python.org/library/datetime.html#date-objects) object 
###BusinessDay.add(days)
Returns a [datetime.date](http://docs.python.org/library/datetime.html#date-objects) object that represents the resulting date of adding _days_ business days to _self_

##Examples
###Finding the numbre of business days between two dates

<pre><code>
>>>from pybd import BusinessDay
>>>start = BusinessDay(2012,10,1)
>>>end = BusinessDay(2012,10,8) #also works with a [datetime.date](http://docs.python.org/library/datetime.html#date-objects) object
>>>start.diff(end) #start date must be before end date, atm
5
</code></pre>

###Adding N business days to a date

<pre><code>
>>>from pybd import BusinessDay
>>>start = BusinessDay(2012,10,1)
>>>start.add(5)
datetime.date(2012,10,8)
</code></pre>

The BusinessDay.add() method returns a [datetime.date](http://docs.python.org/library/datetime.html#date-objects) object to avoid compatibility issues. If you need to use a BusinessDay object, you can use the BusinessDay.fromdate() classmethod

<pre><code>
>>>from pybd import BusinessDay
>>>start = BusinessDay(2012,10,1)
>>>BusinessDay.fromdate(start.add(5))
BusinessDay(2012,10,8)
</code></pre>

##TODOs
* Add support for negative diffs
* Custom calendars
* Dealing with business hours