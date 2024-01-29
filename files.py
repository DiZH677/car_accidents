import json
import xmltodict


# Обработка XML
def from_xml_to_json(path_name_xml):
    with open(path_name_xml, encoding='UTF-8') as xml_file:
        data_dict = xmltodict.parse(xml_file.read(), encoding='UTF-8')

        # Get the list of <tab> elements
        tab_list = data_dict['dtpCardList']['tab']

        # If there's only one <tab> element, convert it into a list
        if not isinstance(tab_list, list):
            tab_list = [tab_list]
        # Checking info of dtp
        for i in range(len(tab_list)):
            # Checking participant without transport
            if "uchInfo" in tab_list[i]["infoDtp"].keys() and not isinstance(tab_list[i]["infoDtp"]["uchInfo"], list):
                tab_list[i]["infoDtp"]["uchInfo"] = [tab_list[i]["infoDtp"]["uchInfo"]]
            # Checking transport of dtp
            if not isinstance(tab_list[i]["infoDtp"]["ts_info"], list):
                tab_list[i]["infoDtp"]["ts_info"] = [tab_list[i]["infoDtp"]["ts_info"]]
            # Checking participant in transport
            for k in range(len(tab_list[i]["infoDtp"]["ts_info"])):
                if "ts_uch" in tab_list[i]["infoDtp"]["ts_info"][k].keys() and not isinstance(tab_list[i]["infoDtp"]["ts_info"][k]["ts_uch"], list):
                    tab_list[i]["infoDtp"]["ts_info"][k]["ts_uch"] = [tab_list[i]["infoDtp"]["ts_info"][k]["ts_uch"]]


        # Generate the JSON data
        json_data = json.dumps(tab_list, ensure_ascii=False, indent=4)
        # Write the JSON data to the output file
        with open(f"{path_name_xml[:-4]}.json", "w") as json_file:
            json_file.write(json_data)


if __name__ == "__main__":
    path_fname = "./data/February2023.xml"
    from_xml_to_json(path_fname)
