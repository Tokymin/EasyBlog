###step1 
安装所需依赖库
pip install -r requirements -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
###step2 
建议新建虚拟环境
###step3 
set FLASK_MODE=default
###step4 
python manage.py runserver --host 0.0.0.0 --port 9008 指定端口运行 

注意step3很重要，如果是本地运行，邮箱验证时记得手机和电脑在同一局域网内。或者用电脑打开邮箱链接进行验证