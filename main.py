import requests
import lxml
from bs4 import BeautifulSoup

class CyberAtack:
    session = requests.session()
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
    def __init__(self):
        self.url = "https://kups.club/"

    def get_response(self):
        response = self.session.get(self.url, headers=self.header)
        return response

    def get_data(self):
        for j in range(1, 21):
            print(f"PAGE = {j}")

            if self.get_response().status_code == 200:
                soup = BeautifulSoup(self.get_response().text, "lxml")
                allProduct = soup.find("div", class_="row mt-4")
                print(allProduct)
                self.products = allProduct.find_all("div", class_="col-lg-4 col-md-4 col-sm-6 portfolio-item")
                for i in range(len(self.products)):
                    try:
                        self.title = self.products[i].find("h3", class_="card-title").text
                        self.price = self.products[i].find("p", class_="card-text").text
                        with open("product.txt", "a", encoding="UTF-8") as file:
                            file.write(f"{self.title} --->>> {self.price}\n")
                        print(self.title, self.price)
                    except:
                        print(f" not for sale")

cl = CyberAtack()
print(cl.get_response())
print(cl.get_data())

