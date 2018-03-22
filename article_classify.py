# -*- coding:utf-8 -*-

from aip import AipNlp
import pandas as pd

# """ 你的 APPID AK SK """
APP_ID = '123456789'
API_KEY = 'asdfjklqwertyuiop'
SECRET_KEY = 'asdfjklqwertyuiop123456789'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# 解析返回的json数据
def parse_jsonData(json_data):
    lv1_tag=[]
    lv2_tag=[]
    if json_data is None:
        return [lv1_tag,lv2_tag]
    if 'item' in json_data.keys():
        item=json_data['item']
        lv1_tag_list=item['lv1_tag_list']
        lv2_tag_list=item['lv2_tag_list']
        if len(lv1_tag_list)>=1:
            lv1_tag=[i['tag'] for i in lv1_tag_list]
        if len(lv2_tag_list)>=1:
            lv2_tag=[i['tag'] for i in lv2_tag_list]
    lv_tag=[lv1_tag,lv2_tag]
    return lv_tag
        
# 逐行读取文章列表，提交参数，返回结果
filename = 'article.txt' 
i=0
outputfile = 'result.txt'
file_to_write = open(outputfile,'a+',encoding='UTF-8')
with open(filename, 'r',encoding='UTF-8') as file_to_read:
    while True:
        lines = file_to_read.readline() # 整行读取数据
        if not lines :
            break
        if i>=0 :
            title,content = lines.split('\t')
            content="".join(content.split()) #去掉空格'\xa0'
            # print(title,content)
            json_data=client.topic(title,content)  
            # print (json_data)
            lv_tag =parse_jsonData(json_data)
            lv1_tag=lv_tag[0]
            lv2_tag=lv_tag[1]
            lv1_tag=" ".join(lv1_tag)
            lv2_tag=" ".join(lv2_tag)
            result = [str(i),lv1_tag,lv2_tag,title,content]
            if i%100==0:
                print(result,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            file_to_write.write("\t".join(result))
            file_to_write.write("\n")
        i=i+1
        
file_to_write.close()        
        
