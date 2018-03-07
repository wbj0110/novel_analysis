#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from basic import *
import pandas as pd
import jieba.posseg
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread
import random


def cut_words_with_pos(text):
    seg = jieba.posseg.cut(text)
    res = []
    for i in seg:
        if i.flag in ["a", "v", "x", "n", "an", "vn", "nz", "nt", "nr"] and is_fine_word(i.word):
            res.append(i.word)

    return list(res)


def person_word(name):
    lines = open("data/芳华-严歌苓.txt", "r").readlines()
    word_list = []
    for line in lines:
        if name in line:
            words = cut_words_with_pos(line)
            word_list += words

    print(word_list)
    print(len(word_list))

    return word_list


def count(word_list):
    return pd.Series(word_list).value_counts()


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


def draw_cloud(mask_path, word_freq, save_path):
    # mask = np.array(Image.open(mask_path))
    mask = imread(mask_path)
    wc = WordCloud(font_path='/System/Library/Fonts/STHeiti Light.ttc',  # 设置字体
                   background_color="black",  # 背景颜色
                   max_words=1000,  # 词云显示的最大词数
                   mask=mask,  # 设置背景图片
                   max_font_size=80,  # 字体最大值
                   random_state=42,
                   )
    wc.generate_from_frequencies(word_freq)
    # store to file

    # show
    image_colors = ImageColorGenerator(mask)
    plt.figure()
    plt.imshow(wc.recolor(color_func=image_colors), interpolation='bilinear')
    plt.axis("off")
    # wc.to_file(save_path)
    plt.show()
    return


if __name__ == '__main__':
    # word_list = person_word("何小嫚")
    # freq = count(word_list)
    # input_freq = freq.to_dict()
    # print(input_freq)
    input_freq = {'何小嫚': 216, '刘峰': 77, '母亲': 52, '头发': 33, '父亲': 32, '团长': 28, '老师': 28, '眼睛': 21, '演出': 20, '女兵': 20, '卫生员': 20, '女儿': 19, '丁丁': 19, '战士': 17, '首长': 17, '所有人': 16, '看着': 16, '身体': 16, '舞蹈': 16, '年轻': 15, '骑兵': 14, '发现': 13, '点儿': 13, '护士': 12, '牺牲': 11, '朱克': 11, '医院': 11, '名字': 11, '女人': 11, '辫子': 10, '男兵': 10, '厅长': 10, '同志': 10, '新兵': 10, '排长': 9, '丈夫': 9, '照片': 9, '军帽': 9, '服装': 9, '秘密': 9, '轻伤': 9, '衬衫': 9, '感觉': 9, '离开': 9, '小何': 8, '报道': 8, '希望': 8, '胆石': 8, '想象': 8, '装病': 8, '目光': 8, '舞台': 8, '继父': 8, '跟着': 8, '排练': 7, '掌上明珠': 7, '告诉': 7, '家庭': 7, '体温计': 7, '父母': 7, '流传': 7, '记得': 7, '前线': 7, '生命': 7, '只能': 7, '闹钟': 7, '火线': 7, '帽子': 7, '部队': 7, '生活': 7, '军区': 7, '前夫': 6, '报纸': 6, '包扎': 6, '优越': 6, '承认': 6, '眼泪': 6, '军装': 6, '悲哀': 6, '生病': 6, '剪断': 6, '发生': 6, '高烧': 6, '名目': 5, '男舞者': 5, '司机': 5, '玩儿': 5, '班长': 5, '战友': 5, '政治部': 5, '动作': 5, '同情': 5, '见到': 5, '活儿': 5, '手指': 5, '天使': 5, '结束': 5, '文工团': 5, '走廊': 5, '号叫': 5, '发出': 5, '野战医院': 5, '孩子': 5, '善良': 5, '护理员': 5, '故事': 5, '地方': 5, '捎来': 5, '说话': 5, '表扬': 5, '事件': 5, '成长': 5, '口音': 5, '坏话': 5, '正当': 5, '范儿': 4, '时间': 4, '不想': 4, '文人': 4, '火车': 4, '城管': 4, '骑兵团': 4, '队长': 4, '搂抱': 4, '走出': 4, '不到': 4, '提出': 4, '镜子': 4, '太久': 4, '精彩': 4, '倒下': 4, '回到': 4, '小鬼': 4, '证明': 4, '回去': 4, '军马': 4, '毛巾': 4, '精神科': 4, '明白': 4, '爸爸': 4, '痕迹': 4, '集体舞': 4, '梳头': 4, '角色': 4, '程度': 4, '网兜': 4, '家境': 4, '机会': 4, '结婚': 4, '背着': 4, '触摸': 4, '坐在': 4, '危险': 4, '来到': 4, '热爱': 4, '托举': 4, '能量': 4, '等待': 4, '哨兵': 4, '弄堂': 4, '凝聚力': 4, '羡慕': 4, '放弃': 4, '分队': 4, '软弱': 4, '上当': 4, '活动': 4, '焦虑': 4, '缠绵': 4, '位置': 4, '灯光': 4, '车队': 4, '保障': 4, '大幕': 3, '横幅': 3, '送到': 3, '排练厅': 3, '靠拢': 3, '送行': 3, '有限': 3, '新兵训练': 3, '掌声': 3, '连队': 3, '形容': 3, '粪便': 3, '流通': 3, '走进': 3, '驾驶员': 3, '著名': 3, '情景': 3, '原因': 3, '稿子': 3, '团支部': 3, '编撰': 3, '肩膀': 3, '手艺': 3, '打开': 3, '表演': 3, '负伤': 3, '媒人': 3, '自信': 3, '奖品': 3, '面孔': 3, '辅导员': 3, '练功': 3, '洗浴': 3, '坏分子': 3, '穿着': 3, '手绢': 3, '参加': 3, '背心': 3, '头晕': 3, '心理': 3, '失望': 3, '解密': 3, '选择': 3, '擦擦': 3, '老兵': 3, '乳罩': 3, '记忆': 3, '质疑': 3, '登记簿': 3, '冰棍': 3, '舞蹈队': 3, '舞者': 3, '证实': 3, '小说': 3, '接下去': 3, '出汗': 3, '牙膏': 3, '艰苦': 3, '转业': 3, '伐木': 3, '轿车': 3, '弟弟': 3, '先进': 3, '出路': 3, '创作': 3, '油条': 3, '住院': 3, '体温': 3, '领导': 3, '看成': 3, '显得': 3, '脑袋': 3, '进门': 3, '台词': 3, '事实': 3, '发烧': 3, '帮忙': 3, '听到': 3, '裤衩': 3, '作弊': 3, '邀请': 3, '自杀': 3, '军马场': 3, '慰问': 3, '嘴唇': 3, '学校': 3, '十克拉': 3, '腐蚀': 3, '科室': 3, '胳肢窝': 3, '小病': 3, '不该': 3, '听见': 3, '舞剧': 3, '队形': 3, '标兵': 3, '病号': 3, '组织': 3, '接兵': 3, '相当于': 3, '碰到': 3, '椅子': 3, '宿舍': 3, '伤痛': 3, '院子': 3, '解释': 3, '报告': 3, '不见': 3, '好看': 3, '抗命': 3, '世界': 3, '招待所': 3, '污点': 3, '考生': 3, '历史': 3, '关爱': 2, '入伍': 2, '导演': 2, '生意': 2, '神龛': 2, '抗争': 2, '银灰': 2, '可爱': 2, '沉默': 2, '泄露': 2, '世纪': 2, '马路': 2, '白色': 2, '担心': 2, '保健': 2, '织补': 2, '取出': 2, '身世': 2, '异类': 2, '瘌痢': 2, '塞进': 2, '摄制组': 2, '短暂': 2, '浑身': 2, '音乐': 2, '后台': 2, '咕哝': 2, '出场': 2, '服务员': 2, '微妙': 2, '马戏': 2, '遗憾': 2, '相貌': 2, '关怀': 2, '通铺': 2, '士兵': 2, '愿望': 2, '批准': 2, '交界': 2, '遭遇': 2, '喜欢': 2, '穿越': 2, '慈祥': 2, '香蕉': 2, '听说': 2, '场部': 2, '帐篷': 2, '温暖': 2, '昏暗': 2, '嫁妆': 2, '学习': 2, '设备': 2, '没错': 2, '梳理': 2, '橛子': 2, '绝望': 2, '寻找': 2, '扮演': 2, '物件': 2, '厌倦': 2, '是从': 2, '提到': 2, '死结': 2, '摊点': 2, '揭露': 2, '跑操': 2, '追光': 2, '合算': 2, '战胜': 2, '节目': 2, '门诊部': 2, '录音机': 2, '真诚': 2, '带有': 2, '模样': 2, '毛衣': 2, '胡闹': 2, '中央': 2, '恶心': 2, '纪念章': 2, '想起': 2, '副团长': 2, '送给': 2, '洗澡': 2, '起到': 2, '敌人': 2, '老粗': 2, '味儿': 2, '人物': 2, '萌生': 2, '细看': 2, '小心': 2, '叫作': 2, '招生': 2, '招生办': 2, '摇摇头': 2, '剧本': 2, '排骨': 2, '嫌恶': 2, '高明': 2, '花儿': 2, '看护': 2, '箱子': 2, '送回': 2, '把戏': 2, '人和事': 2, '地板': 2, '饼干': 2, '汽车': 2, '解放': 2, '急救': 2, '弹药': 2, '藤椅': 2, '切断': 2, '打着': 2, '政治': 2, '商量': 2, '无耻': 2, '体液': 2, '公园': 2, '病毒': 2, '不用': 2, '拉倒': 2, '号召': 2, '命令': 2, '工作': 2, '下基层': 2, '战争': 2, '头头': 2, '迟到': 2, '彩色': 2, '想到': 2, '利用': 2, '肯定': 2, '指着': 2, '腰肢': 2, '起床号': 2, '新媳妇': 2, '拿出': 2, '图书': 2, '电话': 2, '好像': 2, '转过身': 2, '午饭': 2, '假臂': 2, '木枪': 2, '对面': 2, '模仿': 2, '离婚': 2, '女护士': 2, '孕育': 2, '年糕': 2, '地带': 2, '荣誉': 2, '战地': 2, '拖油瓶': 2, '海拔': 2, '军人': 2, '军功章': 2, '感动': 2, '小分队': 2, '青睐': 2, '足够': 2, '回来': 2, '身份': 2, '声音': 2, '运气': 2, '足尖': 2, '搀扶': 2, '角小': 2, '造假': 2, '眼看': 2, '指令': 2, '主角': 2, '镇压': 2, '试用期': 2, '独舞': 2, '回过': 2, '战场': 2, '司令员': 2, '军服': 2, '皮鞋': 2, '残忍': 2, '电脑': 2, '示范': 2, '副班长': 2, '泡菜': 2, '编导': 2, '休息': 2, '揭穿': 2, '装满': 2, '退货': 2, '个家': 2, '标准': 2, '女性': 2, '社会': 2, '不动': 2, '渴望': 2, '剩下': 2, '闪念': 2, '装扮': 2, '针线': 2, '威严': 2, '友谊商店': 2, '指示': 2, '充满': 2, '陆军医院': 2, '小郝': 2, '打算': 2, '吹响': 2, '认定': 2, '感到': 2, '集体': 2, '老干部': 2, '露天': 2, '方法': 2, '铜锤': 2, '频率': 2, '想念': 2, '叫喊': 2, '设想': 2, '同屋': 2, '感情': 2, '女孩': 2, '营房': 2, '自私': 2, '关系': 2, '口罩': 2, '酷暑': 2, '伤害': 2, '正义': 2, '事物': 2, '材料': 2, '话题': 2, '勾当': 2, '效应': 2, '演员': 2, '教养': 2, '丑闻': 2, '上班': 2, '电报': 2, '得来': 2, '一大': 2, '化装': 2, '指出': 2, '享受': 2, '不出': 2, '光明': 2, '人格': 2, '吃惊': 2, '龙套': 2, '英勇': 2, '红色': 2, '总算': 2, '俱乐部': 2, '结婚照': 2, '全军': 2, '回事': 2, '听出': 2, '摔坏': 2, '知情': 2, '战马': 2, '潜意识': 2, '宣传': 2, '恋爱': 2, '配合': 2, '地址': 2, '医护人员': 2, '军医': 2, '军鼓': 2, '嫁人': 2, '搭档': 2, '命运': 2, '睡衣': 2, '集体创作': 2, '人性': 2, '洗衣': 2, '尼龙袜': 2, '随队': 2, '单位': 2, '轮流': 2, '卡车': 2, '伤员': 2, '合影': 2, '下放': 2, '手指尖': 2, '见证': 2, '行李': 2, '餐桌': 2, '棉被': 2, '掉头': 2, '舞姿': 2, '退役': 2, '碉堡': 2, '活着': 2, '玻璃器皿': 2, '解散': 2, '消费': 2, '取消': 2, '稿纸': 2, '不住': 2, '元帅': 2, '下巴': 2, '肉麻': 2, '床上': 2, '代表': 2, '报告团': 2, '标语': 2, '孤立': 2, '找到': 2, '记住': 2, '欺负': 2, '飞跃': 2, '幼儿园': 2, '走向': 2, '捉弄': 2, '炊事班': 2, '年龄': 2, '总得': 2, '父女俩': 2, '绸带': 2, '炸毁': 2, '嗓音': 2, '传达': 2, '背包': 2, '逃遁': 2, '疼痛': 2, '姑娘': 2, '贪生': 2, '回想': 2, '决策': 2, '纤细': 2, '平常': 2, '丰胸': 2, '仁慈': 2, '天生': 2, '病者': 2, '警卫': 2, '抛弃': 2, '申请书': 2, '我军': 2, '写下': 2, '普通话': 2, '男女': 2, '皮包': 2, '发明': 2, '缺乏': 2, '额头': 2, '锻炼': 2, '发言': 2, '颜色': 2, '对话': 2, '成员': 2, '形象': 2, '能力': 2, '急诊室': 2}

    draw_cloud("data/liu2.png", input_freq, "data/hexiaoman.png")

