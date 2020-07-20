import os
import paramiko  # 用于调用scp命令
from scp import SCPClient


def upload_file(file_name, remote_path, file_path):
    """将指定文件上传到服务器指定目录"""

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(host, port, username, password)
    scpclient = SCPClient(ssh_client.get_transport(), socket_timeout=15.0)
    local_path = file_path + "/" + file_name
    try:
        scpclient.put(local_path, remote_path)
    except FileNotFoundError as e:
        print(e)
        print("系统找不到指定文件" + local_path)
    else:
        print(file_name, "文件上传成功")
    ssh_client.close()


def upload_files(remote_path, file_path):
    """将指定文件下所有文件上传到服务器指定目录"""
    all_file = os.listdir(file_path)
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(host, port, username, password)
    scpclient = SCPClient(ssh_client.get_transport(), socket_timeout=15.0)
    for name in all_file:
        local_path = file_path + "/" + name
        try:
            scpclient.put(local_path, remote_path)
        except FileNotFoundError as e:
            print(e)
            print("系统找不到指定文件" + local_path)
        else:
            print(file_name, "文件上传成功")
    ssh_client.close()


if __name__ == '__main__':
    host = ""           # 服务器ip地址
    port = 22           # 端口号
    username = ""       # ssh 用户名
    password = ""       # 密码
    file_name = ""      # file_name是file_path本地文件夹路径下面的文件名称
    remote_path = ""    # remote_path 远程服务器目录
    file_path = ""      # file_path   本地文件夹路径
    if file_name == "" or file_name == None or os.path.exists(file_path + "/" + file_name):
        upload_files(remote_path, file_path)
    else:
        upload_file(file_name, remote_path, file_path)
