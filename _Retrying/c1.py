from retrying import retry
import requests


@retry(stop_max_attempt_number=3
       )  #让被装饰的函数反复执行3次，三次全部报错才会报错，中间有一次正常执行，停止重复执行，继续该方法之后的内容
def _parse_url(url):
    response = requests.get(url)
    return response.text()


def parse_url(url):
    try:
        html = _parse_url(url)
    except:
        html = None
    return html


if __name__ == '__main__':
    url = 'https://www.bing.com'
    html_str = parse_url(url)
    if html_str:
        print(html_str)
