from urllib import request, parse, error
import json


if __name__=="__main__":
    query = parse.urlencode({'q': 'python'})

    # httpbin은 요청 내용을 반환해 줌
    url = f'https://httpbin.org/get?{query}'
    
    try:
        with request.urlopen(url) as f:
            res = f.read().decode('utf-8')
            print(res)
    except error.HTTPError as e:
        print(e)
    #res= request.get('http://httpbin.org/get',params={'q':'python'})
    print(json.loads(res), type(res))

    print(res.json().keys)
    print(res.json()['form'])