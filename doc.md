Help on module email_util:

NAME
    email_util

CLASSES
    builtins.object
        SendMail
    
    class SendMail(builtins.object)
     |  ʵ�ø������ָ�������ַ�����ʼ�
     |  
     |  Methods defined here:
     |  
     |  parse_options(self)
     |      �����ⲿ��������
     |      -f from_name
     |      -t to_name
     |      -s subject
     |      -c content
     |      -p pwd
     |      -r smtp_server
     |      -a to_addr
     |      :return:
     |  
     |  send_mail(self, from_name, to_name, subject, content, from_addr, pwd, to_addr, smtp_server)
     |      �����ʼ�
     |      :param from_name: ���ͷ����֣��������ͣ���ָ�����
     |      :param to_name: �ռ������֣��������ͣ���ָ�����
     |      :param subject: �ʼ�����
     |      :param content: �ʼ�����
     |      :param from_addr: ���ͷ������ַ���������ͣ���ָ�����
     |      :param pwd: ���ͷ���������
     |      :param to_addr: ���ͷ������ַ���������ͣ���ָ�����
     |      :param smtp_server: ���ͷ���������
     |      :return:
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FILE
    d:\pythoncode\floorutil\floorutil\email_util.py


