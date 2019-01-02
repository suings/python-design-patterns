import json
import xml.etree.ElementTree as etree


class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connector_factory(filepath):
    # 工厂方法,基于文件路径的拓展名返回JSONConnector或XMLConnector的实例
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError("Cannot connect to {}".format(filepath))
    return connector(filepath)


def connect_to(filepath):
    factory = None
    try:
        factory = connector_factory(filepath)
    except ValueError as ve:
        print(ve)

    return factory


if __name__ == '__main__':
    '''
    使用工厂方法处理xml/json文件
    '''
    xml_factory = connect_to('person.xml')
    xml_data = xml_factory.parsed_data
    print(xml_data)

    json_factory = connect_to('person.json')
    json_data = json_factory.parsed_data
    print(json_data)
