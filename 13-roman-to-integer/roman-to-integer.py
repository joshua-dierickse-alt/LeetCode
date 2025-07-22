class Solution:
    def romanToInt(self, s: str) -> int:
        # Roman to Integer


        numeral_dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        string_list = s.replace(""," ").split()

        string_list.append("end")

        num_counter = 0

        skip_bool = False

        for i in range(len(string_list) - 1):
            if skip_bool == False:
                if string_list[i] == "I" and (string_list[i + 1] == "V" or string_list[i + 1] == "X"):
                    num_counter += numeral_dic[string_list[i + 1]] - numeral_dic[string_list[i]]
                    skip_bool = True
                elif string_list[i] == "X" and (string_list[i + 1] == "L" or string_list[i + 1] == "C"):
                    num_counter += numeral_dic[string_list[i + 1]] - numeral_dic[string_list[i]]
                    skip_bool = True
                elif string_list[i] == "C" and (string_list[i + 1] == "D" or string_list[i + 1] == "M"):
                    num_counter += numeral_dic[string_list[i + 1]] - numeral_dic[string_list[i]]
                    skip_bool = True
                else:
                    num_counter += numeral_dic[string_list[i]]
            else:
                skip_bool = False

        return num_counter