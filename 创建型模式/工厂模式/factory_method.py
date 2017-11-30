# -*- coding: utf-8 -*-
# author：lyletang
# date: 2017-11-30

import xml.etree.ElementTree as etree
import json

class JSONConnector:
    """类JSONConnector解析JSON文件"""
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)
    
    @property
    def parsed_data(self):
        return self.data

class XMLConnector:
    """类XMLConnector解析XML文件"""
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
    	return self.tree

def connection_factory(filepath):
    '''工厂方法，基于输入文件路径的扩展名返回一个JSONConnector或XMLConnector的实例'''
    if filepath.endswith('json'):
    	connector = JSONConnector
    elif filepath.endswith('xml'):
    	connector = XMLConnector
    else:
    	raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)

def connect_to(filepath):
    """对工厂函数connection_factory的封装，加入异常处理机制"""
    factory = None
    try:
    	factory = connection_factory(filepath)
    except ValueError as ve:
    	print(ve)
    return factory

def main():
    # 确认异常机制生效
    sqlite_factory = connect_to('data/person.sq3')
    print()

    # 工厂方法处理XML文件
    xml_factory = connect_to('data/person.xml')
    #print(type(xml_factory))
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar')) 
    print('found: {} persons'.format(len(liars)))
    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        [print('phone number ({})'.format(p.attrib['type']), p.text) for p in liar.find('phoneNumbers')]
    print()

    # 工厂方法处理JSON文件
    json_factory = connect_to('data/donut.json')
    #print(type(json_factory))
    json_data = json_factory.parsed_data
    print('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
    	print('name: {}'.format(donut['name']))
    	print('price: {}'.format(donut['ppu']))
    	[print('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]

if __name__ == '__main__':
    main()
