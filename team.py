import json
from filesave import folder_save, image_save


def members(soup):
    baja_site = soup.find('div', class_="container")
    baja_sites = baja_site.find_all('div', id="group")
    member_data = []
    counter = 1
    folder_save('team_image')
    for idx, j in enumerate(baja_sites):
        heading = j.find('div', id="heading")
        if idx == 0:
            heading = "Faculty Advisor"
        else:
            heading = heading.text.strip()
        row = j.select("div[id*=row]")
        member_column = j.find_all('li')
        curr = {
            "id": idx + counter,
            "type": str(heading)
        }
        baja_members = []
        if row:
            for ids, x in enumerate(row):
                counter += 1
                col1 = x.find('div', class_="column1").find('img')
                col2 = x.find('div', class_="column2").find_all(['h3', 'p'])
                name = str(col2[0].text.strip()).replace('\u200b', '').replace('\n', '')
                position = str(col2[1].text.strip())
                description = str(col2[2].text.strip())
                col3 = x.find('div', class_="column3").find('a')
                linked_in = False
                image_save('team_image', name, str(col1['src']))
                if col3:
                    linked_in = str(col3['href'])
                person = {
                    "id": counter + ids + idx,
                    "name": name,
                    "position": position,
                    "description": description,
                    "linked_in": linked_in
                }
                baja_members.append(person)
            a = {"members": baja_members}
            curr.update(a)
            member_data.append(curr)
            counter += 5
        elif member_column:
            baja_members = []
            counter += 15
            for ind, k in enumerate(member_column):
                counter += 1
                person = {
                    "id": counter + ind,
                    "name": str(k.text.strip()),
                    "position": "member"
                }
                baja_members.append(person)
            a = {"members": baja_members}
            curr.update(a)
            member_data.append(curr)
            break
    with open('members.json', 'w', encoding='utf-8') as outfile:
        print('test')
        json.dump(member_data, outfile, ensure_ascii=False, indent=4)
