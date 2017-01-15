## 正则表达式
1. 利用正则表达式查找文本

re.compile(pattern)
Regex.search(str) 返回Match对象
Match.group() 返回实际匹配的字符串

2. 匹配更多模式
pattern 中加括号，表示分组
Match.group(index)可返回相应分组匹配结果 groups获取所有分组

|：管道，匹配其中一种规则，如：r'Batman|Tina Fey'
search 查找到第一个匹配立即返回
Bat(man|mobile|copter)
?：匹配零次或一次，如：r'Bat(wo)?man'
*：匹配零次或多次，如：r'Bat(wo)*man' 可匹配多个重复的 wo
+：匹配一次或多次
{}：匹配特定次数，如 r'(Ha){3}' 'HaHaHa'; r'(Ha){3,} 三次或更多; r'(Ha){3,5} 3到5次; r'(Ha){,5} 0到5次
贪心匹配：匹配最长；非贪心匹配：在{}后加?号，匹配最短；

3. findall()
search返回第一次匹配，返回结果为Match对象；
findall返回所以匹配，返回结果为字符串列表（无分组），返回元组列表（有分组）；

4. 字符分类
\d:0-9任何数字，\D:0-9以外的任何字符；
\w:字母、数字或下划线，\W:其他；（只匹配一个字符，\w+匹配一个单词）
\s:空格、制表符或换行符，\S:其他；
[0-5]:0-5的数字

5. 自己的字符分类
r'[aeiouAEIOU]':匹配所以 a e i... 字符
r'[a-zA-Z0-9]':匹配所有大小写字母和数字；
[]内不会解释正则表达式，其他字符无需转义；
^:匹配补集，如：r'[^aeiouAEIOU]'

正则表达式中：
r'^Hello' 匹配以'Hello'开始的字符串
r'\d$'匹配以数字结尾的字符串
r'^\d$'匹配从开始到结束都是数字的字符串

6. 通配字符
.；匹配除换行之外的所有字符；如：r'.at' cat; .之匹配一个字符
.*:匹配所以字符，贪心匹配；
.*?：非贪心匹配 
如：'<To serve man> for dinner.>'
r'<.*>'  :'<To serve man> for dinner.>'
r'<.*?>' :'<To serve man>'
re.compile('.*', re.DOTALL)匹配所以字符（包括换行符）

7. 不区分大小写
re.compile(r'robocop', re.I) re.I = re.IGNORECASE

8. 替换字符串
Regex.sub(A, B) 用A替换B中匹配的字符串；
使用匹配结果替换匹配内容：
如：
agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
'A**** told C**** that E**** knew B**** was a double agent.'

9. 复杂的正则表达式
re.compile(''' ''', re.VERBOSE) 使正则表达式可以分开写,'''''' 为分行字符串

10. 组合 re.*
someRegex = re.compile('foo', re.I | re.DOTALL | re.VERBOSE)