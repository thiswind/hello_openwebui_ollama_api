import os

# 设置环境变量
# os.environ['MY_VAR'] = 'Hello, World!'

# 读取环境变量
var_value = os.getenv('API_KEY')

print(var_value)  # 输出：Hello, World!