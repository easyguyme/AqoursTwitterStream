# Aqours ����ʵʱת�� Telegram

�� Python �ű�����ʵ�ֽ� Aqours ��Ա����ʵʱת���� Telegram �����˵Ĺ��ܡ�Aqours ��Ա���طֱ�Ϊ�������

* [�����Ә�](https://twitter.com/anju_inami)
* [����������](https://twitter.com/Rikako_Aida)
* [Ռ�L�ʤʤ�](https://twitter.com/suwananaka)
* [С�m�м�](https://twitter.com/box_komiyaarisa)
* [��������](https://twitter.com/Saito_Shuka)
* [С�֐���](https://twitter.com/Aikyan_)
* [�ߘ����ʤ�](https://twitter.com/Kanako_tktk)
* [�ľ����](https://twitter.com/aina_suzuki723)
* [��ᦐ�](https://twitter.com/furihata_ai)

����ʵ�ֵĹ����У�

1. ת�����������Լ�������ý�壬���ý����ڵĻ���
	1. ͼƬ����������ţ�ת��ͼƬԴ�ļ���
	2. ��Ƶ������Ƶ�����޷�ȷ��������ѡ��� Twitter Դ���������Telegram ���ܻ���ѹ����
2. ת��ת���������Լ�������ý�壬���ý����ڵĻ���
	1. ������׼ͬ����
	2. ������������ĵĻ���ת���������ļ��丽����ý�岢ת���������֡�
3. ת���ظ�
	1. ����ת�����ظ����ĸ�����ý�壬���ý����ڵĻ���

## ����ʹ��

�����Խ����ű����� VPS �� Google App Engine ��ƽ̨����ʹ��֮ǰ����Ҫ����һ�� Telegram �������Լ� Twitter Ӧ�ó�����ͬ��Ҳ����ֱ���� Telegram �Ϲ�עƵ�� [Aqours �����Զ�ת��](https://t.me/MagaFunbotfield)��

### VPS

����ȷ������ VPS ��װ�� Git �Լ� Python 2.6��Ȼ�������������

`git clone https://github.com/MagaFun/AqoursTwitterStream.git
`

Ȼ�����Ŀ¼���� `config.py` ��ճ���Լ��� Token��ճ����Ϻ󱣴档

֮��������Ҫ�����ղŴ����Ļ����˸�������˽����Ϣ���� Aqours ��Ա���ظ��µĻ�������Ҫ�༭ `CHAT_ID`������ `CHAT_ID` ����ͨ����һ�������� [get_id_bot](https://telegram.me/get_id_bot) ����ȡ��

֮��ֱ�������������

`python AqoursTwitterStream.py`

��������˸���������Ϣ`������������`��˵���ű������ɹ���

�ű�ͬ������Ŀ¼�ﴴ�� `output.log` ����¼һЩ��־������֪Ϥ��

### ���˵���

��ͬ��Ҳ�������Լ��ĵ�����������ű�����ȷ�����ĵ��԰�װ�� Python 2.7��Ȼ��ֱ�����ر���Ŀ�� ZIP archive��Ȼ��ֱ��˫�� `AqoursTwitterStream.py` �����С�

## Ǳ������

* �ű�������������ֱ��ֹͣ���У�������Ҫ����������̨�����
* ��ʱ�޷�ת���ظ������ĵ�ý��
* ���ת�����ܲ��Ṥ��