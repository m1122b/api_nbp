
import requests, csv

def mdata():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    return data



if __name__ == '__main__':
    
    
    data = mdata()

    rates_len = len(data[0]['rates'])
    rates = data[0]['rates']
    
    tradingdate = data[0]['tradingDate']
    print(tradingdate)

    rates_header = list([rates[0].keys()][0])
    rates_data = []

    
    for i in range(rates_len):
        rates_data.append([rates[i]['currency'],rates[i]['code'],rates[i]['bid'],rates[i]['ask']])

    print(rates_header)
    print(rates_data)

    filename = f'rates{tradingdate}.csv'
    with open(filename, 'w', encoding="utf-8", newline='') as file:
        csvwriter = csv.writer(file, delimiter=';')
        csvwriter.writerow(rates_header)
        csvwriter.writerows(rates_data)


    


