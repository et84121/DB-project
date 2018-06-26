## 套件
django

### pipfile
它是 [pipenv](https://medium.com/bryanyang0528/%E4%BD%BF%E7%94%A8-pipenv-%E7%AE%A1%E7%90%86-python-%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83-5ac2d4c39626)的東東

## 第一次啟動
 1. 裝好python3和套件 django
 2. cd board/
 3. python manage.py migrate #建立sqlite資料庫
 4. python manage.py createsuperuser #設置超級使用者(admin的帳號)
 5. python manage.py runserver #啟動debug server(有資料庫後以後只要這行就好了)

## 自已系統的預設帳密為
whale
123