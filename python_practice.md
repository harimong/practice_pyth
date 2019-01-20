##Python_code_study


- study source:
https://wikidocs.net/7022

####1. data type & variable

```
Basic: print() 하면 그냥 안에 있는거 나옴 
>>>print("Hello Wolrd")
>>>Hello World

- 문자열을 출력할 때 줄바꿈 말고 공백을 만들고 싶다면
>>>print("first", end=' ');print("second", end= ' ')
>>>first second

- 문자열 곱셈도 가능
>>>print("Hi"*3)
>>>HiHiHi

- 데이터 타입을 바꿀 때
>>>num_str = "720"
>>>num = int(num_str)

- 문자열은 배열과 같음, 배열 번지수는 0부터 시작!
>>>lang = 'python'
>>>print(lang[0])
>>>p

- 슬라이싱
>>> license_plate = "24가 2210"
>>>print(license_plate[4:])
>>>2210

>>>string = "홀짝홀짝홀짝"
>>>print(string[::2])
>>>홀홀홀

- backward print
>>> string = "PYTHON"
>>> print(string[::-1])
>>>NOHTYP

- replacing specific string
>>> phone_number = "010-1111-2222"
>>> phone_number.replace('-', ' ')
>>> 010 1111 2222

>>>string = 'abcdfe2a354a32a'
>>>string2 = string.replace('a', 'A') //변수에 넣어줘야 인식함, print(string) 하면 소문자로 출력됨(변경x)
>>>print(string2)
>>>Abcdfe2A354A32A

```
