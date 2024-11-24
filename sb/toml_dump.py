import json



class TOMLWrite:

    # List to String
    def list(data: list) -> str:
        if not data:
            return "[]"
        text = "[\n"

        list_len = len(data)

        for i in range(list_len):
            if i == list_len - 1:
                text = text + "   " + "\"" + str(data[i]) + "\"" + "\n"
            else:
                text = text + "   " + "\"" + str(data[i]) + "\"" + "," + "\n"


        text += "]"

        return text


    def dump(file_obj, data: dict):
        for key in data:
            if type(data[key]) is dict:
                sub_data = data[key]

                file_obj.write(f"\n[{key}]\n")

                for k in sub_data:
                    if type(sub_data[k]) is dict:
                        file_obj.write(f"{k} = " + json.dumps(sub_data[k]))
                    
                    elif type(sub_data[k]) is list:
                        file_obj.write(f"{k} = " + TOMLWrite.list(sub_data[k]))


                    elif type(sub_data[k]) is bool:
                        if sub_data[k]:
                            file_obj.write(f"{k} = true")
                        else:
                            file_obj.write(f"{k} = false")

                    else:
                        if sub_data[k] == "":
                            sub_data[k] = "\"\""
                        file_obj.write(f"{k} = {sub_data[k]}")

                    file_obj.write("\n")

            
            elif type(data[key]) is list:
                file_obj.write(f"{key} = " + TOMLWrite.list(data[key]))

            elif type(data[key]) is bool:
                if data[key]:
                    file_obj.write(f"{key} = true")
                else:
                    file_obj.write(f"{key} = false")


            else:
                if data[key] == "":
                    data[key] = "\"\""
                file_obj.write(f"{key} = {data[key]}")

            file_obj.write("\n")