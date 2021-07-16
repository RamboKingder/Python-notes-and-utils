# 这个文件中都是一些我写的python的使用的函数，可以直接复制过去使用



# 使用正则，将一段长文本中的标点符号去除并将文本分成纯文字的列表
import re
def text_split(origin_str):
    pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'
    result_list = re.split(pattern, origin_str)
    while '' in result_list:
        result_list.remove('')

    return result_list
  
  
  
  
