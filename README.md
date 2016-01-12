#Alfred workflows

##mt-alfred
search meituan by keyword

##IDEA-alfred
search IDEA project in User Defined Workspace and open it with IDEA

##RotateDisplay-alfred
Invoke a apple script to set the "Display" option.
I modified a nice script from
here[http://fancyham.com/tips/OS_X_toggle_display_rotation_applescript.html]
Pay attention to two things:

1. only setting the external one, I assume that the external one is the last
   screen is "screen List"
2. Button 2 or Button 1, the id may differ in different system, test the script
   and debug the button number please.
   
   
##Propbank-alfred 
Get the propbank of a verb by using this url. 
https://verbs.colorado.edu/propbank/framesets-english/ 
P.S. some verbs also have some other form, v, n, j, e.g. absent can be a j and v.

In this index.html page, the following regex pattern can extract the propbank html info. Then show them in the alfred menu. We can choose form we want and open the correct url in the new window.

```
p = re.compile(r'\<a href=\"%s-.*?\.html\"\> %s-.*?\.html\<\/a\>' % (originQuery,originQuery) ,re.S)
title_re = re.compile(r'.*?\<a href=\"(?P<html>.*?.html).*',re.S)
```

