from pelinrakentaja import Pelinrakentaja


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )
        vastaus = input()
        if vastaus == "a":           
            Pelinrakentaja.vastaan_ihminen().pelaa()
        elif vastaus == "b":
            Pelinrakentaja.vastaan_tekoäly().pelaa()     
        elif vastaus == "c":
            Pelinrakentaja.vastaan_kehittynyt_tekoäly().pelaa()                
        else:
            break


if __name__ == "__main__":
    main()
