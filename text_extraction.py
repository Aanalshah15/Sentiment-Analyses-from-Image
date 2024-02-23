import re,os
direc = r"C:\Users\LENOVO\PycharmProjects\project3\text_extraction\Inputs//"
files = os.listdir(direc)
texts = [direc + text for text in files]

def term_match(string_to_search, term):
    try:
        regular_expression = re.compile(term, re.IGNORECASE)
        result = re.findall(regular_expression, string_to_search)
        if len(result) > 0:
            return result[0]
        else:
            return None
    except Exception:
        print('Error occurred during regex search')
        return None

def read_file(text):
    data = open(text,'r')
    text = data.read()
    return text

email1,contact = [],[]
for i in texts:
    text = read_file(i)
    email = r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}"
    mobile = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
    email1.append(term_match(text,email))
    contact.append(term_match(text,contact))

print(email1,contact)
#
# result = re.findall(mobile,text)
# result1 = re.findall(email,text)

# print(result,result1)


# ------------







