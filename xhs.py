from DrissionPage import WebPage

page = WebPage()
page.get("https://www.xiaohongshu.com/")

page.listen.start("web/v1/search/usersearch")
while True:
    res = page.listen.wait()
    print(res.response.body)
