'''
❓ PROMPT
You're working on a finance application and need to format monetary amounts in the following manner for accounting purposes. Every number must adhere to a strict set of rules:

1. All amounts are rounded to two decimal places, even if it is .00.
2. A $ precedes the first digit.
3. Thousands, millions, billions, etc have commas between every 3 digits from the left of the decimal.
4. Negative numbers are surrounded by parentheses.
5. If the absolute amount is less than 1, there should still be a zero before the '.'

Write a function that takes a numeric value and outputs the "finance formatted" string representation.

This is a very realistic data processing problem with lots of special cases!

Example(s)
moneyFormat(1) == "$1.00"
moneyFormat(-1) == "($1.00)"
moneyFormat(16) == "$16.00"
moneyFormat(123) == "$123.00"
 

🔎 EXPLORE
List your assumptions & discoveries:
- takes a number and spits out a dollar amount
- 
 

Insightful & revealing test cases:
- 0 -> $0.00
- 1.2456 -> $1.25
- 1.999 -> 2.00
- 1.399 -> 1.40
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- we'll end up iterating over the input number in some way
- create a new string to put everything in
Time: O(n)
Space: O(n)
 

📆 PLAN
Outline of algorithm #: 
- need to round to two decimal places no matter what
- need to check if it's negative (should add parentheses add the end if it is)
- extract non decimal part, and then put in commas every three
- extract decimal part, rounded two and up if needed, add to our string.  if there's no decimal part, add .00
 

🛠️ IMPLEMENT
function moneyFormat(amount) {
def moneyFormat(amount: float) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
import decimal

def moneyFormat(amount):

    amount = decimal.Decimal(str(amount))

    amount = amount.quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_HALF_UP)
    negative = False

    if amount < 0:
        negative = True
        amount = abs(amount)
    
    # extract integer part
    integer_part = str(int(amount))
    if integer_part == "0":
        decimal_part = str(amount - int(amount))[3:]
    else:
        decimal_part = str(amount - int(amount))[2:]

    print(integer_part, "Integer")
    print(decimal_part, "Decimal")

    # figure out commas
    integer_part_result = ""
    for i in range(len(integer_part)):
        # need to count backwards, add a comma every three, if i % 3 == 0, add a comma (before the three digits)
        if i > 0 and (len(integer_part) - i) % 3 == 0:
            integer_part_result += ","
        integer_part_result += integer_part[i]
    
    # add decimals if necessary
    while len(decimal_part) < 2:
        decimal_part += "0"
    
    if negative:
        result = "($" + integer_part_result + "." + decimal_part + ")"
        return result

    result = "$" + integer_part_result + "." + decimal_part
    return result


# happy cases



print(moneyFormat(-0.001), "($0.00)")


