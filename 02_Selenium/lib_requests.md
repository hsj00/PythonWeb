# Python library: `requests`

다른 사람들이 짜놓은 예제 코드들에 `requests` 라이브러리가 자주 등장하길래 공부하면서 정리해보았다. 아마 수시로 업데이트 될 것 같다.

----------

## 1. install & import
```shell
$ pip install requests
```
```python
import requests
```

## 2. `get`, `post`<sup>[^1]</sup>
### (1) `get`: 서버로부터 정보를 조회하기 위해 설계된 메소드
  - `GET`은 요청을 전송할 때 필요한 데이터를 `Body`에 담지 않고, 쿼리스트링을 통해 전송 (쿼리스트링: URL의 끝에 ?와 함께 이름과 값으로 쌍을 이루는 요청 파라미터)
  - 요청 파라미터가 여러개일 경우 `&`로 연결
  - 쿼리스트링을 사용할 경우, URL에 조회 조건을 표시하기 때문에 특정 페이지를 링크하거나 북마크할 수 있음
  - 불필요한 요청을 제한하기 위해 요청이 캐시될 수 있음
    - `js`, `css`, 이미지 같은 정적 컨텐츠는 데이터양이 크고, 변경될 일이 적어서 반복해서 동일한 요청을 보낼 필요가 없음
    - 정적 컨텐츠를 요청하고 나면 브라우저에서는 요청을 캐시해두고, 동일한 요청이 발생할 때 서버로 요청을 보내지 않고 캐시된 데이터를 사용
  
> ```html
> <!-- 쿼리스트링을 포함한 URL
>   파라미터명: name1, name2 / 파라미터: value1, value2 -->
> www.example-url.com/resources?name1=value1&name2=value2
> ```

### (2) `post`: 리소스를 생성/변경하기 위해 설계된 메소드
  - 전송해야될 데이터를 HTTP 메세지의 `Body`에 담아서 전송 (`Body`는 길이 제한없이 데이터 전송 가능)
  - `POST` 요청은 대용량 데이터를 전송할 수 있음
  - `POST`는 데이터가 `Body`로 전송되고 내용이 눈에 보이지 않아 `GET`보다 보안 측면에서 안전하다고 생각할 수 있지만, `POST` 요청도 크롬 개발자 도구, `Fiddler`와 같은 툴로 요청 내용을 확인할 수 있기 때문에 민감한 데이터의 경우에는 반드시 암호화해 전송
  - `POST`로 요청을 보낼 때는 요청 헤더의 `Content-Type`에 요청 데이터 타입 표시
    - 데이터 타입을 표시하지 않으면 서버는 내용이나 URL에 포함된 리소스의 확장자명 등으로 데이터 타입을 유추
    - 만약, 알 수 없는 경우에는 `application/octet-stream`로 요청을 처리

### (3) `get`, `post` 차이
- `Idempotent(멱등)`: 수학적 개념, 동일한 연산을 여러 번 수행하더라도 동일한 결과를 반환

> 수학이나 전산학에서 연산의 한 성질을 나타내는 것으로, 연산을 여러 번 적용하더라도 결과가 달라지지 않는 성질

- `GET`: `Idempotent`
  - `GET`으로 서버에 동일한 요청을 여러 번 전송하더라도 동일한 응답이 돌아와야 한다는 것을 의미
  - 설계원칙에 따라 서버의 데이터나 상태를 변경시키지 않아야 Idempotent하기 때문에 주로 조회를 할 때에 사용
  - 브라우저에서 웹페이지를 열어보거나 게시글을 읽는 등 조회를 하는 행위는 `GET`으로 요청
  - `GET`은 URL에 요청 파라미터를 가지고 있기 때문에 링크를 걸 때, URL에 파라미터를 사용해 더 디테일하게 페이지를 링크할 수 있음

- `POST`: `Non-idempotent`
  - `POST`는 Non-idempotent하기 때문에 서버에게 동일한 요청을 여러 번 전송해도 응답은 항상 다를 수 있음
  - 서버의 상태나 데이터를 변경시킬 때 사용
  - `POST`는 생성, 수정, 삭제에 사용할 수 있지만, 생성에는 `POST`, 수정은 `PUT` 또는 `PATCH`, 삭제는 `DELETE`가 더 용도에 맞는 메소드
  - `POST`는 요청 데이터가 `Body`에 담겨 있기 때문에 링크 정보를 가져올 수 없음

## 3. `requests` api<sup>[^2]</sup>
### (1). `get`
```python
# requests.get()
>>> import requests

>>> r1 = requests.get('https://api.github.com/events')

>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r2 = requests.get('https://httpbin.org/get', params=payload)

>>> print(r2.url)
https://httpbin.org/get?key2=value2&key1=value1
```
### (2). `post`
```python
# requests.post()
## 요청 보내기
>>> r1 = requests.post('https://httpbin.org/post', data = {'key':'value'})
```
#### (2)-A. `tuple`, `dictionary`, `files` 보내기
```python
## 복잡한 요청 보내기
>>> payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
>>> r1 = requests.post('https://httpbin.org/post', data=payload_tuples)

>>> payload_dict = {'key1': ['value1', 'value2']}
>>> r2 = requests.post('https://httpbin.org/post', data=payload_dict)

>>> print(r1.text)
{
  ...
  "form": { 
    "key1": [
      "value1",
      "value2"
    ]
  },
  ...
}

>>> r1.text == r2.text
True
```
```python
## 파일 보내기
>>> url = 'https://httpbin.org/post'
>>> files = {'file': open('report.xls', 'rb')}
 
>>> r = requests.post(url, files=files)
>>> r.text
{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}
```
#### (2)-B. `JSON`
```python
## JSON으로 인코딩
>>> import json
 
>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'} 
>>> r = requests.post(url, data=json.dumps(payload))
```
```python
## JSON 파라미터 이용
>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'}
>>> r = requests.post(url, json=payload)
```
### (3). `text`, `content`, `encoding`
```python
## r.text: 텍스트 형식
>>> import requests
 
>>> r = requests.get('https://api.github.com/events')
>>> r.text
'[{"id":"10674951288",...
...
...
...'

## r.content: 바이트 형식
>>> r.content
b'[{"id":"10674951288",...
...
...
...'

## r.encoding: 인코딩 형식 변환
>>> r.encoding
'utf-8'

>>> r.encoding = 'ISO-8859-1'
>>> r.encoding
'ISO-8859-1'
```

### (4). `put`, `delete`, `head`, `options`
```python
>>> r = requests.put('https://httpbin.org/put', data = {'key':'value'})

>>> r = requests.delete('https://httpbin.org/delete')

>>> r = requests.head('https://httpbin.org/get')

>>> r = requests.options('https://httpbin.org/get')
```
----------

[^1]: <https://hongsii.github.io/2017/08/02/what-is-the-difference-get-and-post/>
[^2]: <https://blog.ujsstudio.com/?p=32>