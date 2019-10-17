# MyWeatherSpider
爬取天气网数据

## 数据来源 [天气网](lishi.tianqi.com)

## 注意事项
  运行时需要对getCityName.py中的`each_person`进行修改，0、1、2、3、4、5、6、7分别对应爬取A-C、D-F、G-I、J-L、M-O、P-R、S-V、W-Z的城市

## 使用方法
- 在命令行中输入 `pip install pyenv-win --target %USERPROFILE%/.pyenv`
- 在命令行中输入 `pip install pipenv`
- 进入到该文件目录下，输入 `pipenv install`
- 完成后输入 `pipenv shell` 进入**虚拟环境**
- 输入 `python getCityName.py`
- 完成代码运行以后输入 `exit` 退出虚拟环境

## 爬取后的文件处理
1、将所有爬取的数据放到一个空文件夹中，例如放在D:中，文件夹命名为delete_data

2、新建一个空文件夹，例如放在D:中，文件夹命名为out_data

3、将delete.py中的第3行中的r"path1"替换成r"D:\\delete_data"  （注意这里没有双斜线）
     将delete.py中的第36行中的r"path2"替换成r"D:\\out_data\\"  （注意这里有双斜线）

4、运行后，out_data文件夹中将会生成对应的相同名称的文件
