# 配置
配置文件在config.py中，configure.sh可将config.py复制到需要的文件夹中

# 运行
采用flask + nginx(http://nginx.org/en/download.html) + uwsgi(pip install uwsgi)，uwsgi配置文件需要设置对应端口，nginx监听某个端口后将请求转交到uwsgi。
