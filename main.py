def main():
    import requests
    zipcode = input("郵便番号を入力してください。　＞")
    # zipcode = "1600023"
    url = f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}'
    # print(url)
    response = requests.get(url)
    results = response.json()['results'][0]

    都道府県名 = results["address1"]
    市区町村名 = results["address2"]
    町域名 = results["address3"]

    print(f'{都道府県名} {市区町村名} {町域名}')



if __name__ == '__main__':
    main()
