# -*- coding:utf-8 -*-
# Author:yangsc
#weiapp_article_classify

# https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=ZTsf3EQc47PkP0WMDexHnvNh&client_secret=2jdWGEnr4xFdzfvZ26uqlne4MjnVD9p6&

# {"access_token":"24.6a8a7dc73b0937702421f69582adc0d0.2592000.1523607216.282335-10926098",
# "session_key":"9mzdDZfPFInXJRKcYOY6DX0Itkyx5UANnDoSyaSZvmgjg+AuiUIWl9gRerqn0PVaye93cnB4EtXQrkSSu2LvJZ6HjI+u9A==",
# "scope":"public nlp_simnet nlp_wordemb nlp_comtag nlp_dnnlm_cn brain_nlp_lexer brain_all_scope brain_nlp_comment_tag brain_nlp_dnnlm_cn brain_nlp_word_emb_vec brain_nlp_word_emb_sim brain_nlp_sentiment_classify brain_nlp_simnet brain_nlp_depparser brain_nlp_wordembedding brain_nlp_dnnlm_cn_legacy brain_nlp_simnet_legacy brain_nlp_comment_tag_legacy brain_nlp_lexer_custom brain_nlp_keyword brain_nlp_topic wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower bnstest_fasf lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission",
# "refresh_token":"25.c47548f8f35d26d3732073013c920043.315360000.1836375216.282335-10926098",
# "session_secret":"ba8cae9a9087e96cba6f927801a699ff","expires_in":2592000}


# https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer?access_token=24.6a8a7dc73b0937702421f69582adc0d0.2592000.1523607216.282335-10926098

from aip import AipNlp
import pandas as pd
import time 

# """ 你的 APPID AK SK """
APP_ID = '10926098'
API_KEY = 'ZTsf3EQc47PkP0WMDexHnvNh'
SECRET_KEY = '2jdWGEnr4xFdzfvZ26uqlne4MjnVD9p6'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def parse_jsonData2(json_data):
    lv_tag=[]
    if json_data is None:
        return lv_tag
    if 'items' in json_data.keys():
        items=json_data['items']
        if len(items)>=1:
            lv_tag=([i['tag'] for i in items])
    return lv_tag
        
# 文章内容读取
# filename = 'D:\企业号分析\\tmp_s_weiapp_cms_article_data.txt' 
filename = '/qyh/shell/weekly_report/data/tmp_s_weiapp_cms_article_data.txt' 

# filename = 'D:\\企业号分析\\test.txt' 
i=0
# outputfile = 'D:\\企业号分析\\articlr_keywords_result.txt'
outputfile = '/qyh/shell/weekly_report/data/articlr_keywords_result.txt'
file_to_write = open(outputfile,'a+',encoding='UTF-8')
with open(filename, 'r',encoding='UTF-8') as file_to_read:
    while True:
        lines = file_to_read.readline() # 整行读取数据
        if not lines or i>100000 :
            break
        if i>=0:
            title,content = lines.split('\t')
            content="".join(content.split())
            # print(title,content)
            json_data=client.keyword(title,content)
            # print (json_data)
            lv_tag =parse_jsonData2(json_data)
            # print(lv_tag)
            lv_tag=" ".join(lv_tag)
            result = [str(i),title,lv_tag]
            if i%100==0:
                print(result)
            file_to_write.write(",".join(result))
            file_to_write.write("\n")
        i=i+1
        # time.sleep(0.001)
        
file_to_write.close()        
        
        
        

# title = "北京保监局"
# content= """
# 5月13日，北京保监局陆玉华处长一行莅临信诚人寿北京分公司，对电子投保工作进行调研。保监局领导听取了北分的工作汇报会并提出指导意见，总公司副首席营运官戴华雨，北京分公司总经理齐彤、副总经理张颖，及客服部门负责人参加了本次会议。 　　会上，戴华雨总汇报了信诚在电子化展业方面的发展情况，介绍了信诚在服务理念、新契约回访以及系统方面进行的创新。随后信诚伙伴现场演示了电子投保和电子回访的流程。陆处长对信诚积极探索实践、提升服务品质的努力给予了正面评价，并就电子投保的流程优化提出了指导意见。 　　2013年，信诚预见到电子投保市场的快速发展，成立了“信易通”专项项目小组。“信易通”平台涵盖了营销员增员、客户需求分析、电子投保、保全、理赔，以及客户网上服务、营销员销售支持等内容。为了提升客户体验，信诚在客户需求分析板块投入了大量精力，逐步扭转了营销员以产品为主导的销售习惯，在销售中更注重贴合客户的实际需求。这个创新获得了客户和营销员两方面的高度评价。为了真正实现电子投保无纸化，安全可靠的电子签名至关重要。针对目前大部分同业采用Pad收集电子签名，容易引起法律纠纷的情况，信诚引用北京CA的技术，采用了完整的证据链的模式，让电子签名的可信度大大上升，提升了电子投保的安全性。为了提升服务品质，信诚加强了对营销员的资质管理，配套推出了《合规责任书》、《营销员专业品质管理办法》两项制度。对营销员进行分类管理、分级授权。对德才兼备的优秀销售人员大胆赋予授权；对口碑较差的营销员则进行重点监控，在产品种类及服务提供方面给予严格限制。 　　北分电子投保服务自上线后，打破了传统投保模式的局限，30分钟即可完成投保、承保手续，为客户带来巨大的便利。截至2014年4月，北分当月的电子投保率已达到88%。经过近半年的实践，北分积累了很多经验，在电子投保风险管控和品质管理方面均取得较大突破。 　　电子投保简便、快捷、安全、绿色、透明，大大提升了客户满意度。未来，北分将根据监管部门的指导意见进一步完善工作，对电子投保业务进行更多探索，为客户提供更优质的保险服务。
# """
# print ()
# json_data=client.topic(title,content)
# print (json_data)
# lv1_tag=parse_jsonData(json_data)[0]
# lv2_tag=parse_jsonData(json_data)[1]
# print('********',title,content[0:10],lv1_tag,lv2_tag)

# print (text_classify)


# title = "欧洲冠军杯足球赛"

# content = "欧洲冠军联赛是欧洲足球协会联盟主办的年度足球比赛，代表欧洲俱乐部足球最高荣誉和水平，被认为是全世界最高素质、最具影响力以及最高水平的俱乐部赛事，亦是世界上奖金最高的足球赛事和体育赛事之一。"

# json_data=client.topic(title,content)
# print (json_data)
# lv1_tag=parse_jsonData(json_data)[0]
# lv2_tag=parse_jsonData(json_data)[1]
# print('********',title,content[0:10],lv1_tag,lv2_tag)




