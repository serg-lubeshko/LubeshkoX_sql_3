import json
from dict2xml import dict2xml


# def save_result(f):
#     def wrapped(self,*args, **kwargs):
#         res, text_file_res = f(self, *args, **kwargs)
#         head = res.description
#         result = res.fetchall()
#         SaveResultJsonXml.dictfetchall(head, result, text_file_res)
#     return wrapped

class SaveResultJsonXml:
    data = None
    file_text = None

    @classmethod
    def save(cls):
        with open(f'{SaveResultJsonXml.file_text}.json', 'w') as f:
            json.dump(cls.data, f)

    @classmethod
    def save_xml(cls):
        xml_data = {'div': cls.data}
        res = dict2xml(xml_data, wrap="main", indent=" ")
        with open(f'{SaveResultJsonXml.file_text}.xml', 'w') as f:
            f.write(res)

    @staticmethod
    def dictfetchall(heads, rv, text):

        row_headers = [x[0] for x in heads]
        json_data = []
        for result in rv:
            json_data.append((dict(zip(row_headers, result))))

        SaveResultJsonXml.file_text = text
        SaveResultJsonXml.data = json_data
        SaveResultJsonXml.save()
        SaveResultJsonXml.save_xml()
