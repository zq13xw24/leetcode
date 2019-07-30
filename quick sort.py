'''
快排算法
'''

class Solotion():
    def quick_sort(self, list, start, end):
        if len(list) == 0:
            return None
        elif len(list) == 1:
            return list
        else:
            if start < end:
                m, n = start, end
                base = list[m]
                while m < n:
                    while (m<n) and list[n] >= base:
                        n = n - 1
                    list[m] = list[n]
                    while (m<n) and list[m] <= base:
                        m = m + 1
                    list[n] = list[m]
                list[m] = base
                self.quick_sort(list, start, m - 1)
                self.quick_sort(list, n + 1, end)
        return list


list = [10,1,18,30,23,12,7,5,18,17]
a = Solotion()
end = len(list) - 1
print(list)
print(a.quick_sort(list, 0, end))