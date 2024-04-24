from playwright.sync_api import sync_playwright

# 创建一个自定义的请求拦截器
class MyInterceptor:
    def __init__(self):
        self.request_content = []

    # 捕获请求，并提取请求数据包中的内容
    def on_request(self, request):
        # 获取请求的 URL
        url = request.url
        # 获取请求的方法
        method = request.method
        # 获取请求的头部
        headers = request.headers
        # 获取请求的内容
        content = request.post_data
        # 将请求信息保存到列表中
        self.request_content.append({"url": url, "method": method, "headers": headers, "content": content})

# 启动 Playwright
with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False
    )
    page = browser.new_page()

    # 实例化自定义的请求拦截器
    interceptor = MyInterceptor()

    # 启用请求拦截器
    page.on("request", interceptor.on_request)

    # 访问页面
    page.goto("https://www.xiaohongshu.com/")

    # 这里可以执行页面上的其他操作
    # page.pause()

    # 关闭浏览器
    browser.close()

# 打印捕获到的请求数据
for req in interceptor.request_content:
    print("URL:", req["url"])
    print("Method:", req["method"])
    print("Headers:", req["headers"])
    print("Content:", req["content"])
    print("--------------------------------------------")
