def joinList(l):
    str_l = ""
    return(str_l.join(l))

def timeconvert(str1):
    string_con = list(str1)
    add_zero = "0"
    add_one = "1"
    add_two = "2"
    add_colon = ":"
    if len(str1) == 8:
        if str1[-2:] == "am":
            if str1[:2] == "12":
               string_con[0] = "0"
               string_con[1] = "0"
            del string_con[5:8]
            return joinList(string_con)
        if str1[-2:] == "pm":
            if str1[:2] != "12":
                add_digit_two = string_con[0]
                add_digit_two = int(add_digit_two) + 1
                string_con[0] = str(add_digit_two)
                add_digit_two = string_con[1]
                add_digit_two = int(add_digit_two) + 2
                string_con[1] = str(add_digit_two)
            del string_con[5:8]
            return joinList(string_con)
    elif len(str1) == 7:
        if str1[-2:] == "am":
            if str1[:2] == "12":
                string_con.insert(0, "00")
            else:
                string_con.insert(0, add_zero)
            del string_con[5:8]
            return joinList(string_con)
            #print(string_con)
        elif str1[-2:] == "pm":
            if int(str1[0]) == 8 | int(str1[0]) == 9:
                if int(str1[0]) == 8:
                    string_con[0] = "20"
                elif int(str1[0]) == 9:
                    string_con[0] = "21"
            else:
                string_con.insert(0, add_one)
                add_digit_two = string_con[1]
                add_digit_two = int(add_digit_two) + 2
                string_con[1] = str(add_digit_two)
            del string_con[5:8]
            return joinList(string_con)
    elif len(str1) == 5:
        string_con.insert(2, add_colon)
        string_con.insert(3, add_zero)
        string_con.insert(4, add_zero)
        if str1[-2:] == "am":
            if str1[:2] == "12":
               string_con[0] = "0"
               string_con[1] = "0"
            del string_con[5:8]
            return joinList(string_con)
        elif str1[-2:] == "pm":
            if str1[:2] == "12":
                del string_con[5:8]
                return joinList(string_con)
            add_digit_one = string_con[0]
            add_digit_one = int(add_digit_one) + 1
            string_con[0] = str(add_digit_one)
            add_digit_two = string_con[1]
            add_digit_two = int(add_digit_two) + 2
            string_con[1] = str(add_digit_two)
            del string_con[5:8]
            return joinList(string_con)
    elif len(str1) == 4:
        if str1[-2:] == "pm":
            if int(str1[0]) == 8 | int(str1[0]) == 9:
                if int(str1[0]) == 8:
                    string_con[0] = "20"
                elif int(str1[0]) == 9:
                    string_con[0] = "21"
                #print(string_con)
                string_con.insert(1, add_colon)
                string_con.insert(2, add_zero)
                string_con.insert(3, add_zero)
                add_digit_two = string_con[1]
            del string_con[5:8]
            return joinList(string_con)
            #print(string_con)
        if str1[-2:] == "am":
            if str1[:2] == "12":
               string_con[0] = "0"
               string_con[1] = "0"
            string_con.insert(0, add_zero)
            string_con.insert(2, add_colon)
            string_con.insert(3, add_zero)
            string_con.insert(4, add_zero)
        elif str1[-2:] == "pm":
            string_con
        del string_con[5:8]
        return joinList(string_con)

#Driver 

my_list = ["12:00 am", "12:30 am", "12:00 pm", "11:30 am","11:30 pm", "11:00 am", "11:00 pm", "11 am", "11 pm", "9 am", "9 pm", "12 am", "12 pm", "7:30 am", "7:30 pm"]

for i in range(len(my_list)):
    print(timeconvert(my_list[i]))

#print(timeconvert(my_list[0]))

#test = "9 pm"
#print(timeconvert(test))

# 00:00
# 00:30
# 12:00
# 11:30
# 23:30
# 11:00
# 23:00
# 11:00
# 23:00
# 09:00--
# 21:00
# 00:00
# 12:00
# 07:30
# 19:30
