# Author:Santi
class PagnatorCustom(object):
    def __init__(self, total_num, current_page, per_page_num=20, max_page_num=11):
        self.total_num = total_num
        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1
        self.per_page_num = per_page_num
        self.max_page_num = max_page_num

    @property
    def start(self):  ###起始
        return (self.current_page - 1) * self.per_page_num

    @property
    def end(self):  ###终止
        return self.current_page * self.per_page_num

    @property
    def total_page(self):  ###总页数
        a, b = divmod(self.total_num, self.per_page_num)
        if b == 0:
            return a
        else:
            return a + 1

    def page_num(self):
        part = int(self.max_page_num / 2)
        if self.total_page < self.max_page_num:  ###当总数少于显示数量时以总数为end；
            return range(1, self.total_page)
        if self.current_page <= part:
            return range(1, self.max_page_num)  ###当当前页面值低于part时，显示范围为1到显示数量；
        if self.current_page + part > self.total_page:
            return range(self.total_page - self.max_page_num + 1,
                         self.total_page + 1)  ###如果当前页面+5大于总页数，则end为总页数，start为总页数-每页显示数 + 1
        return range(self.current_page - part, self.current_page + part + 1)  ###其他情况都显示一半

    def page_num_str(self):
        page_str_list = []
        ###首页
        first = "<li><a href='fenye3.html?p=1'>首页</a>"
        page_str_list.append(first)

        ###上一页逻辑判断
        if self.current_page == 1:
            prev = "<li><a href='javascript:void(0)'>上一页</a></li>"
        else:
            prev = "<li><a href='fenye3.html?p=%s'>上一页</a></li>" % (self.current_page - 1)
        page_str_list.append(prev)
        ###页码序列
        for i in self.page_num():
            if self.current_page == i:
                s = "<li class='active'><a href='fenye3.html?p=%s'>%s</a></li>" % (i, i)
            else:
                s = "<li><a href='fenye3.html?p=%s'>%s</a></li>" % (i, i)
            page_str_list.append(s)
        ###下一页逻辑判断
        if self.current_page == self.total_page:
            nex = "<li><a href='#'>下一页</a></li>"
        else:
            nex = "<li><a href='fenye3.html?p=%s'>下一页</a></li>" % (self.current_page + 1)
        page_str_list.append(nex)
        ###尾页逻辑判断
        last = "<li><a href='fenye3.html?p=%s'>尾页</a></li>" % self.total_page
        page_str_list.append(last)

        return ''.join(page_str_list)  ###列表转换为字符串
