def main():
    import os
    os.system("cls")

    def func(string):
        string_len = len(string)
        string_arr = [""] * string_len
        temp_arr = [0] * string_len
        temp = 0
        my_dict = {}
        for i in range(string_len):
            string_arr[i] = string[i]

        for i in range(string_len):
            for j in range(string_len):
                if string_arr[i] == string_arr[j]:
                    temp = 1
                    temp_arr[j] += temp
                    my_dict[string_arr[j]] = temp_arr[j]
                else:
                    temp = 0
                    temp_arr[j] += temp
                    my_dict[string_arr[j]] = temp_arr[j]
        return my_dict

    print(func("hello world"))