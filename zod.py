import requests
from bs4 import BeautifulSoup


def get_horoscope(zodiac_sign: int, day: str):
    if not "-" in day:
        res = requests.get(
            f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign}")
    else:
        day = day.replace("-", "")
        res = requests.get(
            f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={day}")

    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text


if __name__ == '__main__':
    zodiac_signs = {
        "Aries": 1,
        "Taurus": 2,
        "Gemini": 3,
        "Cancer": 4,
        "Leo": 5,
        "Virgo": 6,
        "Libra": 7,
        "Scorpio": 8,
        "Sagittarius": 9,
        "Capricorn": 10,
        "Aquarius": 11,
        "Pisces": 12
    }
    print(*zodiac_signs.keys(), sep=", ")
    zodiac_symbol = input(
        "Which is your zodiac sign from the above? : ").capitalize()
    day = input("For which day do you wish to know the horoscope? For today, write 'today', else write the date in YYYY-MM-DD format : ")
    print(f"Getting horoscope for {zodiac_symbol} for {day}\n")
    print(get_horoscope(zodiac_signs[zodiac_symbol], day))
