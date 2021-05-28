# 配置
配置文件在config.py中，configure.sh可将config.py复制到需要的文件夹中

# 运行
采用flask + nginx(http://nginx.org/en/download.html) + uwsgi(pip install uwsgi)，uwsgi配置文件需要设置对应端口，nginx监听某个端口后将请求转交到uwsgi。

# 授权
本程序遵循MIT协议，对所有人免费，可以任意处置，包括使用，复制，修改，合并，发表，分发，再授权，或者销售。唯一的限制是，软件中必须包含上述版权和许可提示。
