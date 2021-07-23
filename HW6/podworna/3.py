def calculates_number_char(string_input):
   result={}
   for x in string_input:
      if x in result:
         continue
      else:
         result.update({str(x): string_input.count(x)})
   return result
      
print(calculates_number_char('pythonHTMLcssJS   '))