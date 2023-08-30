'''
Problem:
You are given a string 'STR' representing JSON object.
Return an array of strings denoting JSON objects with proper indentation.
Rules For Proper Indentation:
1. Every inner brace should increase one indentation to the following lines.
2. Every close brace should decrease one indentation to the same line and the following lines.
3. Every, will mean a separate line.
4. The indents can be increased with an additional 4 spaces or '\t'.
'''
from os import *
from sys import *
from collections import *
from math import *
'''
    Time Complexity: O(N ^ 2)
    Space Complexity: O(N ^ 2)

    Where 'N' is the length of the string.
'''
def prettyJSON(str):
    # A pointer to the last row.
    r = 0
    result = []
    result.append("")
    brace = 1
    i = 0

    while i < len(str):
        # Space just ignore.
        if str[i] == " ":
            i += 1
            continue
        elif str[i] == "{" or str[i] == "[":
            # If first brace is found.
            if brace == 1 and r == 0:
                result[r] += str[i]
            else:
                # Make a new line and add adequate spaces and increment braces.
                r = r + 1
                result.append('\t' * brace + str[i])
                brace = brace + 1
            r = r + 1
            result.append('\t' * brace)
            i += 1
        elif str[i] == "}" or str[i] == "]":
            # Make a new line and decrement braces.
            if brace > 1:
                r = r + 1
                result.append('\t' * (brace - 1))
                result[r] += str[i]
                brace = brace - 1
                i += 1
            else:
                r = r + 1
                result.append(str[i])
                brace = brace - 1
                i += 1
        elif str[i] == ",":
            result[r] += str[i]
            # Corner case check.
            if str[i + 1]=="{" or str[i + 1] == "[":
                i += 1
                continue
            else:
                r = r + 1
                result.append('\t' * brace)
                i += 1
        elif str[i] == ":":
            result[r] += str[i]
            if str[i + 1] == "{" or str[i + 1] == "[":
                r = r + 1 
                result.append('\t' * brace)
                i = i + 1
                result[r] += str[i]
                brace = brace + 1
                if str[i + 1] != "{" and str[i + 1] != "[":
                    r = r + 1
                    result.append('\t' * brace)
                    i = i + 1
                    result[r] += str[i]
            i += 1
        else:
            # For all other cases.
            result[r] += str[i]
            i += 1
    return result

'''
Sample Input:
3
["foo",{"bar":["baz",null,1.0,2]}]
[{"EmployeeID":1,"Name":"Abhishek","Designation":"SoftwareEngineer"}]
{"EmployeeID":2,"Name":"Garima","Designation":"EmailMarketingSpecialist"}

Desired Output:
[
	"foo",
	{
		"bar":
		[
			"baz",
			null,
			1.0,
			2
		]
	}
]
[
	
	{
		"EmployeeID":1,
		"Name":"Abhishek",
		"Designation":"SoftwareEngineer"
	}
]
{
	"EmployeeID":2,
	"Name":"Garima",
	"Designation":"EmailMarketingSpecialist"
}
'''